import os
from urllib.parse import urlparse

from dotenv import load_dotenv
from flask import Flask
from flask import render_template, request

from create_cloud import create_cloud

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['POST', 'GET'])
def get_link():
    if request.method == 'POST':
        link = request.form['link']
        disassembled_url = urlparse(link)
        group_id = os.path.basename(disassembled_url.path)
        error = create_cloud(group_id)
        if error:
            return render_template('template.html', context={
                "error": error
                })

        return render_template('template.html', context={
            "filename": f'images/{group_id}.png'
            })

    return render_template('template.html', context=None)


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
