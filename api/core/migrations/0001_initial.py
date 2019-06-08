# Generated by Django 2.2.2 on 2019-06-08 09:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('title', models.CharField(choices=[('ADMIN', 'Admin'), ('DOCTOR', 'Doctor'), ('SUPERUSER', 'SuperUSer')], max_length=9)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('level', models.CharField(choices=[('TIER 1', 'Level 1'), ('TIER 2', 'Level 2'), ('TIER 3', 'Level 3'), ('TIER 4', 'Level 4')], max_length=6)),
                ('administrator', models.ForeignKey(limit_choices_to={'title': 'ADMIN'}, on_delete=django.db.models.deletion.PROTECT, related_name='administrator', to=settings.AUTH_USER_MODEL)),
                ('doctors', models.ForeignKey(limit_choices_to={'title': 'DOCTOR'}, on_delete=django.db.models.deletion.PROTECT, related_name='practitioners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('identification', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('marital_status', models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married'), ('DIVORCED', 'Divorced'), ('SEPARATED', 'Separated')], max_length=10)),
                ('county', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=5)),
                ('photo', models.ImageField(blank=True, upload_to='profile_photos')),
                ('bio', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDiagnoses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='eye_photos/')),
                ('model_diagnosis', models.CharField(choices=[('DME', 'Diabetic macular edema'), ('AMD', 'Age-related macular degeneration'), ('NORMAL', 'Normal')], max_length=7, null=True)),
                ('is_true', models.BooleanField(default=False)),
                ('doctors_comment', models.CharField(max_length=255, null=True)),
                ('doctor', models.ForeignKey(limit_choices_to={'title': 'DOCTOR'}, on_delete=django.db.models.deletion.PROTECT, related_name='physician', to=settings.AUTH_USER_MODEL)),
                ('hospital_visited', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hospital', to='core.Hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appointments', to='core.Patient')),
            ],
        ),
    ]
