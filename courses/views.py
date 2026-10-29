from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from .models import Course, Lesson, UserProgress


def landing(request):
    """SEO-optimized landing page. Redirects logged-in users to dashboard."""
    if request.user.is_authenticated:
        return redirect('courses:dashboard')
    return render(request, 'courses/landing.xhtml')


def register(request):
    """User registration."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('courses:dashboard')

    return render(request, 'registration/register.xhtml', {'form': form})


@login_required
def dashboard(request):
    """Course selection page with progress summary."""
    courses = Course.objects.all()
    user_progress = UserProgress.objects.filter(
        user=request.user, completed=True
    )
    completed_lesson_ids = set(user_progress.values_list('lesson_id', flat=True))

    # Build progress info per course
    course_data = []
    for course in courses:
        total = course.lessons.count()
        done = course.lessons.filter(id__in=completed_lesson_ids).count()
        percent = int((done / total) * 100) if total else 0
        course_data.append({
            'course': course,
            'total': total,
            'done': done,
            'percent': percent,
        })

    return render(request, 'courses/dashboard.xhtml', {'course_data': course_data})


@login_required
def course_detail(request, slug):
    """List lessons for a selected course with completion status."""
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.all()

    completed_ids = set(
        UserProgress.objects.filter(
            user=request.user, completed=True
        ).values_list('lesson_id', flat=True)
    )

    lesson_data = [
        {'lesson': lesson, 'completed': lesson.id in completed_ids}
        for lesson in lessons
    ]

    done = sum(1 for l in lesson_data if l['completed'])
    total = len(lesson_data)
    percent = int((done / total) * 100) if total else 0

    context = {
        'course': course,
        'lesson_data': lesson_data,
        'done': done,
        'total': total,
        'percent': percent,
    }
    return render(request, 'courses/course_detail.xhtml', context)


@login_required
def lesson_detail(request, lesson_id):
    """Show a lesson with embedded video, resources, and progress toggle."""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, _ = UserProgress.objects.get_or_create(
        user=request.user, lesson=lesson
    )

    # Find next/prev lessons
    siblings = list(lesson.course.lessons.all())
    idx = next((i for i, l in enumerate(siblings) if l.id == lesson.id), None)
    prev_lesson = siblings[idx - 1] if idx and idx > 0 else None
    next_lesson = siblings[idx + 1] if idx is not None and idx < len(siblings) - 1 else None

    context = {
        'lesson': lesson,
        'course': lesson.course,
        'progress': progress,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
    }
    return render(request, 'courses/lesson_detail.xhtml', context)


@login_required
def toggle_progress(request, lesson_id):
    """Mark a lesson as complete or incomplete."""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, _ = UserProgress.objects.get_or_create(
        user=request.user, lesson=lesson
    )
    progress.completed = not progress.completed
    progress.completed_at = timezone.now() if progress.completed else None
    progress.save()

    return redirect('courses:lesson_detail', lesson_id=lesson.id)
