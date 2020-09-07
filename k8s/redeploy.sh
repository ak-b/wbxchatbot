#!/bin/bash

set -x
NS=<>

kubectl delete -f <>.yml
kubectl delete configmap <> --namespace=$NS

kubectl create configmap <> --from-file=users.properties=./users.properties --namespace=$NS
kubectl create -f <>.yml
