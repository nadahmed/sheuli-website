# Generated by Django 4.1.10 on 2023-09-01 14:47

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('images', wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock())], use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]