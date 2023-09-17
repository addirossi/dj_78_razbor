from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(unique=True, max_length=60)
    slug = models.CharField(primary_key=True, max_length=60)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    #def clean(self):
        #

    class Meta:
        db_table = 'main_category'


# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, models.DO_NOTHING) #category_id
    # tags = models.ManyToManyField(Tag, related_name='scopes', through='OrderItemsInlineForm')
    # product.scopes.all()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_product'
        # ordering = ['price']
        # verbose_name = '...'
        # constraints = ...



# class ProductTags(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scopes',)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     is_main = models.BooleanField(default=False)
    #product.scopes.all()
    #ProductTags.objects.filter(product=product)


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItems')

    def __str__(self):
        return f'Заказ №: {self.id}'

    class Meta:
        db_table = 'main_order'


class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.SmallIntegerField()
    order = models.ForeignKey(Order, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        db_table = 'main_orderitems'
