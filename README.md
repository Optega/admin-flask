# Change the data in the file to Flask

## Setup

### .env

1. Create `.env` from `.evn example`;
2. Update the data in `.env`

A secret key should be as random as possible. Your operating system has ways to generate pretty random data based on a cryptographic random generator. Use the following command to quickly generate a value for `FLASK_SECRET_KEY`:

```bash
python -c 'import secrets; print(secrets.token_hex())'
```

### recipients.json

You need to create a file `admin/recipients.json` with the data template

```json
[
  {
    "id": 1,
    "phone": "+380987654321",
    "name": "John"
  },
  {
    "id": 2,
    "phone": "+380123456789",
    "name": "Jane"
  },
  {
    "id": 3,
    "phone": "+380918273645",
    "name": "Jack"
  },
  {
    "id": 4,
    "phone": "+380192837465",
    "name": "Jill"
  }
]
```

The program is created to edit the `recipients.json` file.
In docker, the `recipients.json` file is used by volume, it can be used in other code.

I am using code as an admin to change message recipients. I have a script that sends messages to recipients in the `recipients.json` file

## Run in Development Mode

```bash
cd admin
```

```bash
flask run --debug
```

## Run Container in Production Mode

```bash
docker compose -f docker/docker-compose.yml up -d
```
