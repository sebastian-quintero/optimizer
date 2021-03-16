# optimizer

Template for an optimizer to be deployed into production. A
simple [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
is built as a sample.

## Set Up

Create a Python virtual environment. Install the `virtualenv` library.

```bash
pip install virtualenv
```

Create the `venv`.

```bash
virtualenv venv
```

Activate the `venv`.

```bash
source venv/bin/activate
```

Install requirements.

```bash
pip install -r requirements.txt
```

## Deploy

### Locally

First, set your `PYTHONPATH`.

```bash
export PYTHONPATH=.
```

Run the app.

```bash
uvicorn main:optimizer --host localhost --port 8080
```

or

```bash
python3 main.py
```

Make requests to `http://localhost:8080`.

### Docker

Build the image with the `Dockerfile` recipe and name it `optimizer`.

```bash
docker build -t optimizer .
```

Run the `optimizer` image in the background (`-d`), name it `optimizer-app` and
expose port `8080`.

```bash
docker run -d --name optimizer-app -p 8080:8080 optimizer
```

Make requests to `http://localhost:8080`.

## Use

Make the following request:

```bash
curl -L -X POST 'http://localhost:8080/knapsack/' \
-H 'Content-Type: application/json' \
--data-raw '{
    "items": [
        {
            "name": "Laptop",
            "weight": 4,
            "value": 3
        },
        {
            "name": "Cellphone",
            "weight": 3,
            "value": 5
        },
        {
            "name": "Headphones",
            "weight": 2,
            "value": 3
        },
        {
            "name": "Charger",
            "weight": 4,
            "value": 1
        },
        {
            "name": "Extension",
            "weight": 5,
            "value": 4
        },
        {
            "name": "Camera",
            "weight": 5,
            "value": 5
        },
        {
            "name": "Tablet",
            "weight": 6,
            "value": 5
        },
        {
            "name": "Case",
            "weight": 2,
            "value": 1
        },
        {
            "name": "Glasses",
            "weight": 4,
            "value": 1
        },
        {
            "name": "Earphones",
            "weight": 2,
            "value": 2
        },
        {
            "name": "Ultrabook",
            "weight": 5,
            "value": 7
        },
        {
            "name": "Sunglasses",
            "weight": 2,
            "value": 3
        },
        {
            "name": "Magazine",
            "weight": 3,
            "value": 1
        },
        {
            "name": "Book",
            "weight": 2,
            "value": 4
        },
        {
            "name": "Powerbank",
            "weight": 2,
            "value": 2
        },
        {
            "name": "Sunscreen",
            "weight": 2,
            "value": 5
        }
    ],
    "capacity": 20
}'
```

You should get the following response:

```JSON
{
  "selected_items": [
    "Cellphone",
    "Headphones",
    "Earphones",
    "Ultrabook",
    "Sunglasses",
    "Book",
    "Powerbank",
    "Sunscreen"
  ],
  "total_value": 31.0,
  "total_weight": 20.0
}
```
