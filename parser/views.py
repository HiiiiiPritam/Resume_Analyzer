from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from .utils import extract_text_from_pdf, extract_email, extract_phone

class ResumeUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('resume')
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        file_path = default_storage.save(file.name, file)
        text = extract_text_from_pdf(file_path)
        # print("\nExtracted Text:\n", text)

        email = extract_email(text)
        phone = extract_phone(text)

        request.session['email'] = email if email else "Not Found"
        request.session['phone'] = phone if phone else "Not Found"

        print("Session Email Set:", request.session['email'])  # Debugging
        print("Session Phone Set:", request.session['phone'])

        print("session ::::::::::::",request.session['email'])  # Should print extracted email
        print(request.session['phone']) 

        return Response({"email": email, "phone": phone})

def index(request):
    return render(request, "analyzer/upload.html")

def result_view(request):
    """This view will display extracted data"""
    print(request.session)
    email = request.session.get('email', "Not found")
    phone = request.session.get('phone', "Not found")
    return render(request, "analyzer/result.html", {"email": email, "phone": phone})