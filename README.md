# OpenShift Client Demo

A Flask application that demonstrates using the Kubernetes Python client from a running OpenShift pod.

## deployment

Log in to an OpenShift cluster first.

```
git clone https://github.com/shaneboulden/openshift-client-demo
cd openshift-client-demo
oc new-app openshift_deploy/ocd.yaml
```
Uncomment (L31)[https://github.com/shaneboulden/openshift-client-demo/blob/master/ocd/ocd.py#L31] to use the Kubernetes API.

