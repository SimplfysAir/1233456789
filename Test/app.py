from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        company_name = request.form['companyName']
        result = fetch_company_data(company_name)
    return render_template('index.html', result=result)

def fetch_company_data(company_name):
    try:
        process = subprocess.Popen(
            ['python', 'your_script.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        result = process.communicate(input=company_name.encode())[0]
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
