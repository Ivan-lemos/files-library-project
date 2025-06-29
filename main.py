from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# all_books = []
all_books = [
     {
        "title": "Harry Potter",
        "author": "J. K. Rowling",
        "rating": 9,
    }
]

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        new_book = request.form.to_dict()
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

