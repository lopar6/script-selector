from django.db import models

class ScriptSet(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Script(models.Model):
    name = models.CharField(max_length=100)
    script_set = models.ForeignKey('ScriptSet', on_delete=models.CASCADE, blank=True, null=True)
    chosen_one = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    bat_file = models.FileField()
    # base64_file = models.CharField(max_length=10000)

    def save(self, *args, **kwargs):
        # only allow one script to be chosen
        if self.chosen_one:
            try:
                temp = Script.objects.get(chosen_one=True)
                if self != temp:
                    temp.chosen_one = False
                    temp.save()
            except Script.DoesNotExist:
                pass

        # # encode into base64
        # bytes = self.bat_file.encode('ascii')
        # self.base64_file = base64.b64encode(bytes)
        super(Script, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
