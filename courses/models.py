from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """A course like Digital Marketing or SEO."""
    COURSE_CHOICES = [
        ('dm', 'Digital Marketing'),
        ('seo', 'SEO'),
    ]
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='bi-book')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def total_lessons(self):
        return self.lessons.count()


class Lesson(models.Model):
    """An individual lesson within a course."""
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='lessons'
    )
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    youtube_url = models.URLField(
        help_text="Full YouTube URL (e.g., https://www.youtube.com/watch?v=...)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['course', 'order']
        unique_together = ('course', 'order')

    def __str__(self):
        return f"[{self.course.name}] {self.title}"

    @property
    def embed_url(self):
        """Convert a YouTube watch URL into an embed URL.

        Uses youtube-nocookie.com, which avoids the stale-cookie
        'error 153 - video player configuration' problem in browsers.
        """
        url = self.youtube_url
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0]
        elif 'v=' in url:
            video_id = url.split('v=')[1].split('&')[0]
        else:
            return url
        return f"https://www.youtube-nocookie.com/embed/{video_id}"


class UserProgress(models.Model):
    """Tracks which lessons a user has completed."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='progress'
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.user.username} - {self.lesson.title} {status}"
