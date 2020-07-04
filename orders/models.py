from django.db import models
from shop.models import Product
#from phone_field import PhoneField

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50,verbose_name="Фамилия")
    email = models.EmailField()
    address = models.CharField(max_length=350,verbose_name="Адрес доставки")
    phone = models.CharField(max_length=13,verbose_name="Телефон")
    com= models.CharField(max_length=350,blank = True,verbose_name="Комментарий")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                related_name='items',
                on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',
                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity