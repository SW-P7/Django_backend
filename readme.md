Prerequisites

    Python 3.x
    Docker

Setting Up the Project

Clone the Repository:
    git clone https://github.com/SW-P7/Django_backend.git
    cd Django_backend

Create a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

Install Dependencies:
    pip install -r requirements.txt

Build the Docker image:
    docker compose build

Start the containers:
    docker compose up

Run commands in containers
    sudo docker exec -it [container_name] bash/python
    to run management commands:
        use bash and run python manage.py [management_command]
