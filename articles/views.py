from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import fitz
import requests
from django_elasticsearch_dsl.search import Search
from .document import YourModelDocument
from .models import YourModel  # Add this import
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def articles_list(request):
    articles=Article.objects.all()
    return render(request, 'article_list.html',{'articles':articles})


def article_detail(request,slug):
    return HttpResponse(slug)

def extract_text_from_pdf(request):
    # Direct link to the PDF file on Google Drive (replace with the actual URL)
    pdf_url = 'https://drive.google.com/uc?id=1-CG4cP2sAOKkpp3r92PDqsJzvCcOfkkp'

    try:
        # Download the PDF content
        response = requests.get(pdf_url)
        response.raise_for_status()

        # Open the PDF content
        pdf_document = fitz.open(stream=response.content, filetype="pdf")

        extracted_text = []
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            page_text = page.get_text()
            extracted_text.append(page_text)

        pdf_document.close()

        # Return the extracted text as JSON
        return JsonResponse({'success': True, 'text': extracted_text})

    except requests.exceptions.RequestException as re:
        return JsonResponse({'success': False, 'error': f'Request error: {re}'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        search = Search(index='yourmodel_index').query("match", name=query)
        results = search.execute()
        result_text = "\n".join([f"Name: {hit.name}, Description: {hit.description}" for hit in results])
    else:
        results = YourModel.objects.all()
        result_text = "\n".join([f"Name: {item.name}, Description: {item.description}" for item in results])
        result_text += "\nCustom Text for 'else' Condition"  # Add your custom text here


    return HttpResponse(result_text, content_type='text/plain')



@api_view(['POST'])
def tagged_post_view(request):
    

    tag_value = request.data

    return Response({'success': True, 'tag_value': tag_value}, status=status.HTTP_200_OK)


