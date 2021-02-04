# Generated by Django 3.1.6 on 2021-02-04 19:17

import auction.models.bases
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BidBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auction_bidbasket_related', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Bid basket',
                'verbose_name_plural': 'Bid baskets',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, verbose_name='Lot name')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_biddable', models.BooleanField(default=False, verbose_name='Is biddable?')),
                ('object_id', models.PositiveIntegerField(verbose_name='Object ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_lot_lots', to='contenttypes.contenttype', verbose_name='Content type')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_auction.lot_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Auction lot',
                'verbose_name_plural': 'Auction lots',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BidItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.PositiveIntegerField(verbose_name='Lot ID')),
                ('amount', auction.models.bases.CurrencyField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount')),
                ('bid_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_biditem_related', to='auction.bidbasket', verbose_name='Bid basket')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_biditem_related', to='contenttypes.contenttype', verbose_name='Content type')),
            ],
            options={
                'verbose_name': 'Bid item',
                'verbose_name_plural': 'Bid items',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Auction name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='End date')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('total_bids', models.IntegerField(default=0, verbose_name='Total bids')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_auction.auction_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Auction',
                'verbose_name_plural': 'Auctions',
                'abstract': False,
            },
        ),
    ]
