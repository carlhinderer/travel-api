from api import app

# FOR PRODUCTION
handler = app.create_app()


if __name__ == "__main__":
    # FOR DEVELOPMENT
    print("== Running in debug mode ==")
    app.run(host='0.0.0.0', port=5000, debug=True)
