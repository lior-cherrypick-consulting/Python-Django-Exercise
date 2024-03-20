# Python-Django Exercise
## Installation ##
1. Install Docker on your machine: https://docs.docker.com/get-docker/
2. Clone this repository.
3. Set up an `.env` file in the repository's root folder. Refer to `.env.example` to see an example.
4. Ensure that `DB_PORT` from your `.env` file and `8000` ports aren't used on your machine.
4. Run in a terminal the following command to run the Django application:
`docker compose up -d`

## Usage ##
When the application is running, the REST endpoints can be accessed at `http://localhost:8000/api`.

## Testing ##
To run tests please run:
`docker compose exec web python manage.py test`