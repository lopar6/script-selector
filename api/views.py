import codecs
from django.http import HttpResponse
from django.conf import settings

from api.models import Script
from api.serializers import ScriptSerializer

class ScriptViewSet():
    def selected_script(self, *args, **kwargs):
        script: Script = Script.objects.filter(chosen_one=True).first()
        if script is None:
            print('no script selected')
            # TODO return script that dispayes error
            return
        # TODO move this to save?
        serializer = ScriptSerializer(script)
        file = open(settings.MEDIA_ROOT + serializer.data['bat_file'], "r")
        file_text = file.read()
        file.close()
        bytesFile = file_text.encode('ascii')
        base64File = codecs.encode(bytesFile, 'base64')

        return HttpResponse(base64File, content_type="text/plain")
