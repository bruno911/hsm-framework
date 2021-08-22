from django.core.management.base import BaseCommand

from hms_framework.factory import CustomerFactory, FinancialFactory


class Command(BaseCommand):

    def handle(self, *args, **options):

        customers_with_debts = CustomerFactory().create_model().objects.filter(
            has_debts=True,
            last_has_debts_notified_datetime__isnull=True)

        for customer_with_debts in customers_with_debts:
            debt_collector_service = FinancialFactory().debt_collector_service(customer=customer_with_debts)
            debt_collector_service.collect()