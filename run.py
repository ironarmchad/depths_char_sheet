from app import create_app, db

if __name__ == "__main__":
    char_app = create_app('dev')
    with char_app.app_context():
        db.create_all()

    char_app.run()
