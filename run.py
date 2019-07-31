from app import create_app

if __name__ == "__main__":
    char_app = create_app('dev')

    char_app.run()
