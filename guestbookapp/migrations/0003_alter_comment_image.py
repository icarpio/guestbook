# Generated by Django 5.1.2 on 2024-10-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbookapp', '0002_alter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='No Image', upload_to='images/'),
            preserve_default=False,
        ),
    ]