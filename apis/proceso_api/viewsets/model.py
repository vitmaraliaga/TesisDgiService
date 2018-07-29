from rest_framework import mixins, views
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
# from django.db.models import get_model
from django.apps import apps
from rest_framework import serializers
# from rest_framework.core import serializers

import json

class Select(object):
    id = None
    label = None
    def __init__(self, id=None, label=None):
        self.id = id
        self.label = label
    def __str__(self):
        return '%s %s' % (self.id, self.label)
        # return self.label

class SelectSerializers(serializers.Serializer):
    id = serializers.UUIDField()
    label = serializers.CharField()

class Model(object):
    model = None
    queryset = None

    def __init__(self, *args, **kwargs):
        # Inicializa cualquier variable que necesites a partir de la entrada que obtienes
        data = args[0]
        appname_and_modelname = []
        for field in data.split('.'):
            appname_and_modelname.append(field)
        self.model = apps.get_model(*appname_and_modelname)
        self.get_queryset()
        pass
    def get_queryset(self):
        self.queryset = self.model.objects.all()
    
    def get_data_label_array(self, data_label=None):
        qlabel = []
        for label in data_label.split('.'):
            qlabel.append(label)
        return qlabel
    def get_query_label(self, q=None, labels=None):
        query = []
        for label in labels:
            query.append(q[label])
        query = ' '.join(str(x) for x in query)
        return query
    def orderModels(self, data_pk=None, data_label=None):
        # Haz algunos cálculos aquí
        # devuelve una tupla ((1,2,3,), (4,5,6,))
        array_labels = self.get_data_label_array(data_label)
        # myQuery =self.queryset.values(data_pk,*array_labels)
        myQuery =self.queryset.values(data_pk,*array_labels)
        # .include(alias__exact='')
        list_options=[]
        for q in myQuery:
            query_label= self.get_query_label(q, array_labels)
            option = Select(id=q[data_pk], label=query_label)
            list_options.append(option)
        seralizer_o = SelectSerializers(list_options, many=True)
        return seralizer_o.data

class ModelRestView(views.APIView):
# class Model(mixins.ListModelMixin, GenericAPIView):

    def get(self, request, *args, **kwargs):
        data_model = request.GET.get('data_model_name', None)
        data_pk = request.GET.get('data_model_pk', None)
        data_label = request.GET.get('data_model_label', None)
        model = Model(data_model)
        result = model.orderModels(data_pk, data_label)
        response = Response(result, status=status.HTTP_200_OK)

        return response

