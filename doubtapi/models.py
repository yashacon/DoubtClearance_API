from django.db import models

import os

def get_upload_path(instance, filename):
    fileName, fileExtension = os.path.splitext(filename)
    return os.path.join(
      "Ques_%s" % instance.Ques_ID,"Ques_{0}.{1}" .format(instance.Ques_ID,fileExtension) )


class Doubts(models.Model):
    Student=models.CharField(max_length=20)
    Ques_ID=models.CharField(max_length=6)
    Q_Type=models.CharField(max_length=20)
    Description=models.CharField(max_length=200)
    Image=models.ImageField(upload_to=get_upload_path,blank='True')
    