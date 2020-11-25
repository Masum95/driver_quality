from rest_framework.exceptions import APIException


class UserUnavilableException(APIException):
    status_code = 404
    default_detail = "Driver doesn't exist"
    default_code = 'driver_unavailable'