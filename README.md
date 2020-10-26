# django-clicoh

- Se implementaron los siguientes models con atributos:

    - Product:  
        - id PK [char field]
        - name [char field]
        - price [float field] 

    - Order:  
        - id PK [char field]
        - date_time [datetime field]

    - OrderDetail:  
        - order FK [Order]
        - cuantity [int field]
        - price [float field]
        - product FK [Product]

- Se implementaron serializers usando **ModelSerializer** para la implementación de la api, los cuales se implementaron en [serializers.py ](https://github.com/lucasblanco31/django-clicoh/blob/main/clicoh/mysite/myapi/serializers.py).

- Se implemento **ModelViewSet** para las vistas en [views.py ](https://github.com/lucasblanco31/django-clicoh/blob/main/clicoh/mysite/myapi/views.py), y se definieron las siguientes funciones para el manejo de datos en los models y su modificación:

    - list
    - retrieve
    - create
    - update
    - delete 

- Además se implementó autenticación por tokens a partir de *TokenAuthentication* y *IsAuthenticated* de rest_framework, las cuales se dejaro comentadas para seguir trabajando.