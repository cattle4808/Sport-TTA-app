from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class DayFilterAdmin(admin.SimpleListFilter):
    title = _('Day Filter')
    parameter_name = 'day_filter'

    def lookups(self, request, model_admin):
        return [
            ('all', _('All')),
            ('today_and_future', _('Today and Future')),
            ('past', _('Past Sessions')),
            ('last_7_days', _('Last 7 Days')),
        ]

    def queryset(self, request, queryset):
        today = timezone.now().date()

        if self.value() == 'today_and_future' or self.value() is None:
            return queryset.filter(day__gte=today)
        elif self.value() == 'past':
            return queryset.filter(day__lt=today)
        elif self.value() == 'last_7_days':
            return queryset.filter(day__gte=today - timezone.timedelta(days=7))
        return queryset

