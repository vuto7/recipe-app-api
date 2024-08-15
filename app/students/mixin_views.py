from rest_framework import mixins, viewsets, generics
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
#from django_filters.rest_framework import 

class StudentSetPagination(PageNumberPagination):
    page_size=4

#MODEL VIEWSETS
#class StudentViewSet(viewsets.ReadOnlyModelViewSet):
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'score']


#APIvIEWS 
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentDetail(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

"""
#
# MIXINS
#
class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

        
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)   

    def put(self, request, pk):
        return self.update(request, pk)   

    def delete(self, request, pk):
        return self.delete(request, pk)    

"""