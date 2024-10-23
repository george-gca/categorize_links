from flask import Flask, render_template, request
from .categorize_links import categorize_links, remove_duplicates

TITLE = 'Categorize links into Research or Leisure'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def _root():
    if request.method == 'POST':
        if 'categorize' in request.form:
            links = request.form.get('links')

            if links is not None and len(links) > 0:
                research_links, other_links = categorize_links(links)
                values = {
                    'links': links,
                    'research_links': '\n'.join(remove_duplicates(research_links)),
                    'other_links': '\n'.join(remove_duplicates(other_links)),
                    'title': TITLE,
                }

                return render_template('index.html', **values)

    values = {
        'links': '',
        'research_links': '',
        'other_links': '',
        'form_script': '',
        'title': TITLE,
    }

    return render_template('index.html', **values)