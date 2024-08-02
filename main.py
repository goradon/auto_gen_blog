from gen_blog_ai import generate
from toNotion import create_notion_page

BLOG = generate().text
BLOG_TITLE = BLOG[:10] #TODO:もっとうまくやる
BLOG_CONTENT = BLOG

create_notion_page(BLOG_TITLE, BLOG_CONTENT)