# Generated by Django 2.1.7 on 2019-03-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumePage', '0003_bullet_related_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bars',
            name='subtitleImg',
            field=models.FileField(blank=True, default=None, upload_to='resumePage/svg/content'),
        ),
        migrations.AlterField(
            model_name='bullet',
            name='bulletImage',
            field=models.FileField(blank=True, default=None, upload_to='resumePage/svg/bullet'),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='resumePage/img/profilePic/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='subtitleImg',
            field=models.FileField(blank=True, default=None, upload_to='resumePage/svg/content'),
        ),
        migrations.AlterField(
            model_name='text',
            name='subtitleImg',
            field=models.FileField(blank=True, default=None, upload_to='resumePage/svg/content'),
        ),
    ]