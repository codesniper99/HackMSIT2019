from django.contrib import admin
from core.models import ClassificationModel,RegressionModel,Dataset


#registered
admin.site.register(ClassificationModel)

admin.site.register(RegressionModel)

admin.site.register(Dataset)
