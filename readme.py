from dash import dcc

# Markdown to HTML function
def markdown_to_html(markdown_url, style_dic):
    # Read README file
    readme_content = open(markdown_url, "r", encoding="utf-8").read()
    return dcc.Markdown(children=readme_content, style=style_dic.readme_style)