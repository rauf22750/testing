from django.http import HttpResponse
from django.http import HttpResponse

def index(request):
    # Define the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a simple HTML page returned from the index view in Django.</p>
    </body>
    </html>
    """
    
    # Return the HTML content as an HTTP response
    return HttpResponse(html_content)

