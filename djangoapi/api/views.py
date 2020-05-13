from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .serializers import StatusSerializer
from .models import Status
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from .permissions import LimitedAccess
# http://localhost:8000/api/status/?q=content for searching




class StatusDetailAPIView(mixins.DestroyModelMixin,
                          mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [LimitedAccess]
    # authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_object(self):
    #     kw_id = self.kwargs.get('id')
    #     return Status.objects.get(id=kw_id)










####################NOT USED AS MIXINS ARE USED TO CLUB CERTAIN METHODS#############

class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

# class StatusAPIView(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.UpdateModelMixin,
#                     generics.ListAPIView):
#
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#
#         if query:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get('id', None)
#         queryset = self.get_queryset()
#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id = passed_id)
#             self.check_object_permissions(request, obj)
#         return obj
#
#     def get(self, request, *args, **kwargs):
#         passed_id = request.GET.get('id', None)
#         if passed_id is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request,*args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request,*args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'
