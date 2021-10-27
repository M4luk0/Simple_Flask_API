"""
Simple API
Copyright: Juan Antonio Gil Chamorro (M4luk0)
"""

# Libraries
from flask import Flask, request, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# App name
app = Flask(__name__)

# Limiter of requests
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


# Route /suma to plus numbers
@app.route('/suma', methods=["GET", "POST"])
@limiter.limit("30 per minute") # Limit of requests
def suma():
    # Web arguments
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")

    #Check headers
    if request.headers.get("s3cr3t") == '1337':
        return "El resultado de la suma es: " + str(int(n1) + int(n2)), 200
    else:
        return "Unauthorized", 403


# Route /admin to check if you are admin
@app.route('/admin', methods=["GET", "POST"])
@limiter.limit("10 per minute") # Limit of requests
def admin():
    # Check headers to set you as admin
    if request.headers.get("s3cr3t") == '1337':
        resp = make_response("")
        resp.set_cookie("app-session", "v4l1dt0k3n")
        return "Admin!", 200
    else:
        return "Unauthorized", 403
