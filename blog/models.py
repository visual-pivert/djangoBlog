from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Influenceur(AbstractBaseUser):
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    sex_choices = [
        ('M', 'Masculin'),('F', 'Female')
    ]
    sex = models.CharField(max_length=20, choices=sex_choices)
    password = models.CharField(max_length=80)
    email = models.EmailField()

    date_joined = models.DateTimeField("date joined", auto_now=True)
    last_login = models.DateField("last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = is_staff = is_superuser = False,

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", )



class Blog(models.Model):
    title =  models.CharField(max_length=100, blank=False)
    img = models.ImageField(upload_to='media/', default="the_def_img.jpg", height_field=None, width_field=None, max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    like = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=False)


    def get_nb_likes(self) -> int:
        self.like = Commentator.objects.filter(person_id=self.id, like=True)
        return len(self.like)

    def __str__(self):
        return f'Blog {self.id} from {self.title}'


class Commentator(models.Model):
    person = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)
    # """  individual_name = models.CharField(max_length=10, default='Anonymous', blank=True, null=False)"""
    user = models.OneToOneField(to=Influenceur, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)
    commentary = models.TextField(default='')
    objects = models.Manager

    def __str__(self):
        return f'{self.individual_name}-{self.id}'
