# Generated by Django 4.2.17 on 2024-12-17 08:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('rack_number', models.CharField(max_length=10)),
                ('total_copies', models.IntegerField(default=1)),
                ('available_copies', models.IntegerField(default=1)),
                ('usage_statistics', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('member_type', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('RS', 'Research Scholar'), ('FC', 'Faculty')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('due_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('penalty', models.FloatField(default=0.0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library_App.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library_App.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='issued_books',
            field=models.ManyToManyField(through='Library_App.Transaction', to='Library_App.book'),
        ),
    ]