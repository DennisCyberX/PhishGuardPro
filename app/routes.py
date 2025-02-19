from flask import render_template, request, send_file
from app import app
from app.phishing_detection import analyze_input
from app.report_generator import generate_report

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['input']
    analysis_result = analyze_input(user_input)
    report_path = generate_report(user_input, analysis_result)
    return send_file(report_path, as_attachment=True)
