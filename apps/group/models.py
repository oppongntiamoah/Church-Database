from django.db import models
from django.urls import reverse_lazy
from apps.member.models import Member


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_description = models.CharField(blank=True, max_length=255)
    group_members = models.ManyToManyField(Member, through='GroupMember')

    def __str__(self):
        return self.group_name

    # def get_absolute_url(self):
    #     return reverse_lazy('groups:group_detail', kwargs={
    #         'pk': self.id,
    #         })

class MemRole(models.Model):

    mem_role = models.CharField(max_length=35)
    
    class Meta:
        verbose_name_plural = 'Membership Roles'
    
    def __str__(self):
        return self.mem_role

class GroupMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    leader = models.BooleanField(default=False)
    member_role = models.ForeignKey(MemRole, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s: %s (%s)' % (self.group, self.member, self.member_role)