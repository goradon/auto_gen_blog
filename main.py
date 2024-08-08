from gen_blog_ai import generate
from toNotion import create_notion_page
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import re


def main():
    BLOG = generate().text
    match = re.search(r"【(.*?)】", BLOG)
    if match:
        BLOG_TITLE = match.group(1)
    BLOG_CONTENT = BLOG[len(BLOG_TITLE)+7:]
    create_notion_page(BLOG_TITLE, BLOG_CONTENT)

    # 確認用
    print("-"*10)
    print(len(BLOG[len(BLOG_TITLE):])-2)
    print("-"*10)
    print(BLOG_TITLE)
    print("-"*10)
    print(STATUS)
    print("-"*10)
    print(BLOG_CONTENT)

if __name__ == "__main__":
    main() 