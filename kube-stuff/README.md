In kubestuff folder
1. Create deployment
    kubectl apply -f nginx-deployment.yaml

1. Create service
    kubectl apply -f service.yaml

minikube service nginx-deployment

Visit the minikube url
http://127.0.0.1:40707