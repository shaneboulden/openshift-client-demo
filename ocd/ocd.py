# This is the odc front-end.

from flask import Flask, render_template, flash, redirect, request

import requests
import json
import os
import kubernetes.client
import kubernetes.config
from openshift.dynamic import DynamicClient

application = Flask(__name__)
application.secret_key = os.environ['FLASK_SECRET']
k8s_client = config.load_incluster_config()
dyn_client = DynamicClientk8s_client)


@application.route('/healthz')
def healthz():
    """
    Check the health of this peakweb instance. OCP will hit this endpoint to verify the readiness
    of the peakweb pod.
    """
    return 'OK'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/pods')
    """
    List pods in the current project
    """
def pods():
    v1_pods = dyn_client.resources.get(api_version='v1', kind='Pod')
    pods = v1_pods.get()
    print(v1_pods)
    return render_template('pods.html',pods=pods)
