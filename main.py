from gen_blog_ai import generate
from toNotion import create_notion_page
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models


BLOG = generate().text
BLOG_TITLE = BLOG[0]
BLOG_CONTENT1 = BLOG[0:900]
BLOG_CONTENT2 = BLOG[900:1800]
BLOG_CONTENT3 = BLOG[1800:2700]
BLOG_CONTENT4 = BLOG[2700:3600]
BLOG_CONTENT5 = BLOG[3600:4500]
BLOG_CONTENT6 = BLOG[5400:6300]
BLOG_CONTENT7 = BLOG[7200:8100]
BLOG_CONTENT8 = BLOG[8100:]

create_notion_page(BLOG_TITLE, BLOG_CONTENT1, BLOG_CONTENT2, BLOG_CONTENT3, BLOG_CONTENT4, BLOG_CONTENT5, BLOG_CONTENT6, BLOG_CONTENT7, BLOG_CONTENT8)