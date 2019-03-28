# Generated by Django 2.1.7 on 2019-03-28 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, default=None, max_length=256)),
                ('subtitleImg', models.ImageField(blank=True, default=None, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bullet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256)),
                ('bulletImage', models.ImageField(blank=True, default=None, upload_to='')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('surname', models.CharField(default='', max_length=256)),
                ('profession', models.CharField(default='', max_length=256)),
                ('introduction', models.TextField(default='')),
                ('profile_pic', models.ImageField(blank=True, default=None, null=True, upload_to='resumePage/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, default=None, max_length=256)),
                ('subtitleImg', models.ImageField(blank=True, default=None, upload_to='')),
                ('bullet', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_content', to='resumePage.Bullet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgressBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=256)),
                ('percentage', models.IntegerField()),
                ('bar', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='progress_bar', to='resumePage.Bars')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('illustration', models.ImageField(blank=True, null=True, upload_to='')),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to='resumePage.Portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256, unique=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, default=None, max_length=256)),
                ('subtitleImg', models.ImageField(blank=True, default=None, upload_to='')),
                ('description', models.TextField(default='')),
                ('bullet', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='text_content', to='resumePage.Bullet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bullet',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bullet', to='resumePage.Section'),
        ),
        migrations.AddField(
            model_name='bars',
            name='bullet',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bars_content', to='resumePage.Bullet'),
        ),
    ]
