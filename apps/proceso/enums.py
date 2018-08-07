"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso

Description: Enums de la aplicación
"""
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


NORMAL = 'NORMAL'
TEMPORIZADOR = 'TEMPORIZADOR'
TIPO_REQUISITO_CHOICES = (
    (NORMAL, capfirst(_('requisito normal'))),
    (TEMPORIZADOR, capfirst(_('requisito temporizador'))),
)


# inputs
INPUT = 'input'
TEXTAREA = 'textarea'
PASSWORD = "password"
NUMBER = "number"
EMAIL = "email"
CHECKBOX = 'checkbox'
RADIOBUTTON = 'radiobutton'
SELECT = 'select'

BUTTON = "button"
SLIDER = "slider"
FILEINPUT = "fileinput"
SLIDETOGGLE = "slidetoggle"

DATE = "date"
DATETIMELOCAL = "datetimelocal"
MONTH = "month"
TIME = "time"
URL = "url"

VALIDADOR = "validador"
GENERAR_DOCUMENTOS = "generar_documentos"

TIPO_CAMPO_CHOICES = (
    (INPUT, capfirst(_('input'))),
    (TEXTAREA, capfirst(_('textarea'))),
    (PASSWORD, capfirst(_('password'))),
    (NUMBER, capfirst(_('number'))),
    (EMAIL, capfirst(_('email'))),
    (CHECKBOX, capfirst(_('checkbox'))),
    (RADIOBUTTON, capfirst(_('radio-button'))),
    (SELECT, capfirst(_('select'))),

    (BUTTON, capfirst(_('button'))),

    (SLIDER, capfirst(_('slider'))),
    (FILEINPUT, capfirst(_('file-input'))),
    (SLIDETOGGLE, capfirst(_('slide-toggle'))),
    (DATE, capfirst(_('date'))),
    (DATETIMELOCAL, capfirst(_('date-time-local'))),
    (MONTH, capfirst(_('month'))),
    (TIME, capfirst(_('time'))),
    (URL, capfirst(_('url'))),

    (VALIDADOR, capfirst(_('validador'))),
    (GENERAR_DOCUMENTOS, capfirst(_('generar-documentos'))),
)

GRUPAL = "G"
ROL = "R"
PERSONAL = "P"

TIPO_VALIDADOR_CHOICES = (
    (GRUPAL, capfirst(_('grupal'))),
    (ROL, capfirst(_('rol'))),
    (PERSONAL, capfirst(_('personal'))),
)