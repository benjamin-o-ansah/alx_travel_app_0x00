from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "name": "Luxury Beach Villa",
                "description": "Oceanfront paradise with private pool.",
                "location": "Malindi, Kenya",
                "price_per_night": 250.00
            },
            {
                "name": "Cozy Mountain Cabin",
                "description": "Perfect for winter getaways.",
                "location": "Nanyuki, Kenya",
                "price_per_night": 120.00
            },
            {
                "name": "Modern City Apartment",
                "description": "Heart of the city with great views.",
                "location": "Nairobi, Kenya",
                "price_per_night": 85.00
            }
        ]

        for item in sample_data:
            Listing.objects.create(**item)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {item["name"]}'))