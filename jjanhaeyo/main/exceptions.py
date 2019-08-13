from django.utils.translation import ugettext_lazy as _
from rest_framework.views import exception_handler as rest_exc_handler
from rest_framework.response import Response


def exception_handler(exc, context):
    response = rest_exc_handler(exc, context)
    if response is None:
        return None

    if 'detail' in response.data:
        message = response.data['detail']
    else:
        if response.status_code == '400':
            message = _('Bad Request')
        elif response.status_code == '404':
            message = _('Not Found')
        elif response.status_code == '500':
            message = _('Internal Server Error')
        else:
            message = str(response.status_code)

    return Response({
        'code': response.status_code,
        'message': message,
        'detail': {k: v for (k, v) in response.data.items() if k not in ['detail']},
    }, status=response.status_code)
