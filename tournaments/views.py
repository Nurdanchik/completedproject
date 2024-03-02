from rest_framework import generics, permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Tournament
# , SearchTournament
from .serializers import TournamentSerializer
# , SearchTournamentSerializer
from rest_framework.response import Response
from rest_framework import filters

class TournamentListCreateView(generics.ListCreateAPIView):
    search_fields = ['name', 'id']
    filter_backends = (filters.SearchFilter, )
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class TournamentListCreateView(generics.ListCreateAPIView):
#     search_fields = ['name']
#     filter_backends = (filters.SearchFilter, )
#     queryset = Tournament.objects.all()
#     serializer_class = TournamentSerializer

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TournamentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class SearchTournamentView(generics.ListAPIView):
#     queryset = Tournament.objects.all()
#     serializer_class = SearchTournamentSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):

#         to_search = request.query_params.get('tosearch', '')

#         try:
#             to_search_int = int(to_search)

#             queryset = self.queryset.filter(id=to_search_int)

#         except ValueError:
#             queryset = self.queryset.filter(name__icontains=to_search)

#         serializer = self.serializer_class(queryset, many = True)

#         return Response(serializer.data)

# class SearchTournamentView(generics.ListAPIView):
#     serializer_class = SearchTournamentSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         # Получаем параметр tosearch из запроса
#         to_search = request.query_params.get('tosearch', '')

#         try:
#             # Пытаемся преобразовать to_search в целое число
#             to_search_int = int(to_search)
#             # Ищем точное совпадение по идентификатору
#             queryset = self.queryset.filter(id=to_search_int)
#         except ValueError:
#             # Если не удается преобразовать в число, ищем частичное совпадение по имени
#             queryset = self.queryset.filter(name__icontains=to_search)

#         # Создаем сериализатор для результата
#         serializer = self.serializer_class(queryset, many=True)
#         # Возвращаем результат в виде JSON-ответа
#         return Response(serializer.data)
    
# class SearchTournamentView(generics.ListAPIView):
#     serializer_class = SearchTournamentSerializer

#     def get_queryset(self):
#         # Получаем значение tosearch из параметров запроса
#         to_search = self.request.query_params.get('tosearch', '')

#         queryset = Tournament.objects.all()

#         try:
#             # Пытаемся преобразовать to_search в целое число
#             to_search_int = int(to_search)
#             # Фильтруем турниры по точному совпадению с id
#             queryset = queryset.filter(name__icontains=to_search)
#         except ValueError:
#             # Если не удается преобразовать в число, фильтруем турниры по частичному совпадению с name
#             if len(to_search) >= 3:  # Проверяем, что строка имеет хотя бы 3 символа
#                 queryset = queryset.filter(name__icontains=to_search)

#         return queryset