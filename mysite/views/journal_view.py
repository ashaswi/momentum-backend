
from rest_framework import viewsets
from mysite.models import Journal
from mysite.serializers.journal_serializer import JournalSerializer
from rest_framework.permissions import IsAuthenticated


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)