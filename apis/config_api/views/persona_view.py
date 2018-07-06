"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso persona.
"""
import logging

from apps.config.models.persona import Persona
from rest_framework import viewsets, serializers
from rest_framework.validators import UniqueValidator

log = logging.getLogger(__name__)


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id',
                  'nombres',
                  'apellido_paterno',
                  'apellido_materno',
                  'genero',
                  'fecha_nacimiento',
                  'direccion',
                  'telefono',
                  'celular',
                  'num_doc',
                  'carnet_extrangeria',
                  'foto',

                  'fecha_creacion', 'fecha_actualizacion')

        extra_kwargs = {
                'num_doc': {'validators': []},
            }

        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

    def validate_num_doc(self, value):
        if self.context['request']._request.method == 'POST':
            unique = UniqueValidator(
                self.Meta.model.objects.all(),
                message='Persona with this Dni already exists.',
            )
            unique.set_context(self.fields['num_doc'])
            unique(value)
        return value

class PersonaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving personas.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    default_fields = 'codename'
    fields = 'nombres,'

    def search(self, fields, term):
        queryComplex = Q()
        for field in fields.split(','):
            dynamic_field = field + '__icontains'
            queryComplex = queryComplex | Q(**{dynamic_field: term})
        return queryComplex

    def get_queryset(self):
        search = self.request.query_params.get('query', None)
        fields = self.request.query_params.get('fields', None)

        if (search and fields) is not None:
            queryset = queryset.filter(self.search(fields, search))

        # text_search = self.request.text_search
        # return Persona.objects.filter(purchaser=text_search)