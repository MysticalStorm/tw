from server import app, db

db.create_all()
app.run()