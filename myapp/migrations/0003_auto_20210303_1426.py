# Generated by Django 3.1.7 on 2021-03-03 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_author_author1_book_books_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='current_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.reader'),
        ),
    ]
