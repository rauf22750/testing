from django.http import HttpResponse

def index(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to My Project</title>
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
                font-size: 2.5em;
                color: #2c3e50;
                margin-bottom: 20px;
            }

            p {
                font-size: 1.3em;
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
                text-align: center;
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

            .profile-pic {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://via.placeholder.com/150/0000FF/808080 ?Text=PAKAINFO.com" alt="Profile Picture" class="profile-pic">
            <h1>Welcome to My First Deployment!</h1>
            <p>This is my first deployed project on Vercel, created using Django. I am a Python Django developer currently working on an NLP project focused on building a chatbot.</p>
            <p>Feel free to explore my work and learn more about the exciting projects I'm developing in the field of Natural Language Processing (NLP).</p>
            <a href="#" class="button">Check Out My Project</a>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)
