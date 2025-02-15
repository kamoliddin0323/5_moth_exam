from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Seller(BaseModel):
    name = models.CharField()
    sotilgan_maxsulot = models.IntegerField()
    daromadi = models.IntegerField()
    image = models.ImageField()
    background_image = models.ImageField()



class Category(BaseModel):
    name = models.CharField()
    icon = models.ImageField()


class ProductImage(BaseModel):
    image =  models.ImageField()


class Product(BaseModel):
    name = models.CharField(max_length=355)
    owner = models.ForeignKey(Seller,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    betlar_soni = models.IntegerField()
    hajmi = models.FloatField()
    turi = models.CharField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ManyToManyField.many_to_many(ProductImage,on_delete=models.CASCADE)    


