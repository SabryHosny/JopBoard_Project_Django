from .serializers import JobSerializer
from .models import Jop
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


# Function based api_view
@api_view(['GET'])
def job_list_api(request):
    all_jobs = Jop.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data': data})


# Function based api_view
@api_view(['GET'])
def job_detail_api(request, id):
    job = Jop.objects.get(id=id)
    data = JobSerializer(job).data
    return Response({'data': data})


# Class based api_view
class JopListApi(generics.ListAPIView):
    queryset = Jop.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jop.objects.all()
    lookup_field = 'id'
    serializer_class = JobSerializer
