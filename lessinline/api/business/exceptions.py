from rest_framework.exceptions import APIException


class BusinessNotFound(APIException):
    status_code = 404
    default_detail = 'Business ID not found'


class InvalidPermission(APIException):
    status_code = 401
    default_detail = 'Invalid permissions'


class ServiceNotFound(APIException):
    status_code = 404
    default_detail = 'Service ID not found'
