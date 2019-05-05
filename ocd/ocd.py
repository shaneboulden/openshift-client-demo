# This is the odc front-end.

from flask import Flask, render_template, flash, redirect, request

import requests
import json
import os
from kubernetes import client, config

application = Flask(__name__)
application.secret_key = os.environ['FLASK_SECRET']
config.load_incluster_config()
v1 = client.CoreV1Api()

@application.route('/healthz')
def healthz():
    """
    Check the health of this peakweb instance. OCP will hit this endpoint to verify the readiness
    of the peakweb pod.
    """
    return 'OK'

@application.route('/pods')
def pods():
    """
    List pods in the current project
    """
    pods = json.dumps(v1.list_namespaced_pod(namespace=os.environ["POD_NAMESPACE"]).to_dict())
    print(pods)
    return render_template('pods.html',pods=pods)

@application.route('/')
def index():
    return render_template('index.html')
