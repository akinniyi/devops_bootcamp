In kubestuff folder
1. Start minikube
    minikube start
    minikube dashboard

2. Create folder name-kube-stuff with deployments & service files
3. Create deployment
    kubectl apply -f nginx-deployment.yaml

4. Create service
    kubectl apply -f service.yaml

minikube service nginx-deployment

Visit the minikube url
http://127.0.0.1:40707


docker build -t simple-app
docker tag simple-app niyibuggy/simple-app:latest
docker push niyibuggy/simple-app:latest
