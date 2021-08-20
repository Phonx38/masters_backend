from django.db import models
from django.core.validators import RegexValidator

# Create your models here.



class GstInfo(models.Model):
    status_choices = (("ACTIVE", "Active"), ("INACTIVE", "Inactive"))

    tax_payer_choices = (
        ("REGULAR", "Regular"),
        ("COMPANY", "Company"),
        ("FIRM", "Firm"),
    )

    bussiness_choices = (
        ("PRIVATE LIMITED COMPANY", "Private Limited Company"),
        ("SOLE PROPERITERSHIP", "Sole Properitership"),
        ("LLC", "Llc"),
    )

    gstin_id = models.CharField(max_length=15, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    addrs_line_1 = models.CharField(max_length=150, blank=True, null=True)
    addrs_line_2 = models.CharField(max_length=150, blank=True, null=True)
    addrs_line_3 = models.CharField(max_length=150, blank=True, null=True)
    pincode = models.CharField(
        max_length=6, validators=[RegexValidator(r"^\d{1,6}$")], blank=True, null=True
    )

    registration_date = models.DateField(("Date_registration"), auto_now=False,)
    cancellation_date = models.DateField(
        ("Date_Cancellation"), auto_now=False, blank=True, null=True
    )
    state_jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    center_jurisdiction = models.CharField(max_length=100, blank=True, null=True)
    status_type = models.CharField(
        choices=status_choices, max_length=50, default="INACTIVE"
    )
    taxpayer_type = models.CharField(
        choices=tax_payer_choices, max_length=50, default="REGULAR"
    )
    bussiness_type = models.CharField(
        choices=bussiness_choices, max_length=100, default="LLC"
    )

    def __str__(self):
        return self.gstin_id

    def save(self, *args, **kwargs):
        self.gstin_id = self.gstin_id.upper()
        for field_name in ["name", "state_jurisdiction", "center_jurisdiction"]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(GstInfo, self).save(*args, **kwargs)  # Call the real save() method
