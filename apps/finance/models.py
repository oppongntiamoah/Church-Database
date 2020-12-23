from django.db import models
from apps.event.models import Event
from apps.member.models import Member, Visitor
from phonenumber_field.modelfields import PhoneNumberField
from apps.location.models import Address
import calendar
from apps.newsletter.send_sms import sendSMS


class Offertory(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()

    class Meta:
        verbose_name = "Offertory"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.event.name + ": " + str(self.date_received)

    def get_absolute_url(self):
        return reverse("offertory_detail", kwargs={"pk": self.pk})


class Giving(models.Model):

    member = models.ForeignKey(
        Member, blank=True, null=True, on_delete=models.PROTECT)
    # visitor = models.ForeignKey(Visitor, blank=True, null=True, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "Giving"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.member.full_name or self.visitor.full_name

    def get_absolute_url(self):
        return reverse("Giving_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        body = 'Thanks for giving'
        to = str(self.member.phone_number)
        created = self.pk is None
        super().save(*args, **kwargs)

        if created:
            sendSMS(body, to, "Giving") 
        
       


class Contribution_Type(models.Model):

    name = models.CharField(unique=True, max_length=250)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "contribution Type"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contribution_type_detail", kwargs={"pk": self.pk})

      
     


class Contribution(models.Model):

    member = models.ForeignKey(
        Member, blank=True, null=True, on_delete=models.PROTECT)
    contribution_type = models.ForeignKey(
        Contribution_Type, on_delete=models.PROTECT)
    # visitor = models.ForeignKey(Visitor, blank=True, null=True, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "contribution"
        verbose_name_plural = verbose_name + "'s"

    def __str__(self):
        return self.member.full_name + " - " + self.contribution_type.name or self.visitor.full_name + " - " + self.contribution_type.name

    def save(self, *args, **kwargs):
        body = 'Your Contribution to ' + self.contribution_type.name + ', has been received'
        to = str(self.member.phone_number)
        created = self.pk is None
        super().save(*args, **kwargs)

        if created:
            sendSMS(body, to, "Contribution") 
      


class Donation(models.Model):

    title = models.CharField(blank=True, max_length=20)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()
    address = models.ForeignKey(
        Address, blank=True, null=True, on_delete=models.PROTECT)
    occupation = models.CharField(blank=True, max_length=255)
    workplace = models.CharField(blank=True, max_length=255)
    school = models.CharField(max_length=120, blank=True)
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donation"

    def __str__(self):
        return self.last_name

    def save(self, *args, **kwargs):
        body = 'Your Donation to  has been received, thanks.'
        to = str(self.phone_number)

        created = self.pk is None
        super().save(*args, **kwargs)

        if created:
            sendSMS(body, to, "Donations") 



class Tithe(models.Model):

    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    date_received = models.DateField()
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tithe"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['member', 'month'], name='unique member month')
        ]

    def __str__(self):
        return self.member.full_name

    # !sending sms
    def save(self, *args, **kwargs):
        body = 'Your Tithe for ' + str(self.get_month_display() ) + ', ' + str(self.date_received.year) + ' has been received'
        to = str(self.member.phone_number)
        
        created = self.pk is None
        super().save(*args, **kwargs)

        if created:
            sendSMS(body, to, "Tithe") 


class Expense(models.Model):

    EXPENSE_TYPE = (
        ('g', 'General'),
        ('d', 'Donations'),
    )

    amount = models.DecimalField(max_digits=15, decimal_places=2)
    expense_type = models.CharField(choices=EXPENSE_TYPE, max_length=1)
    date = models.DateField()
    note = models.TextField(blank=True)

    def __str__(self):
        return self.expense_type
    