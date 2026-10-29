from django.core.management.base import BaseCommand
from courses.models import Course, Lesson


class Command(BaseCommand):
    help = "Seed initial Digital Marketing and SEO courses"

    def handle(self, *args, **kwargs):
        dm, _ = Course.objects.get_or_create(
            slug='digital-marketing',
            defaults=dict(
                name='Digital Marketing',
                description='Master marketing strategy, social media, content, and analytics.',
                icon='bi-megaphone',
            ),
        )
        seo, _ = Course.objects.get_or_create(
            slug='seo',
            defaults=dict(
                name='SEO',
                description='Learn on-page, off-page, and technical SEO with keyword research.',
                icon='bi-search',
            ),
        )

        lessons = [
            (dm, 1, 'Introduction to Digital Marketing',
             'https://www.youtube.com/watch?v=bixR-KIJKYM'),
            (dm, 2, 'Content Marketing Fundamentals',
             'https://www.youtube.com/watch?v=COod8hv98sg'),
            (seo, 1, 'SEO Basics: How Search Engines Work',
             'https://www.youtube.com/watch?v=0eKVizvYSUQ'),
            (seo, 2, 'Keyword Research',
             'https://www.youtube.com/watch?v=VPDe8XL7Mh8'),
        ]

        for course, order, title, yt in lessons:
            Lesson.objects.get_or_create(
                course=course, order=order,
                defaults=dict(title=title, youtube_url=yt),
            )

        self.stdout.write(self.style.SUCCESS('Seeded courses and lessons.'))
