from django.db import models

# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey('authentication.User',
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey('marchant.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    ref_code = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('authentication.User',
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email

    def get_total(self):
        total = 0
        for order_item in self.products.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total
    total = property(get_total)

class Payment(models.Model):
    ref_id = models.CharField(max_length=50, null=True)
    user = models.ForeignKey('authentication.User',
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField(null=True)
    authorization = models.CharField(max_length=60, null=True)
    is_payed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.email

class Coupon(models.Model):
    code = models.CharField(max_length=15, null=True)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.code

class Viewed(models.Model):
    product = models.ManyToManyField('marchant.Product')    