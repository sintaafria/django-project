from django.db import models
from customuser.models import custom_users

class zpraba_conn(models.Model):
    conn_name = models.CharField(max_length=50, blank=True, null=True)
    conn_params = models.TextField(blank=False, null=False)
    desc = models.CharField(max_length=225, blank=False, null=False, default="")
    is_deactivate = models.SmallIntegerField(blank=True, null=True)
    is_asession = models.SmallIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(custom_users, related_name='%(class)s_created', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified_by = models.ForeignKey(custom_users, related_name='%(class)s_last_modified', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now_add=True)
    adapter = models.CharField(max_length=100, blank=True, null=True)
    ubis_id = models.IntegerField(blank=True, null=True)
    sub_ubis_id = models.IntegerField(blank=True, null=True)
    modified_by = models.ForeignKey(custom_users, related_name='%(class)s_modified', on_delete=models.CASCADE)

    class Meta:
        db_table = 'zpraba_conn'
        ordering = ['conn_name']