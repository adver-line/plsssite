# Generated by Django 4.1b1 on 2022-07-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slot", "0003_alter_slot_options_alter_slot_slot_host"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slot",
            name="click_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="slot",
            name="day_count",
            field=models.CharField(
                blank=True,
                choices=[
                    ("3일", "3일"),
                    ("7일", "7일"),
                    ("10일", "10일"),
                    ("20일", "20일"),
                    ("30일", "30일"),
                ],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="slot",
            name="modyfi_check",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="slot",
            name="product_choices",
            field=models.CharField(
                blank=True,
                choices=[("단일상품", "단일상품"), ("가격비교상품", "가격비교상품")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="slot",
            name="product_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="slot",
            name="product_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="slot",
            name="serch_key",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="slot",
            name="store_names",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
