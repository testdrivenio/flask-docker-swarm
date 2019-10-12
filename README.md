# Running Flask on Docker Swarm

## Want to learn how to build this?

Check out the [post](https://testdriven.io/running-flask-on-docker-swarm).

## Want to use this project?

1. Fork/Clone

1. [Sign up](https://m.do.co/c/d8f211a4b4c2) for Digital Ocean and [generate](https://www.digitalocean.com/docs/api/create-personal-access-token/) an access token

1. Add the token to your environment:

    ```sh
    $ export DIGITAL_OCEAN_ACCESS_TOKEN=[your_token]
    ```

1. Spin up four droplets and deploy Docker Swarm:

    ```sh
    $ sh deploy.sh
    ```
