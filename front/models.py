from django.db import models

# Create your models here.
class Banner(models.Model):
    path = models.CharField(max_length=255)
    url = models.CharField(max_length=1024)
    priority = models.IntegerField()
    related_id = models.IntegerField(blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_banner'


class Nav(models.Model):
    title = models.CharField(max_length=32, verbose_name="标题")
    priority = models.IntegerField(verbose_name="优先级（值越小越靠前）")
    url = models.CharField(max_length=255, verbose_name="链接地址")
    level = models.IntegerField(blank=True, null=True, verbose_name="菜单级别")
    path = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片链接")

    class Meta:
        managed = False
        db_table = 'tb_nav'


class SystemSetting(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    value = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_system_setting'



class Contact(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="邮箱")
    name = models.CharField(max_length=32, blank=True, null=True, verbose_name="名字")
    content = models.CharField(max_length=2048, blank=True, null=True, verbose_name="内容")
    gmt_create = models.DateTimeField(blank=True, null=True, verbose_name="时间")
    status = models.CharField(max_length=1, blank=True, null=True, verbose_name="状态")

    class Meta:
        managed = False
        db_table = 'tb_contact'


class Download(models.Model):
    type = models.CharField(max_length=32, blank=True, null=True)
    download_img = models.CharField(max_length=256, blank=True, null=True)
    qrcode_img = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_download'


class Product(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    face_img = models.CharField(max_length=256, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    video_url = models.CharField(max_length=1024, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_product'


class ProductImg(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)
    img_address = models.CharField(max_length=255, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_product_img'


class ProductImgType(models.Model):
    type = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_product_img_type'

class Aboutus(models.Model):
    content = models.TextField(blank=True, null=True)
    title = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_aboutus'