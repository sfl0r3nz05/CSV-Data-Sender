# CSV Data Sender

- Basic project to send data from a CSV file over a socket.

## Project status

- The project is under development: 🛠 by [sfl0r3nz05](sfigueroa@ceit.es)

## Architecture

![project architecture]()

## Requirements

The requirements are to have docker installed and a network called `syntheticnet` created on it, to install docker you can follow [this](https://docs.docker.com/engine/install/) guide, and to create a docker network run the following command:

```bash
docker network create syntheticnet
```

## Generate data

## How to use

1. Set the environment variables of the `docker-compose.yml` file:

    ```console
    SOCK_LISTENER_HOST=publisher
    SOCK_LISTENER_PORT=8053
    ```

2. To launch the program using docker simply place your terminal in the project folder and run the following command:

    ```console
    docker-compose up
    ```

## To Do

- Add trivy vulnerability scanner to github workflow
- Build a container as part of the github workflow
- Push the container to Docker Hub registry
