from prototype2 import start_game

start_game()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)