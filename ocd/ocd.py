# This is the openshift-client-demo front-end.

from flask import Flask, render_template, flash, redirect, request

import requests
import json
import os
# import the Kubernetes client and config objects
from kubernetes import client, config

application = Flask(__name__)
application.secret_key = os.environ['FLASK_SECRET']
config.load_incluster_config()
v1 = client.CoreV1Api()

@application.route('/healthz')
def healthz():
    """
    Check the health of this demo instance. OCP will hit this endpoint to verify the readiness
    of the demo pod.
    """
    return 'OK'

@application.route('/pods')
def pods():
    """
    List pods in the current project
    """
    pods = False
    # Uncomment this line to get the pods lookup working
    #pods = v1.list_namespaced_pod(namespace=os.environ["POD_NAMESPACE"])
    return render_template('pods.html',pods=pods)

@application.route('/')
def index():
    return render_template('index.html')

