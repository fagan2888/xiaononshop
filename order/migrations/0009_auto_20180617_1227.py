# Generated by Django 2.0.6 on 2018-06-17 04:27

from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20180617_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=10, verbose_name='地區')),
            ],
        ),
        migrations.CreateModel(
            name='AreaLimitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remain', models.IntegerField(verbose_name='剩於個數')),
                ('limitation', models.IntegerField(verbose_name='上限個數')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Area', verbose_name='地區')),
            ],
        ),
        migrations.RemoveField(
            model_name='locationalimitation',
            name='bento',
        ),
        migrations.RemoveField(
            model_name='locationalimitation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='distributionplace',
            name='location',
        ),
        migrations.RemoveField(
            model_name='lineprofile',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='order',
            name='location',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
        migrations.AddField(
            model_name='lineprofile',
            name='job',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='order.Job', verbose_name='職業'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bento',
            name='bento_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.BentoType', verbose_name='類型'),
        ),
        migrations.AlterField(
            model_name='bento',
            name='cuisine',
            field=models.TextField(max_length=200, verbose_name='菜色'),
        ),
        migrations.AlterField(
            model_name='bento',
            name='date',
            field=models.DateField(verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='bento',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名稱'),
        ),
        migrations.AlterField(
            model_name='bento',
            name='photo',
            field=models.ImageField(upload_to=order.models.image_path_wrapper, verbose_name='照片'),
        ),
        migrations.AlterField(
            model_name='bento',
            name='price',
            field=models.IntegerField(default=120, verbose_name='價格'),
        ),
        migrations.AlterField(
            model_name='bento',
            name='ready',
            field=models.BooleanField(default=False, verbose_name='上架'),
        ),
        migrations.AlterField(
            model_name='distributionplace',
            name='distribution_place',
            field=models.CharField(max_length=20, verbose_name='發放地點'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='電子郵件'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='line_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='LineID'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='line_name',
            field=models.CharField(max_length=100, verbose_name='Line名稱'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='電話'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='picture_url',
            field=models.URLField(verbose_name='照片網址'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='state',
            field=models.CharField(blank=True, max_length=10, verbose_name='狀態'),
        ),
        migrations.AlterField(
            model_name='lineprofile',
            name='unfollow',
            field=models.BooleanField(default=False, verbose_name='屏蔽'),
        ),
        migrations.AlterField(
            model_name='order',
            name='bento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Bento', verbose_name='飯盒'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='創建時間'),
        ),
        migrations.AlterField(
            model_name='order',
            name='distribution_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.DistributionPlace', verbose_name='發放地點'),
        ),
        migrations.AlterField(
            model_name='order',
            name='line_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.LineProfile', verbose_name='Line名稱'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.IntegerField(verbose_name='數量'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='LocationaLimitation',
        ),
        migrations.AddField(
            model_name='arealimitation',
            name='bento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Bento', verbose_name='飯盒'),
        ),
        migrations.AddField(
            model_name='distributionplace',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.Area', verbose_name='地區'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.Area', verbose_name='地區'),
            preserve_default=False,
        ),
    ]
