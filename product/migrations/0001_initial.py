# Generated by Django 3.2 on 2022-06-25 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_az', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('sort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EvDekorProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('is_featured', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('order_count', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produevdekorproductscts', to='product.color')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evdekorproducts', to='product.category')),
            ],
            options={
                'verbose_name': 'Məhsullar - EV ÜÇÜN DEKOR',
                'verbose_name_plural': 'Məhsullar - EV ÜÇÜN DEKOR',
            },
        ),
        migrations.CreateModel(
            name='FotoOboyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('is_featured', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('order_count', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.color')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.category')),
            ],
            options={
                'verbose_name': 'Məhsullar - FOTOOBOY VE FRESKA',
                'verbose_name_plural': 'Məhsullar - FOTOOBOY VE FRESKA',
            },
        ),
        migrations.CreateModel(
            name='Interier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('texture_image', models.FileField(upload_to='')),
                ('youtube_url', models.CharField(blank=True, max_length=255, null=True)),
                ('material_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('idd', models.CharField(max_length=255)),
                ('iddd', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Materiallar - FOTOOBOY VE FRESKA',
                'verbose_name_plural': 'Materiallar - FOTOOBOY VE FRESKA',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SKINALI ', max_length=250)),
                ('name_en', models.CharField(default='SKINALI ', max_length=250, null=True)),
                ('name_az', models.CharField(default='SKINALI ', max_length=250, null=True)),
                ('name_ru', models.CharField(default='SKINALI ', max_length=250, null=True)),
                ('code', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.FloatField(default=30)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('order_count', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.color')),
                ('main_category', models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_az', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SkinaliProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('is_featured', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('order_count', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skinaliproducts', to='product.color')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skinaliproducts', to='product.category')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skinaliproducts', to='product.room')),
            ],
            options={
                'verbose_name': 'Məhsullar - SKİNALİ',
                'verbose_name_plural': 'Məhsullar - SKİNALİ',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_az', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='product.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SkinaliProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.skinaliproduct')),
            ],
        ),
        migrations.AddField(
            model_name='skinaliproduct',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skinaliproducts', to='product.subcategory'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.room'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.Tag'),
        ),
        migrations.CreateModel(
            name='FotoOboyProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.fotooboyproduct')),
            ],
        ),
        migrations.AddField(
            model_name='fotooboyproduct',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.room'),
        ),
        migrations.AddField(
            model_name='fotooboyproduct',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.subcategory'),
        ),
        migrations.CreateModel(
            name='EvDekorProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.evdekorproduct')),
            ],
        ),
        migrations.AddField(
            model_name='evdekorproduct',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evdekorproducts', to='product.room'),
        ),
        migrations.AddField(
            model_name='evdekorproduct',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evdekorproducts', to='product.subcategory'),
        ),
    ]
