from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
import os

@api_view(['POST'])
def bfhl_post(request):
    data = request.data.get('data', [])
    file_b64 = request.data.get('file_b64', None)
    
    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Find the highest lowercase alphabet
    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
    
    # File handling
    file_valid = False
    file_mime_type = None
    file_size_kb = None
    if file_b64:
        try:
            file_content = base64.b64decode(file_b64)
            file_size_kb = len(file_content) / 1024
            file_valid = True
            file_mime_type = "application/octet-stream"  # Can improve by detecting real MIME type
        except Exception:
            pass
    
    # Return response
    return Response({
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",
        "email": "your_email@college.edu",
        "roll_number": "your_roll_number",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    })


@api_view(['GET'])
def bfhl_get(request):
    return Response({
        "operation_code": 1
    })
from django.shortcuts import render

def frontend_view(request):
    return render(request, 'index.html')
