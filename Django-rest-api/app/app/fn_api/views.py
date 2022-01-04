from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


@api_view(['GET','POST','DELETE','PUT'])
def product_list(request):
    if request.method == 'GET':
        if request.query_params.get('id') is not None:
            product = Product.objects.get(product_id=request.query_params.get('id'))
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        id=request.query_params.get('id')
        print(id)
        Product.objects.filter(product_id=id).delete()
        return Response(status=204)

    elif request.method == 'PUT':
        id=request.query_params.get('id')
        product = Product.objects.get(product_id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        

    