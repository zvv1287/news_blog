# Generated by Django 2.2.7 on 2019-12-08 09:05

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('status', models.BooleanField(default=False, verbose_name='Только для зарегистрированных')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название пункта меню на сайте')),
                ('name', models.CharField(max_length=255, verbose_name='Название латиницей')),
                ('status', models.BooleanField(default=False, verbose_name='Только для зарегистрированных')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='url на внешний ресурс')),
                ('anchor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Якорь')),
                ('object_id', models.PositiveIntegerField(default=1, null=True, verbose_name='Id записи')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Ссылка на')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='Меню')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.MenuItem', verbose_name='Родительский пункт')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
