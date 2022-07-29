from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, related_name='+')
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING, related_name='+')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, related_name='+')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='+')
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, related_name='+')

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='+')
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING, related_name='+')

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Disease(models.Model):
    disease_name = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='disease_name', blank=True, null=True, related_name='+')
    hospital_name = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='hospital_name', blank=True, null=True, related_name='+')
    order = models.CharField(max_length=500)
    disease_checklist = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True, related_name='+')
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='+')

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hospital(models.Model):
    hospital_name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    hospital_address = models.CharField(max_length=100)
    rating = models.FloatField(unique=True, blank=True, null=True)
    all_review = models.ForeignKey('Member', models.DO_NOTHING, db_column='all_review', blank=True, null=True, related_name='+')
    doctors = models.CharField(unique=True, max_length=100, blank=True, null=True)
    time = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    disease_name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital'


class Member(models.Model):
    member_name = models.CharField(max_length=10)
    member_id = models.AutoField(primary_key=True)
    member_pwd = models.CharField(max_length=20)
    mb_address = models.CharField(max_length=50)
    reserved = models.CharField(max_length=50)
    all_review = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Review(models.Model):
    author = models.ForeignKey(Member, models.DO_NOTHING, db_column='author', blank=True, null=True, related_name='+')
    rating = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='rating', blank=True, null=True, related_name='+')
    review_mb = models.CharField(max_length=500)
    doctor = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='doctor', blank=True, null=True, related_name='+')
    cost = models.IntegerField()
    hospital_name = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospital_name', blank=True, null=True, related_name='+')
    disease_review = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='disease_review', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'review'


class SelfDiagnosis(models.Model):
    checklist = models.CharField(max_length=800)
    disease_checklist = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_checklist', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'self_diagnosis'

