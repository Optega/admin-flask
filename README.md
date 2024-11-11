# Change the data in the file to Flask

## Before use

You need to create a file ```admin/recipients.json``` with the data

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

The program is created to edit the ```recipients.json``` file.
In docker, the ```recipients.json``` file is used by volume, it can be used in other code.

I am using code as an admin to change message recipients. I have a script that sends messages to recipients in the ```recipients.json``` file

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
