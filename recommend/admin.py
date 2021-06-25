from django.contrib import admin
from recommend.models import Category, Product, ProductImage, ProductTag, Review, ReviewImage, ReviewTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'created_at'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'prod_no',
        'prod_name',
        'prod_manufacturer',
        'prod_price',
        'created_at',
        'updated_at'
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'prod_no',
        'prod_img_path',
        'prod_is_thumbnail',
        'upload_user_no',
        'created_at'
    )


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = (
        'prod',
        'tag',
        'created_at'
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user_no',
        'prod_no',
        'review_title',
        'review_text',
        'review_img_thumbnail',
        'func1_rate',
        'func2_rate',
        'func3_rate',
        'created_at',
        'updated_at'
    )


@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = (
        'img_path',
        'review_user_no',
        'created_at'
    )


@admin.register(ReviewTag)
class ReviewTagAdmin(admin.ModelAdmin):
    list_display = [
        'review_no',
        'tag',
        'created_at'
    ]
