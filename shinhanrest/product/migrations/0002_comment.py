# Generated by Django 4.1.5 on 2023-01-19 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글내용')),
                ('tstamp', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글',
                'db_table': 'comment',
            },
        ),
    ]
