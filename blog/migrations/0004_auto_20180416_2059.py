# Generated by Django 2.0.3 on 2018-04-16 12:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180414_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='正文内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=None, to='blog.Category', verbose_name='文章分类'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='文章标签'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titleimg',
            field=models.ImageField(blank=True, null=True, upload_to='titleimg/%Y/%m/%d/', verbose_name='标题图片'),
        ),
    ]