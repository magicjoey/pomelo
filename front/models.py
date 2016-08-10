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
