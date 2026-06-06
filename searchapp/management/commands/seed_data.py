import json
import urllib.request
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from searchapp.models import (
    SiteVisit,
    bagmodel_english_json,
    pantsmodel_english_json,
    shoesmodel_english_json,
    tshirtmodel_english_json,
)

MEDIA_ROOT = Path(settings.BASE_DIR) / 'public' / 'static' / 'media'
JSON_DIR = Path(__file__).resolve().parent

OTHER_PRODUCTS = {
    'pants': [
        {
            'id': 'p1001',
            'title_fa': 'شلوار جین زنانه آبی تیره',
            'description': 'شلوار جین زنانه با فیت اسلیم، رنگ آبی تیره، مناسب استفاده روزمره.',
            'attributes': 'جنس: جین, رنگ: آبی تیره, فیت: اسلیم',
            'image_url': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400',
            'page_url': 'https://www.digikala.com',
        },
        {
            'id': 'p1002',
            'title_fa': 'شلوار کتان مردانه بژ',
            'description': 'شلوار کتان راحت با رنگ بژ، مناسب فصل گرم و استایل کژوال.',
            'attributes': 'جنس: کتان, رنگ: بژ, فیت: راحت',
            'image_url': 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400',
            'page_url': 'https://www.digikala.com',
        },
        {
            'id': 'p1003',
            'title_fa': 'شلوار ورزشی مشکی',
            'description': 'شلوار ورزشی با پارچه نرم و کشسان، مناسب ورزش و پیاده‌روی.',
            'attributes': 'جنس: پلی‌استر, رنگ: مشکی, نوع: ورزشی',
            'image_url': 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400',
            'page_url': 'https://www.digikala.com',
        },
    ],
    'bag': [
        {
            'id': 'b2001',
            'title_fa': 'کیف دوشی چرمی قهوه‌ای',
            'description': 'کیف دوشی چرم مصنوعی با طراحی کلاسیک و بند قابل تنظیم.',
            'attributes': 'جنس: چرم مصنوعی, رنگ: قهوه‌ای, نوع: دوشی',
            'image_url': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400',
            'page_url': 'https://www.digikala.com',
        },
        {
            'id': 'b2002',
            'title_fa': 'کیف دستی زنانه مشکی',
            'description': 'کیف دستی شیک با جیب داخلی و بند کوتاه، مناسب مهمانی.',
            'attributes': 'جنس: چرم, رنگ: مشکی, نوع: دستی',
            'image_url': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400',
            'page_url': 'https://www.digikala.com',
        },
        {
            'id': 'b2003',
            'title_fa': 'کوله‌پشتی روزمره خاکستری',
            'description': 'کوله‌پشتی سبک با جای لپ‌تاپ و طراحی مدرن.',
            'attributes': 'جنس: برزنت, رنگ: خاکستری, نوع: کوله‌پشتی',
            'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400',
            'page_url': 'https://www.digikala.com',
        },
    ],
    'shoes': [
        {
            'id': 's3001',
            'title_fa': 'کفش کتانی سفید زنانه',
            'description': 'کفش کتانی سبک و راحت با رویه مشبک، مناسب پیاده‌روی روزانه.',
            'attributes': 'جنس: مش, رنگ: سفید, نوع: کتانی',
            'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400',
            'page_url': 'https://www.digikala.com',
        },
        {
            'id': 's3002',
            'title_fa': 'کفش رسمی مردانه مشکی',
            'description': 'کفش چرم مصنوعی با طراحی کلاسیک، مناسب محیط اداری.',
            'attributes': 'جنس: چرم مصنوعی, رنگ: مشکی, نوع: رسمی',
            'image_url': 'https://picsum.photos/seed/shoe-formal/400/400',
            'page_url': 'https://www.digikala.com',
        },
        {
            'id': 's3003',
            'title_fa': 'صندل تابستانی زنانه',
            'description': 'صندل راحت با کفی نرم و بند قابل تنظیم.',
            'attributes': 'جنس: پلاستیک, رنگ: بژ, نوع: صندل',
            'image_url': 'https://picsum.photos/seed/shoe-sandal/400/400',
            'page_url': 'https://www.digikala.com',
        },
    ],
}


def format_attributes(attrs):
    if isinstance(attrs, list):
        return ', '.join(f"{item['key']}: {item['value']}" for item in attrs if 'key' in item)
    return str(attrs)


def build_description(title, attrs):
    attr_text = format_attributes(attrs)
    return f'{title}. {attr_text}' if attr_text else title


def download_image(url, dest_path):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    if dest_path.exists() and dest_path.stat().st_size > 0:
        return True
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=30) as response:
            dest_path.write_bytes(response.read())
        return True
    except Exception:
        return False


class Command(BaseCommand):
    help = 'Seed the database with sample products and download images.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--per-file',
            type=int,
            default=3,
            help='Number of t-shirts to import from each JSON file (default: 3)',
        )

    def handle(self, *args, **options):
        per_file = options['per_file']
        created = 0
        images_ok = 0

        for json_file in sorted(JSON_DIR.glob('file_*.json')):
            with open(json_file, encoding='utf-8') as handle:
                products = json.load(handle)
            for item in products[:per_file]:
                product_id = str(item['id'])
                title = item['title_fa']
                attrs = item.get('attributes', [])
                image_url = item['image']['main']['url']
                attributes_text = format_attributes(attrs)
                description = build_description(title, attrs)
                image_path = MEDIA_ROOT / 'tshirt' / product_id / 'pic1.jpg'

                tshirtmodel_english_json.objects.update_or_create(
                    id=product_id,
                    defaults={
                        'title_fa': title,
                        'description': description,
                        'image_link': image_url,
                        'attributes': attributes_text,
                    },
                )
                created += 1
                if download_image(image_url, image_path):
                    images_ok += 1
                    self.stdout.write(f'  tshirt/{product_id}/pic1.jpg')

        category_models = {
            'pants': pantsmodel_english_json,
            'bag': bagmodel_english_json,
            'shoes': shoesmodel_english_json,
        }
        for category, items in OTHER_PRODUCTS.items():
            Model = category_models[category]
            for item in items:
                image_path = MEDIA_ROOT / category / item['id'] / 'pic1.jpg'
                Model.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'title_fa': item['title_fa'],
                        'description': item['description'],
                        'image_link': item['page_url'],
                        'attributes': item['attributes'],
                    },
                )
                created += 1
                if download_image(item['image_url'], image_path):
                    images_ok += 1
                    self.stdout.write(f'  {category}/{item["id"]}/pic1.jpg')

        SiteVisit.objects.get_or_create(pk=1, defaults={'total_visits': 0})

        db = settings.DATABASES['default']
        self.stdout.write(self.style.SUCCESS(
            f'Done: {created} products saved, {images_ok} images downloaded.'
        ))
        self.stdout.write(
            f'Database: {db["ENGINE"].split(".")[-1]}://{db["HOST"]}:{db.get("PORT", "5432")}/{db["NAME"]}'
        )
