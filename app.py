from flask import Flask, render_template

app = Flask(__name__)  # Correctly instantiate the Flask app

@app.route('/')
def register():
    return render_template("register_form_devops.html")

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
