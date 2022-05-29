import codecs
from django.http import HttpResponse


from api.models import Script
from api.serializers import ScriptSerializer

class ScriptViewSet():
    def selected_script(self, *args, **kwargs):
        script: Script = Script.objects.filter(chosen_one=True).first()
        if script is None:
            print('no script selected')
            return

        # TODO move this to save?
        serializer = ScriptSerializer(script)
        bytesFile = serializer.data['bat_file'].encode('ascii')
        base64File = codecs.encode(bytesFile, 'base64')

        return HttpResponse(base64File, content_type="text/plain")
