from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/uppercase', methods=['GET', 'POST'])
def work_uppercase():
    result = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = text.upper()
    return render_template('work_uppercase.html', result=result)

@app.route('/works/circle', methods=['GET', 'POST'])
def work_circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            if radius > 0:
                area = math.pi * (radius ** 2)
                circumference = 2 * math.pi * radius
                result = {"area": round(area, 2), "circumference": round(circumference, 2)}
        except ValueError:
            pass
    return render_template('work_circle.html', result=result)

@app.route('/works/triangle', methods=['GET', 'POST'])
def work_triangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            if base > 0 and height > 0:
                area = 0.5 * base * height
                result = {"area": round(area, 2)}
        except ValueError:
            pass
    return render_template('work_triangle.html', result=result)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
