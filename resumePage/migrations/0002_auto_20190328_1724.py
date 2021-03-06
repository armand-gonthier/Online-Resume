# Generated by Django 2.1.7 on 2019-03-28 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumePage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullet',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bullets', to='resumePage.Section'),
        ),
        migrations.AlterField(
            model_name='progressbar',
            name='bar',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='progress_bars', to='resumePage.Bars'),
        ),
        migrations.AlterField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='resumePage.Portfolio'),
        ),
    ]
