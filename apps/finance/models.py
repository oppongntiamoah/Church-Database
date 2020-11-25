from django.db import models
from apps.event.models import Event
from apps.member.models import Member, Visitor
from phonenumber_field.modelfields import PhoneNumberField
from apps.location.models import Address



class Offertory(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()

    class Meta:
        verbose_name = "Offertory"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("fffertory_detail", kwargs={"pk": self.pk})



class Giving(models.Model):

    member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, blank=True, null=True, on_delete=models.PROTECT)
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



class Contribution_Type(models.Model):

    name = models.CharField(unique=True, max_length=250)
    is_active = models.BooleanField(default=False)
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

    member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, blank=True, null=True, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "contribution"
        verbose_name_plural = "contribution's"

    def __str__(self):
        return self.member.full_name or self.visitor.full_name

    def get_absolute_url(self):
        return reverse("contribution_detail", kwargs={"pk": self.pk})


class Donation(models.Model):

    title = models.CharField(blank=True, max_length=20)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True, max_length=254, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.PROTECT)
    occupation = models.CharField(blank=True, max_length=255)
    workplace = models.CharField(blank=True, max_length=255)
    school = models.CharField(max_length=120, blank=True)
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donation's"

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse("donation_detail", kwargs={"pk": self.pk})




class Tithe(models.Model):

    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_received = models.DateField()
    note = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tithe"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.member.full_name

