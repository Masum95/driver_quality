from drf_yasg import openapi

def get_query_param(name, description, type):
    """ Gives a query parameter with given name, description and type """
    return openapi.Parameter(
        name=name,
        in_=openapi.IN_QUERY,
        description=description,
        type=type
    )


def get_authorization_param(required):
    return openapi.Parameter(
        name='Authorization',
        description='Bearer Token',
        required=required,
        type=openapi.TYPE_STRING,
        in_=openapi.IN_HEADER
    )


SUPPLY_ID_QUERY_PARAMETER = get_query_param('supply_id', 'Driver Id (optional)', openapi.TYPE_STRING)
HOW_MANY_LAST_QUERY_PARAMETER = get_query_param('how_many_last', 'How many last orders(optional)', openapi.TYPE_STRING)
