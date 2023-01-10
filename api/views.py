from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from api.clases import Monitor
from api.monitor import dar_uso_cpu, dar_uso_disco, dar_uso_memoria
from api.serializers import monitorSerializer


@api_view(['GET'])
def listar_datos(request):
    if request.method == "GET":
        cpu = dar_uso_cpu()
        memoria = dar_uso_memoria()
        disco = dar_uso_disco()
        datos_raw = Monitor(cpu,memoria,disco)
        serialisador = monitorSerializer(datos_raw)
        datosServer = JSONRenderer().render(serialisador.data)
        return Response(datosServer)
