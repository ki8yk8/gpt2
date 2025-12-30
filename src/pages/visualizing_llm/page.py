from dash import html
from ...markdown import markdown_to_dash

# first markdown
tokenization_section = markdown_to_dash("""
## Tokenization
This is a section that talks about the tokenization.
""")

page = html.Main(children=[tokenization_section])