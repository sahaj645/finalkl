from django.http import JsonResponse

def home_page(request):
    print("home page requested")
    # Assuming you have a list of news articles or stories
    news_articles = [
        {
            'title': 'Breaking News: Something happened!',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
            'author': 'Reporter A',
            'published_at': '2024-04-11T08:00:00Z'
        },
        {
            'title': 'Another News Article',
            'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...',
            'author': 'Reporter B',
            'published_at': '2024-04-10T12:30:00Z'
        },
        # Add more news articles as needed
    ]
    return JsonResponse(news_articles, safe=False)
