from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics , filters
from .models import Order ,Product
from .serializers import OrderSerializer , ProductSerializer


from django.core.mail import send_mail
from django.core.mail import EmailMessage
from backend.settings import EMAIL_HOST_USER


class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response({
                'data': serializer.data,
                'message': "Orders data fetched successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'data': {},
                'message': f"Something went wrong while fetching the data: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Invalid data provided"
                }, status=status.HTTP_400_BAD_REQUEST)
            order = serializer.save()

            # ✅ Prepare email details properly
            subject = "New Order Placed"
            message = f"Dear {order.customer_name},\n\nYour order has been placed successfully!\nThank you for shopping with us."
            recipient_list = [order.customer_email]

            # ✅ Send the email
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,  # sender
                recipient_list,
                fail_silently=False,       # change to True if you don’t want to see errors
            )
            
            return Response({
                'data': serializer.data,
                'message': "New order created successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'data': {},
                'message': f"Something went wrong while creating the order: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def patch(self,request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                return Response({
                    'data':{},
                    'message': "Order is not found with this id"
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = OrderSerializer(order[0], data=data, partial = True)
            
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Invalid data provided"
                }, status=status.HTTP_500_BAD_REQUEST)
            
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': "New order created successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'data': {},
                'message': f"Something went wrong while creating the order: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                return Response({
                    'data':{},
                    'message': "Order is not found with this id"
                }, status=status.HTTP_404_NOT_FOUND)
            
            order[0].delete()
            return Response({
                'data': {},
                'message': "order is deleted!"
            }, status=status.HTTP_200_OK)

        except:
            return Response({
                'data': {},
                'message': "Something went wrong in deleted order"
            }, status=status.HTTP_400_BAD_REQUEST)
        


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product_name','category_name']
    ordering_fields = ['price','created_at']

class ProductRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer







