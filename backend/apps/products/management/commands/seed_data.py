"""
珠合种子数据 — 运行方式:
  cd backend
  python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.products.models import Category, Collection, Product, ProductVariant, ProductTag


SEED_DATA = {
    "categories": [
        {"name": "Akoya 珍珠", "name_en": "Akoya Pearls", "slug": "akoya", "sort_order": 1, "description": "日本 Akoya 珍珠 — 以极致圆润和明亮光泽闻名于世"},
        {"name": "南洋珍珠", "name_en": "South Sea Pearls", "slug": "south-sea", "sort_order": 2, "description": "南洋珍珠 — 体积硕大，丝缎光泽，温暖色调"},
        {"name": "淡水珍珠", "name_en": "Freshwater Pearls", "slug": "freshwater", "sort_order": 3, "description": "淡水珍珠 — 形态丰富，色彩缤纷，亲民之选"},
    ],
    "collections": [
        {"name": "Akoya Classics", "slug": "akoya-classics", "subtitle": "The quintessential Japanese pearl", "bg_gradient": "from-lavender-300 to-lavender-500", "is_featured": True, "sort_order": 1, "description": "Luminous, perfectly round, eternally elegant."},
        {"name": "South Sea Treasures", "slug": "south-sea-treasures", "subtitle": "Largest of all cultured pearls", "bg_gradient": "from-sandy-300 to-sandy-500", "is_featured": True, "sort_order": 2, "description": "Prized for their satiny luster and warm golden hues."},
        {"name": "Freshwater Essence", "slug": "freshwater-essence", "subtitle": "Nature's diverse beauty", "bg_gradient": "from-lake-200 to-lake-400", "is_featured": False, "sort_order": 3},
    ],
    "products": [
        {
            "name": "Akoya 经典珍珠项链",
            "name_en": "Akoya Classic Pearl Necklace",
            "slug": "akoya-classic-necklace",
            "sku_prefix": "AKO-N",
            "short_description": "甄选日本 Akoya 珍珠，7-7.5mm 正圆强光，18K白金扣头",
            "description": "精选来自日本濑户内海的优质 Akoya 珍珠，每一颗都经过严格筛选。\n\n• 珍珠：日本 Akoya，7-7.5mm\n• 形状：正圆\n• 光泽：极强\n• 品质：AAA 级\n• 材质：18K 白金扣头\n• 链长：45cm",
            "pearl_type": "akoya", "pearl_size": "7-7.5mm", "pearl_shape": "正圆",
            "pearl_color": "白色带粉光", "pearl_luster": "极强", "pearl_quality": "AAA",
            "material": "18K 白金",
            "base_price": 5880, "is_price_from": True,
            "is_featured": True, "is_new": False, "sort_order": 1,
            "category_slug": "akoya", "collection_slugs": ["akoya-classics"],
            "variants": [
                {"name": "链长 45cm", "chain_length": "45cm", "price": 5880, "stock": 10, "is_default": True},
                {"name": "链长 50cm", "chain_length": "50cm", "price": 6280, "stock": 8},
            ],
            "tags": ["best-seller", "necklace"],
        },
        {
            "name": "Akoya 珍珠耳环",
            "name_en": "Akoya Pearl Earrings",
            "slug": "akoya-pearl-earrings",
            "sku_prefix": "AKO-E",
            "short_description": "单颗 Akoya 珍珠耳钉，7mm 正圆，18K白金镶嵌",
            "description": "经典单珠耳钉设计，让珍珠本身成为绝对主角。\n\n• 珍珠：日本 Akoya，7mm\n• 形状：正圆\n• 光泽：极强\n• 品质：AAA 级\n• 材质：18K 白金耳针\n• 耳堵：18K 白金",
            "pearl_type": "akoya", "pearl_size": "7mm", "pearl_shape": "正圆",
            "pearl_color": "白色带粉光", "pearl_luster": "极强", "pearl_quality": "AAA",
            "material": "18K 白金",
            "base_price": 2880, "is_price_from": False,
            "is_featured": True, "is_new": True, "sort_order": 2,
            "category_slug": "akoya", "collection_slugs": ["akoya-classics"],
            "variants": [
                {"name": "标准款", "price": 2880, "stock": 15, "is_default": True},
            ],
            "tags": ["new-arrival", "earrings"],
        },
        {
            "name": "南洋金珠项链",
            "name_en": "Golden South Sea Pearl Necklace",
            "slug": "golden-south-sea-necklace",
            "sku_prefix": "SS-N",
            "short_description": "南洋金珠 10-12mm，浓郁金黄色，18K金扣头",
            "description": "来自南洋温暖水域的金色珍珠，以其硕大的尺寸和丝缎般的光泽著称。\n\n• 珍珠：南洋金珠，10-12mm\n• 形状：近圆\n• 光泽：强\n• 品质：AA+ 级\n• 材质：18K 黄金扣头\n• 链长：45cm",
            "pearl_type": "south_sea", "pearl_size": "10-12mm", "pearl_shape": "近圆",
            "pearl_color": "浓郁金黄", "pearl_luster": "强", "pearl_quality": "AA+",
            "material": "18K 黄金",
            "base_price": 16800, "is_price_from": False,
            "is_featured": True, "is_new": False, "sort_order": 3,
            "category_slug": "south-sea", "collection_slugs": ["south-sea-treasures"],
            "variants": [
                {"name": "链长 45cm", "chain_length": "45cm", "price": 16800, "stock": 5, "is_default": True},
            ],
            "tags": ["luxury", "necklace"],
        },
        {
            "name": "南洋白蝶贝珍珠戒指",
            "name_en": "South Sea Pearl Ring",
            "slug": "south-sea-pearl-ring",
            "sku_prefix": "SS-R",
            "short_description": "南洋白蝶贝珍珠 11mm，银白色光泽，18K白金镶嵌",
            "description": "南洋白蝶贝珍珠以其独特的银白色光泽和丝绸质感深受喜爱。\n\n• 珍珠：南洋白蝶贝，11mm\n• 形状：正圆\n• 光泽：极强\n• 品质：AAA 级\n• 材质：18K 白金戒托\n• 可调节圈口",
            "pearl_type": "south_sea", "pearl_size": "11mm", "pearl_shape": "正圆",
            "pearl_color": "银白", "pearl_luster": "极强", "pearl_quality": "AAA",
            "material": "18K 白金",
            "base_price": 9800, "is_price_from": True,
            "is_featured": False, "is_new": True, "sort_order": 4,
            "category_slug": "south-sea", "collection_slugs": ["south-sea-treasures"],
            "variants": [
                {"name": "圈口 14号", "price": 9800, "stock": 5, "is_default": True},
                {"name": "圈口 16号", "price": 9800, "stock": 6},
            ],
            "tags": ["new-arrival", "ring"],
        },
    ],
}


class Command(BaseCommand):
    help = "填充珠合项目种子数据"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("🌊 正在填充珠合种子数据...\n"))

        # Categories
        for data in SEED_DATA["categories"]:
            obj, created = Category.objects.update_or_create(
                slug=data["slug"], defaults=data
            )
            self.stdout.write(f"  {'✅' if created else '🔄'} Category: {obj.name}")

        # Collections
        for data in SEED_DATA["collections"]:
            obj, created = Collection.objects.update_or_create(
                slug=data["slug"], defaults=data
            )
            self.stdout.write(f"  {'✅' if created else '🔄'} Collection: {obj.name}")

        # Tags
        all_tags = {}
        for pdata in SEED_DATA["products"]:
            for tname in pdata.get("tags", []):
                if tname not in all_tags:
                    tag, _ = ProductTag.objects.get_or_create(name=tname, defaults={"slug": slugify(tname)})
                    all_tags[tname] = tag

        # Products + Variants
        for pdata in SEED_DATA["products"]:
            tag_names = pdata.pop("tags", [])
            variant_data = pdata.pop("variants", [])
            cat_slug = pdata.pop("category_slug", None)
            col_slugs = pdata.pop("collection_slugs", [])

            if cat_slug:
                try:
                    pdata["category"] = Category.objects.get(slug=cat_slug)
                except Category.DoesNotExist:
                    pass

            product, created = Product.objects.update_or_create(
                slug=pdata["slug"], defaults=pdata
            )

            # Collections
            for cslug in col_slugs:
                try:
                    col = Collection.objects.get(slug=cslug)
                    product.collections.add(col)
                except Collection.DoesNotExist:
                    pass

            # Tags
            for tname in tag_names:
                if tname in all_tags:
                    product.tags.add(all_tags[tname])

            # Variants
            for vdata in variant_data:
                ProductVariant.objects.update_or_create(
                    product=product,
                    name=vdata["name"],
                    defaults=vdata,
                )

            self.stdout.write(f"  {'✅' if created else '🔄'} Product: {product.name} ({len(variant_data)} SKUs)")

        # Summary
        counts = {
            "Category": Category.objects.count(),
            "Collection": Collection.objects.count(),
            "Product": Product.objects.count(),
            "Variant": ProductVariant.objects.count(),
            "Tag": ProductTag.objects.count(),
        }
        self.stdout.write(self.style.SUCCESS(f"\n📊 种子数据填充完成:"))
        for name, count in counts.items():
            self.stdout.write(f"    {name}: {count}")
