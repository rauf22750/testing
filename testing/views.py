

from django.http import HttpResponse
from django.shortcuts import render
import os

def home(request):
    return render(request, 'homepage/home.html')

def static_html(request, filename):
    file_path = os.path.join('testing/static/html', filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/html')
    else:
        return HttpResponse("File not found.", status=404)

def index(request):
    # Define the HTML content with embedded CSS for design
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f0f8ff;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }

            h1 {
                font-size: 3em;
                color: #2c3e50;
                margin-bottom: 20px;
            }

            p {
                font-size: 1.5em;
                color: #34495e;
                line-height: 1.6;
            }

            .container {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 80%;
                max-width: 600px;
                margin: 20px;
            }

            .button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                font-size: 1.2em;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 20px;
                transition: background-color 0.3s ease;
            }

            .button:hover {
                background-color: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, World!</h1>
            <p>This is a simple HTML page returned from the index view in Django. It includes a basic design to make it visually appealing.</p>
            <a href="#" class="button">Click Me!</a>
        </div>
    </body>
    </html>
    """
    
    # Return the HTML content as an HTTP response
    return HttpResponse(html_content)


