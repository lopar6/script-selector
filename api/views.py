import codecs
from urllib import response
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

from api.models import Script
from api.serializers import ScriptSerializer

class ScriptViewSet():
    def selected_script(self, *args, **kwargs):
        script: Script = Script.objects.filter(chosen_one=True).first()
        if script is None:
            print('no script selected')
            # TODO return script that dispayes error
            return HttpResponse("No script selected :)")
        # TODO move this to save?
        serializer = ScriptSerializer(script)
        file = open(settings.MEDIA_ROOT + serializer.data['bat_file'], "r")
        file_text = file.read()
        file.close()
        bytesFile = file_text.encode('ascii')
        base64File = codecs.encode(bytesFile, 'base64')

        return HttpResponse(base64File, content_type="text/plain")

def turtle_pants(request):
    file = ''
    context ={
        "file": file,
    }
    return render(request, "home.html", context)

# # import Http Response from django

# # create a function
# def geeks_view(request):
#     # create a dictionary to pass
#     # data to the template
#     context ={
#         "data":"Gfg is the best",
#         "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     }
#     # return response with template and context
#     return render(request, "geeks.html", context)
