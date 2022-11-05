from django.db import models

#Rider Model
class Rider(models.Model):
    rider_id = models.AutoField(primary_key=True)
    start_location = models.TextField()
    end_location = models.TextField()
    date_and_time =models.TextField()
    travel_medium=models.CharField(max_length=50,choices=(
        ('BUS','Bus'),
        ('CAR','Car'),
        ('TRAIN','Train')
    ))
    assets_quantity = models.IntegerField()


#Requester Model
class Requester(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="")

    def __str__(self):
        return self.name

#Assets Model
class Assets(models.Model):
    start_location = models.TextField(default="")
    end_location = models.TextField(default="")
    date_and_time =models.TextField(default="")
    assets_quantity = models.IntegerField(default="")
    asset_type=models.CharField(max_length=50,choices=(
        ('LAPTOP','Laptop'),
        ('TRAVEL_BAG','Travel Bag'),
        ('PACKAGE','Package')
    ))
    sensitivity =models.CharField(max_length=50,choices=(
        ('HIGHLY_SENSITIVE','Highly Sensitive'),
        ('SENSITIVE','Sensitive'),
        ('NORMAL','Normal')
    ))
    whom_to_deliver = models.TextField(default="")
    requester_id = models.ForeignKey(Requester, on_delete=models.CASCADE,default="")
    # rider_id = models.ForeignKey(Rider, on_delete=models.CASCADE,required = False)


