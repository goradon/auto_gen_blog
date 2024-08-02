import requests
from config import NOTION_API_KEY, DATABASE_ID, STATUS

def create_notion_page(blog_title, blog_content):
    url = 'https://api.notion.com/v1/pages'

    headers = {
        'Notion-Version': '2022-06-28',
        'Authorization': 'Bearer ' + NOTION_API_KEY,
        'Content-Type': 'application/json',
    }

    json_data = {
        'parent': {'database_id': DATABASE_ID},
        'properties': {
            'Title': {
                'title': [
                    {
                        'text': {
                            'content': blog_title
                        }
                    }
                ]
            },
            'Tags': {
                'select': {
                    'name': STATUS
                }
            }
        },
        "children": [
            {
                "object": 'block',
                "type": 'quote',
                "quote": {
                    "rich_text": [
                        {
                            "text": {
                                "content": blog_content
                            }
                        }
                    ],
                }
            },
        ],
    }

    response = requests.post(url, headers=headers, json=json_data)
    return response