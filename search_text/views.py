from rest_framework.decorators import APIView
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
from django.shortcuts import render
# from search_text.dropboxAPI import getFilesFromDropBoxFolder, getTextFromLinks, test
from search_text.s3 import fetchFromS3, readTextFromFile
from search_text.elasticSearch import insertDocuments, searchText


class ParseTextView(APIView):

    def post(self, request):
        s3response = fetchFromS3()
        files_list = s3response["pdf_files"]
        for data in files_list:
            text = readTextFromFile(data["pdfFile"])
            data["text"] = text
            data.pop("pdfFile")
        response = insertDocuments(files_list)
        if response["success"] == True:
            return Response({"sucess" : True, "code": 200, "message" : response["message"], "error" : s3response["error"]})
        return Response({"sucess" : False, "code": 500, "message" : response["error"]})


class SearchTextView(APIView):

    def get(self, request):
        text = request.GET.get("text", None)
        if text == None:
            return Response({"sucess" : False, "code": 500, "message" : "please enter text to be searched"})
        response = searchText(text)
        if response["success"] == True:
            return Response({"sucess" : True, "code": 200, "data" : response["data"]})
        return Response({"sucess" : False, "code": 500, "message" : response["error"]})


class HomeView(APIView):

    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        text = request.POST['search_token']
        if text != None and len(text) > 0 :
            response = searchText(text)
            if response["success"] == True:
                return render(request, "index.html", {"data" : response["data"]})
            else:
                return render(request, "index.html", {"error" : response["error"]})
        else:
            return render(request, "index.html")



