# views.py
from django.shortcuts import render
import requests

def index(request):
    base_url = "https://staging-api.modrinth.com/v2/search"
    
    # Get the query parameter from the form submission or from the request's GET parameters
    query = request.GET.get('query')

    facets = [["categories:forge"], ["versions:1.17.1"], ["project_type:mod"], ["license:mit"]]
    facet_string = "&".join([f"facets[]={','.join(facet)}" for facet in facets])
    full_url = f"{base_url}?query={query}&{facet_string}"

    # Make the request to the Minecraft API
    response = requests.get(full_url)

    # Convert the response to JSON
    data = response.json()

    # Pass the data and the current query to the template
    return render(request, 'portal/index.html', {'hits': data.get('hits', []), 'current_query': query})
