from django.core.validators import MinValueValidator, RegexValidator
from django.db import models


class NonNegativeValidator(MinValueValidator):
    def __init__(self):
        super().__init__(limit_value=0)


class PositiveValidator(MinValueValidator):
    def __init__(self):
        super().__init__(limit_value=1)


class HexDigestValidator(RegexValidator):
    regex = r'^[0-9a-f]+$'


class Migration(models.Model):
    path = models.CharField(max_length=256)

    checksum = models.CharField(
        max_length=40,
        validators=[HexDigestValidator()]
    )

    comment = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )

    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    execute_timestamp = models.DateTimeField(blank=True, null=True)
    execute_status = models.IntegerField(
        validators=[NonNegativeValidator()]
    )

    class Meta:
        db_table = 'sqlpaths_migrations'
        unique_together = ('path', 'checksum')

    def __repr__(self):
        return 'Migration(path=%r, checksum=%r)' % (self.path, self.checksum)
