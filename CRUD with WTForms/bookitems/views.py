from bookitems import app, db
from flask import render_template, redirect, url_for, request, flash
from bookitems.models import BookList
from bookitems.forms import BookForm


@app.route("/")
@app.route("/home")
def home():
    books = BookList.query.all()
    return render_template('home.html', books=books)


@app.route("/addbook", methods=['GET', 'POST'])
def addbook():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            book = BookList(name=form.name.data, author=form.author.data, price=form.price.data)
            db.session.add(book)
            db.session.commit()
            flash('Your book has been Added!')
            return redirect(url_for('home'))
        else:
            flash('***Please, Insert valid values!***')
    return render_template('add_book.html', form=form, title='Add Book')


@app.route("/edit/<int:id>")
def edit(id):
    form = BookForm()
    book = BookList.query.filter_by(id=id).first()
    form.id.data = book.id
    form.name.data = book.name
    form.author.data = book.author
    form.price.data = book.price

    return render_template('edit.html', title='Edit Book', form=form)


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # book = BookList(name=form.name.data, author=form.author.data, price=form.price.data)
            updated_book = BookList.query.filter_by(id=id).update(
                dict(name=form.name.data, author=form.author.data, price=form.price.data))
            db.session.commit()
            flash('Your book has been Updated Successfully!')
            return redirect(url_for('home'))
        else:
            flash('Please, Insert valid values!')
    return render_template('edit.html', form=form, title='Update')


@app.route("/delete/<int:id>")
def delete(id):
    if request.method == 'GET':
        book = BookList.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))
