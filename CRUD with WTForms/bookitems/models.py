from bookitems import db


class BookList(db.Model):
    __tablename__ = 'booklist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(10), nullable=False, default='NA')

    def __repr__(self):
        return f"{self.name}-->{self.author}"
