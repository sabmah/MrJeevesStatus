from django.db import models

class ROSActionType(models.Model):
    action_type = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.action_type
    
class ROSActionRegister(models.Model):
    action_type = models.ForeignKey(ROSActionType),
    name = models.CharField(max_length=128, unique=True),
    server_name = models.CharField(max_length=128, unique=True),
    client_name = models.CharField(max_length=128, unique=True),
    publisher_name = models.CharField(max_length=128, unique=True),
    subsriber_name = models.CharField(max_length=128, unique=True),
    
    def __unicode__(self):
        return self.name
    
class ROSActionOutput(models.Model):
    ros_action = models.ForeignKey(ROSActionRegister),
    data = models.TextField(), #Stores Raw JSON Data
    
    def __unicode__(self):
        return self.data
    
    

