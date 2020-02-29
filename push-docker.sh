#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=text_adventure .


dockerpath="vkumaresan/text_adventure"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag text_adventure $dockerpath

# Push Image
docker image push $dockerpath 