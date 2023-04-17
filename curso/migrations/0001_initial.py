# Generated by Django 4.1.7 on 2023-04-02 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=10000)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('precio', models.FloatField()),
                ('cantidad_videos', models.IntegerField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='curso/imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=10000)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='curso/videos/')),
                ('curso_pertenece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
            ],
        ),
    ]
