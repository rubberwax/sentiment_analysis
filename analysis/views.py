from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline
from django.shortcuts import render


# Load the sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

@api_view(['POST'])
def analyze(request):
    text = request.data.get('text', '')
    result = sentiment_pipeline(text)[0]
    return Response(result)


def index(request):
    return render(request, 'analysis/index.html')

