from django.db import models
from apps.event.models import Event


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/member/user_<id>/<filename>
    return 'member/user_{0}/{1}'.format(instance.user.id, filename)



class Member(models.Model):

    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
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
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=1)
    email = models.EmailField(unique=True, max_length=254, blank=True)
    date_started = models.DateField()
    photo = models.ImageField(upload_to=user_directory_path)
    note = models.TextField()
    occupation = models.CharField(max_length=80, blank=True)
    school = models.CharField(max_length=120, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Member's"

    def __str__(self):
        return self.last_name + " " + self.middle_name + " " + self.first_name

    # def get_absolute_url(self):
    #     return reverse("member_detail", kwargs={"pk": self.pk})


class Visitor(models.Model):

    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
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
    email = models.EmailField(unique=True, max_length=254, blank=True)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=1)
    date = models.DateField()
    photo = models.ImageField(upload_to=user_directory_path)
    occupation = models.CharField(max_length=80, blank=True)
    school = models.CharField(max_length=120, blank=True)
    guest_of = models.ForeignKey(Member, blank=True, null=True, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS, max_length=1)
    reason = models.CharField(choices=REASON, max_length=1)
    note = models.TextField()

    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitor's"

    def __str__(self):
        return self.last_name + " " + self.middle_name + " " + self.first_name

    # def get_absolute_url(self):
    #     return reverse("member_detail", kwargs={"pk": self.pk})
