from flask import Flask, request, render_template, redirect, abort
from functions import encode,redirect_url, start_db

app = Flask(__name__)
start_db()

@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found!', 404


@app.route('/', methods=['GET', 'POST'])
def url_short():
    if request.method == 'POST':
        name = request.form['url']
        short_url = encode(name)
        
        return render_template('url.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<url_encoded>')
def original_redirect(url_encoded):
    redirection_page = redirect_url(url_encoded)

    if redirection_page is None:
        abort(404)

    return redirect(redirection_page)
    



if __name__ == '__main__':
    app.run(debug=True)