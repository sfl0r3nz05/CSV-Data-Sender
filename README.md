# CSV Data Sender

Basic project to send data from a CSV file over a socket.

>**Note:** At this moment the project is ad-hoc to send positioning data loaded in CSV, but in the To Do is to give guidelines to send any kind of data.

## Project status

- The project is under development: 🛠 by [sfl0r3nz05](sfigueroa@ceit.es)

## Architecture

- The CSV Data Sender must be ready for use in any environment. E.g.:

![Architecture3](https://user-images.githubusercontent.com/6643905/219713121-d5684b33-8308-4d06-9a6f-5d5050baeb16.png)

## Requirements

- The requirements are to have docker installed and a network called `syntheticnet` created on it, to install docker you can follow [this](https://docs.docker.com/engine/install/) guide, and to create a docker network run the following command:

  ```bash
  docker network create syntheticnet
  ```

- In case of using the agent to connect to an already existing network, it will be enough to modify the docker-compose file. E.g.:

  ```console
  networks:
    default:
        external:
           name: syntheticnet
  ```

## How to Generate new data

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

- [Demonstration video of sending data to an AMQP publisher agent](https://youtu.be/OavGNGMnQZ4)
- [Demostration Video of sending data to a MQTT publisher agent](https://youtu.be/k_vCP0BRygY)

## To Do

- Add trivy vulnerability scanner to github workflow
- Improve project documentation
- Manage any kind of data
