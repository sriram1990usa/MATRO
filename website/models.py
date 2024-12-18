from django.db import models
from website.models import *
from django.contrib.auth.models import User
# Create your models here.

gender=(
('Male','Male'),
('Female','Female'),
)

ms=(
('Unmarried','Unmarried'),
('Widowed','Widowed'),
('Divorced','Divorced'),
)
rel=(
        ('Hindu','Hindu'),
		('Sikh','Sikh'),
		('Muslims','Muslims'),
		('Christians','Christians'),
		('Any','Any'),
	)
    
profile_by=(
        ('Self','Self'),
		('Father','Father'),
		('Mother','Mother'),
		('Brother','Brother'),
		('Sister','Sister'),
        ('Friend','Friend'),
        ('Son','Son'),
        ('Daughter','Daughter'),
	)

 


education=(
    ('CFA (Chatared Financial Analyst)','CFA (Chatared Financial Analyst)'),
    ('CA (Chatared Accountant)','CA Chatared Accountant'),
    ('ICWA','ICWA'),
    ('Integrated P.G.','Integrated P.G.'),
    ('M.Arch.(Architecture)','M.Arch.(Architecture)'),
    ('M.Ed.(Education)','M.Ed.(Education)'),
    
    )

occ=(
        ('Media',' Media '),
		('Agriculture','Agriculture'),
		('Architecture & Design','Architecture & Design'),
		('Artists','Artists'),
		('Animators & Web Designers','Animators & Web Designers'),
		('Banking','Banking'),
		('Insurance & Finacial Services','Insurance & Finacial Services'),
		('Beauty','Beauty'),
		('Fashion Designers','Fashion Designers'),
		('Export & Import','Export & Import'),
		('Govt. Employee','Govt. Employee'),
		('Finance & Accounts','Finance & Accounts'),
		('Healthcare','Healthcare'),
		('Doctors','Doctors'),
		('Engineer','Engineer'),
		('Advocate','Advocate'),
		('Merchant Navy','Merchant Navy'),
		('Pvt. Job','Pvt. Job'),
        ('Business','Business'),

	)	



class contactus(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    E_mail=models.CharField(max_length=100)
    Message=models.TextField(max_length=100)
    
class blogs(models.Model):
    Title=models.CharField(max_length=100)
    Des=models.TextField()
    Date=models.DateField()
    Image=models.ImageField(upload_to='pictures')
    class Meta:
        db_table='blogs'
        
        
class serch(models.Model):
    Gender=models.CharField(max_length=10 , choices=gender )
    Maritial_status=models.CharField(max_length=20 , choices=ms)
    age=models.IntegerField()
    age1=models.IntegerField()
    religion=models.CharField(max_length=30 , choices=rel)
    education=models.CharField(max_length=100 , choices=education)
    occupation=models.CharField(max_length=100, choices=occ)
    class Meta:
        db_table='serch'
        
class Searchs(models.Model):
    Pic1=models.ImageField(upload_to='pictures/',default="")
    Pic2=models.ImageField(upload_to='pictures/',default="")
    name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10,default="")
    Maritial_status=models.CharField(max_length=20, default="")
    age=models.IntegerField()
    religion=models.CharField(max_length=30,default="")
    education=models.CharField(max_length=100,default="")
    occupation=models.CharField(max_length=100,default="")
    lastname=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=50,default="")
    profileby=models.CharField(max_length=50,default="")
    complexion=models.CharField(max_length=30,default="")
    height=models.CharField(max_length=20,default="")
    weight=models.CharField(max_length=20,default="")
    approval=models.CharField(max_length=20,default="non_approval")
    slist=models.CharField(max_length=20,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    
    class Meta:
        db_table='Searchs'

    def __str__(self):
        return self.name
 
class ViewedSearchs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    searchs = models.ForeignKey(Searchs, on_delete=models.CASCADE)
    shortlisted = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        db_table='ViewedSearchs'

    def __str__(self):
        return f"{self.user.username} viewed {self.searchs.name}"
    
'''
class Shortlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    slist=models.ForeignKey(Searchs,on_delete=models.CASCADE,related_name="dd")
    shortlisted = models.BooleanField(default=False)
    
    class Meta:
        db_table='shortlist'

    def __str__(self): 
        return f"{self.user.username} viewed {self.searchs.name}"

'''
class showvideo(models.Model):
    Image=models.CharField(max_length=300)
    video=models.CharField(max_length=300)
    class Meta:
        db_table='showvideo'


        
        
        
class story(models.Model):
    Image=models.ImageField(upload_to='pictures')
    name=models.CharField(max_length=100)
    Wedding_Date =models.DateField()
    Title=models.CharField(max_length=20)
    Des=models.TextField()
    class Meta:
        db_table='story'  