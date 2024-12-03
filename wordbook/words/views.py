from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Word
from .serializers import WordSerializer
import random


class WordListView(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordDetailView(APIView):
    def get(self, request, word_id):
        try:
            word = Word.objects.get(id=word_id)
            serializer = WordSerializer(word)
            return Response(serializer.data)
        except Word.DoesNotExist:
            return Response({"error": "Word not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, word_id):
        try:
            word = Word.objects.get(id=word_id)
            word.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Word.DoesNotExist:
            return Response({"error": "Word not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, word_id):
        try:
            word = Word.objects.get(id=word_id)
            serializer = WordSerializer(word, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Word.DoesNotExist:
            return Response({"error": "Word not found"}, status=status.HTTP_404_NOT_FOUND)

        
class RandomWordView(APIView):
    def get(self, request):
        words = list(Word.objects.all())
        random.shuffle(words)
        serializer = WordSerializer(words[:10], many=True)  # 최대 10개 반환
        return Response(serializer.data)