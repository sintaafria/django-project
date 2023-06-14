from django.db import models
from django.contrib.auth.models import AbstractUser

class z_users(AbstractUser):
    password = models.CharField(max_length=255, null=False, db_column='upassword')
    username=None
    uname = models.CharField(max_length=255, null=False, unique=True)
    # upassword = models.CharField(max_length=255, null=False)
    isldap = models.SmallIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    fullname = models.CharField(max_length=255, blank=True, null=True, default='',unique=False)
    status = models.SmallIntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    descr = models.CharField(max_length=255, blank=True, null=True)
    work_unit = models.CharField(max_length=200, blank=True, null=True)
    person_id = models.IntegerField(null=True)
    current_loc = models.IntegerField(null=True)
    last_update = models.DateTimeField(blank=True, null=True, default=None)
    ubis_id = models.IntegerField(null=True)
    sub_ubis_id = models.IntegerField(null=True)
    jabatan = models.CharField(max_length=200, blank=True, null=True)
    fixed_phone = models.CharField(max_length=30, blank=True, null=True)
    mobile_phone = models.CharField(max_length=30, blank=True, null=True)
    redirect_url = models.CharField(max_length=100, blank=True, null=True)
    main_role = models.CharField(max_length=11, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    picture = models.CharField(max_length=225, blank=True, null=True)
    app = models.CharField(max_length=20, blank=True, null=True)
    is_telkom = models.SmallIntegerField(blank=True, null=True)
    employment_category = models.CharField(max_length=100, blank=True, null=True)
    position_name = models.CharField(max_length=200, blank=True, null=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    umur = models.IntegerField(null=True)
    masa_bakti = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    grade_name = models.CharField(max_length=10, blank=True, null=True)
    loc_id = models.SmallIntegerField(blank=True, null=True)
    pendidikan = models.SmallIntegerField(blank=True, null=True)
    lokasi_tip = models.CharField(max_length=10, blank=True, null=True)
    status_tip = models.CharField(max_length=30, blank=True, null=True)
    company_id = models.IntegerField(null=True)
    kode_unit = models.IntegerField(null=True)
    answare_date = models.DateTimeField(blank=True, null=True, default=None)
    active = models.SmallIntegerField(blank=True, null=True)
    is_new_account = models.SmallIntegerField(blank=True, null=True)
    is_blocked = models.SmallIntegerField(blank=True, null=True)
    is_sso = models.SmallIntegerField(blank=True, null=True)
    sid = models.CharField(max_length=100, blank=True, null=True)
    USERNAME_FIELD = "uname"
    REQUIRED_FIELDS = ["upassword"]

    class Meta:
        db_table = 'z_users' # define your custom name