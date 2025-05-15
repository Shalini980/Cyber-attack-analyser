from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        scan_type = request.form.get('scanType')

        # Simulate scan result
        result = simulate_scan(url)
        return redirect(url_for('report', url=url, status=result['status'], score=result['score']))

    return render_template('index.html')


@app.route('/report')
def report():
    url = request.args.get('url')
    status = request.args.get('status')
    score = request.args.get('score')

    # Simulated vulnerabilities
    vulnerabilities = []
    if status == 'unsafe':
        vulnerabilities = [
            {"cve": "CVE-2023-1234", "desc": "SQL Injection vulnerability"},
            {"cve": "CVE-2024-4321", "desc": "Remote Code Execution on port 8080"},
        ]

    # Simulated severity breakdown
    severity = {
        'critical': 2,
        'high': 5,
        'medium': 3,
        'low': 1,
        'info': 0
    }

    # Verdict message and color logic
    if status == 'safe':
        verdict_message = "The website is secure!"
        additional_info = "No major issues detected."
    elif status == 'moderate':
        verdict_message = "The website is moderately secure."
        additional_info = "Some improvements are needed."
    else:
        verdict_message = "The website is very insecure!"
        additional_info = "Fix critical vulnerabilities immediately."

    return render_template(
        'report.html',
        url=url,
        status=status,
        score=score,
        vulnerabilities=vulnerabilities,
        severity=severity,
        verdict_message=verdict_message,
        additional_info=additional_info
    )


def simulate_scan(url):
    import random
    score = random.randint(30, 95)
    if score >= 80:
        status = 'safe'
    elif score >= 60:
        status = 'moderate'
    else:
        status = 'unsafe'
    return {'score': score, 'status': status}


if __name__ == '__main__':
    app.run(debug=True)