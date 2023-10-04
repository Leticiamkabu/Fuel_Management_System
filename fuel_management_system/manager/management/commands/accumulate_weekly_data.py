# your_app/management/commands/accumulate_weekly_data.py
from django.core.management.base import BaseCommand
from datetime import timedelta, date
from .models import Daily_statistics  # Import your Daily_statistics model

class Command(BaseCommand):
    help = 'Accumulate data weekly'

    def handle(self, *args, **options):
        min_date = Daily_statistics.objects.aggregate(min_date=models.Min('date'))['min_date']

        # Set the start date for the first week
        start_date = min_date

        # Define the start and end dates for a week
        # start_date = date(2023, 1, 1)  # Replace with the start date of your data
        # end_date = start_date + timedelta(days=6)

        # while end_date <= date.today():
        #     # Query the Daily_statistics model for data within the week
        #     week_data = Daily_statistics.objects.filter(date__range=[start_date, end_date])

        #     # Calculate and record the sum or perform other calculations
        #     total_diesel_dipping = week_data.aggregate(total_diesel_dipping=Sum('diesel_dipping'))['total_diesel_dipping']
        #     total_super_dipping = week_data.aggregate(total_super_dipping=Sum('super_dipping'))['total_super_dipping']

        #     # Perform your calculations with the accumulated data as needed
        #     # ...

        #     # Update the start and end dates for the next week
        #     start_date += timedelta(days=7)
        #     end_date += timedelta(days=7)



        while start_date <= date.today():
            # Calculate the end date as the next Friday
            end_date = start_date + timedelta(days=(4 - start_date.weekday()) % 7)

            # Query the Daily_statistics model for data within the week
            week_data = Daily_statistics.objects.filter(date__range=[start_date, end_date])

            # Calculate and record the sum or perform other calculations
            total_diesel_dipping = week_data.aggregate(total_diesel_dipping= Sum('diesel_dipping'))['total_diesel_dipping']
            total_super_dipping = week_data.aggregate(total_super_dipping= Sum('super_dipping'))['total_super_dipping']
            total_diesel_litter_sold = week_data.aggregate(total_diesel_litter_sold= Sum('diesel_litters_sold'))['total_diesel_litter_sold']
            total_super_litter_sold = week_data.aggregate(total_diesel_litter_sold= Sum('super_litters_sold'))['total_super_litter_sold']
            total_diesel_amount_sold = week_data.aggregate(total_diesel_amount_sold= Sum('diesel_amount_sold'))['total_diesel_amount_sold']
            total_super_amount_sold = week_data.aggregate(total_super_amount_sold= Sum('super_amount_sold'))['total_super_amount_sold']
            total_diesel_variance = week_data.aggregate(total_diesel_variance= Sum('diesel_variance'))['total_diesel_variance']
            total_super_variance = week_data.aggregate(total_super_variance= Sum('super_variance'))['total_super_variance']

            
            # Perform your calculations with the accumulated data as needed
            # ...

            # Update the start date for the next week
            start_date = end_date + timedelta(days=1)


            # Update the Daily_statistics model with the calculated data
        weekly_statistics = Weekly_statistics.objects.create(
            start_date=start_date,
            end_date=end_date,
            diesel_dipping = total_diesel_dipping,
            super_dipping = total_super_dipping,
            diesel_litter_sold = total_diesel_litter_sold
            super_litter_sold = total_super_litter_sold
            diesel_amount_sold = total_diesel_amount_sold
            super_amount_sold = total_super_amount_sold
            diesel_variance = total_diesel_variance
            super_variance = total_super_variance

        )
        weekly_statistics.save()
