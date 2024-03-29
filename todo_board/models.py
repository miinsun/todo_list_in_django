from django.db import models
from django.db.models import Max

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class ProjectCode(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=4)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_code'


class TodoList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)
    pcode = models.CharField(db_column='PCODE', max_length=4)
    user_id = models.CharField(db_column='USER_ID', max_length=50, blank=True, null=True)
    title = models.CharField(db_column='TITLE', max_length=200, blank=True, null=True)
    content = models.CharField(db_column='CONTENT', max_length=1000, blank=True, null=True)
    is_complete = models.IntegerField(db_column='IS_COMPLETE', blank=True, null=True)
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)

    def todo_save(self):
        self.is_complete = 0
        if TodoList.objects.all().aggregate(Max('priority'))['priority__max'] is None : self.priority = 1
        else : self.priority = int(TodoList.objects.latest('priority').priority) + 1
        self.pcode = 1
        self.user_id = 'guest'
        self.save()

    def todo_update_is_complete(self, complete):
        self.is_complete = complete
        self.save()

    class Meta:
        managed = False
        db_table = 'todo_list'