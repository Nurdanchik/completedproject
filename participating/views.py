from rest_framework import generics
from .models import Request
from rest_framework.views import APIView
import stripe
from .serializers import RequestSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from booking import settings
from tournaments.models import Tournament

class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        tournament_id = self.request.data.get('tournament_id')
        tournament = get_object_or_404(Tournament, id=tournament_id)

        # Проверьте, что Checkout Session завершен успешно
        if tournament.checkout_session_id and stripe.checkout.Session.retrieve(tournament.checkout_session_id).payment_status == 'paid':
            serializer.save(user=self.request.user, tournament=tournament)
        else:
            # Обработка случая, если платеж не завершен успешно
            raise serializers.ValidationError("Payment not completed successfully.")

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        tournament_id = request.data.get('tournament_id')
        tournament = get_object_or_404(Tournament, id=tournament_id)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Participation in Tournament',
                    },
                    'unit_amount': int(tournament.price_for_participating * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success/',
            cancel_url='https://example.com/cancel/',
        )

        # Сохраните идентификатор Checkout Session в базе данных или в объекте турнира
        tournament.checkout_session_id = checkout_session.id
        tournament.save()

        return JsonResponse({'id': checkout_session.id})