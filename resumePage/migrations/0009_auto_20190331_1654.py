# Generated by Django 2.1.7 on 2019-03-31 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumePage', '0008_auto_20190331_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bars',
            name='bullet',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bars_content', to='resumePage.Bullet'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='bullet',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_content', to='resumePage.Bullet'),
        ),
        migrations.AlterField(
            model_name='text',
            name='bullet',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_content', to='resumePage.Bullet'),
        ),
    ]
