from app import db


class CompendiumEntry(db.Model):
    __tablename__ = 'compendium'

    page_id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(30), nullable=False)
    contents = db.Column(db.String)
    approval = db.Column(db.String(10))

    def __init__(self, page_name, contents, approval='UNAPPROVED'):
        self.page_name = page_name
        self.contents = contents
        self.approval = approval

    def __repr__(self):
        return 'Compendium page {} is about {} and is {}'.format(self.page_id, self.page_name, self.approval)
