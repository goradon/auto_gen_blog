from gen_blog_ai import generate
from toNotion import create_notion_page
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import re



BLOG = generate().text
match = re.search(r"【(.*?)】", BLOG)
if match:
    BLOG_TITLE = match.group(1)
BLOG_CONTENT = BLOG[len(BLOG_TITLE)+6:]
create_notion_page(BLOG_TITLE, BLOG_CONTENT)
print(len(BLOG[len(BLOG_TITLE):])-2)