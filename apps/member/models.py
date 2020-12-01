from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from apps.event.models import Event
from apps.location.models import Address
from django.urls import reverse

User = get_user_model()


class Member(models.Model):

    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    MARITAL_STATUS = [
        ('m', 'Married'),
        ('d', 'Divorce'),
        ('w', 'Widowed'),
        ('s', 'Single'),
    ]

    title = models.CharField(blank=True, max_length=20)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateField()
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.PROTECT)
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=1)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True, max_length=254, blank=True)
    photo = models.ImageField(upload_to='member/', blank=True)
    note = models.TextField(blank=True)
    occupation = models.CharField(blank=True, max_length=255)
    workplace = models.CharField(blank=True, max_length=255)
    school = models.CharField(max_length=120, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Member's"

    def __str__(self):
        return self.last_name + " " + self.middle_name + " " + self.first_name
    
    
    @property
    def full_name(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name


    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"pk": self.pk})


class Visitor(models.Model):

    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    MARITAL_STATUS = [
        ('m', 'Married'),
        ('d', 'Divorce'),
        ('w', 'Widowed'),
        ('s', 'Single'),
    ]

    STATUS = [
        ('f', 'First Time Visitor'),
        ('r', 'Returning Visitor'),
    ]

    REASON = [
        ('c', 'Would like to know more about the Church'),
        ('m', 'Would like to be a member'),
        ('v', 'Would like a Visit'),
        ('a', 'New to area'),
        ('b', 'Would like to know more being a Christian'),
    ]


    title = models.CharField(blank=True, max_length=20)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True, max_length=254, blank=True)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.PROTECT)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=1)
    date = models.DateField()
    occupation = models.CharField(blank=True, max_length=255)
    workplace = models.CharField(blank=True, max_length=255)
    school = models.CharField(max_length=120, blank=True)
    guest_of = models.ForeignKey(Member, blank=True, null=True, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS, max_length=1)
    reason = models.CharField(choices=REASON, max_length=1)
    note = models.TextField(blank=True)
    received_by = models.OneToOneField(User, on_delete=models.PROTECT)
    

    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitor's"

    def __str__(self):
        return self.last_name + " " + self.middle_name + " " + self.first_name



    @property
    def full_name(self):
        return self.last_name + " " + self.middle_name + " " + self.first_name

    def get_absolute_url(self):
        return reverse("visitor_detail", kwargs={"pk": self.pk})


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    men = models.PositiveIntegerField()
    women = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    visitors = models.PositiveIntegerField()
    date = models.DateField()
    note = models.TextField(blank=True)

    @property
    def total(self):
        ttl = self.men + self.women + self.children + self.visitors
        return ttl

    def __str__(self):
        return self.event.name + ": " + str(self.total)
    