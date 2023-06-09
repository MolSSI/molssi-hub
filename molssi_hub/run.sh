#!/bin/bash

file_list=$(find ./*/* -type d)
repo_list=$(docker search docker.io/molssiai | awk )

for i in $file_ist; do
    docker run --rm -t \
    -v $i:/myvol \
    -e DOCKER_USER='molssiai' -e DOCKER_PASS=$DOCKER_GH_TOKEN \
    -e PUSHRM_PROVIDER=dockerhub -e PUSHRM_FILE=/myvol/Dockerfile \
    -e PUSHRM_SHORT='my short description' \
    -e PUSHRM_TARGET=${target} \
    -e PUSHRM_DEBUG=1 \
    chko/docker-pushrm:1
done

target=docker.io/molssiai/debian-bullseye-slim-dev:5.2.2023