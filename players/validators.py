from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_draft_year(value):
    current_year = date.today().year
    if value > current_year:
        raise ValidationError(
            _("It's not %(value)s yet"),
            params={"value": value},
        )
