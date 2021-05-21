from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from search_text.dropboxAPI import getFilesFromDropBoxFolder, getTextFromLinks, test
from search_text.s3 import fetchFromS3, readTextFromFile


class SearchTextView(APIView):

    def post(self, request):
        files = fetchFromS3()
        texts = []
        for pdfFile in files:
            text = readTextFromFile(pdfFile)
            texts.append(text)
        return Response({"sucess" : False, "code": 500, "message" : "serializer.errors"})