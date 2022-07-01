# Flask-REST-API

Development of a CRUD RESTful API with Flask, using a SQLite database for data storage.  

## Description

The API endpoints provide the ability for registered users to retrieve and modify a database of household items for sale. Each item has a `name` and a `price`. The data was initially held in an in-memory list, but developed to use a SQLite database to maintain a persistent state. The code for both versions is available in this repository.

Authentication features are handled with Flask-JWT, with only registered and authenticated users able to access methods. Comprehensive testing was conducted using [Postman](https://www.postman.com/). 

## API extension project
The [flask-sqlalchemy](https://github.com/mhoward91/flask-sqlalchemy) project builds on the capabilities of this API by incorporating the following:
- A stores table in the database schema, allowing household items to be allocated to a specific store
- The use of SQLAlchemy as an ORM, to more efficiently create db tables, queries, and individual objects from each row of data 
- Deployment with Heroku & use of a PostgreSQL database
- Token refreshing and additional Flask-JWT-Extended features

## Endpoints

### 1. /items

**Available methods**

| Method   | Description                              |
| -------- | ---------------------------------------- |
| `GET`    | Returns the complete items list as `json` data, displaying the names and prices of each item |

Sample response:
```
{
    "item_list": [
        {
            "name": "piano",
            "price": 15.99
        },
        {
            "name": "sofa",
            "price": 15.99
        }
    ]
}
```

### 2. /item/\<name\>

- **URL Parameters** `GET` `POST` `PUT` `DELETE`

    `name=[str]` (required) 

- **Request Headers** `POST` `PUT`

    `{"Content-Type": "application/json"}`

- **Data (json payload)** `POST` `PUT`

    `{"price": <price>[float]}`
 
**Available methods**

| Method   | Description                              | HTTP Response
| -------- | ---------------------------------------- | -------------|
| `GET`    | Returns data on a single item, identified by the \<name\> parameter | `200 OK` if item found, otherwise `404 Not Found` if item doesn't exist |
| `POST`    | Adds an item with name=\<name\> to the items list, with a price defined in the json payload | `201 Created` if item added, `400 Bad Request` if item already exists |
| `PUT`    | Adds an item with name=\<name\>to the items list if not present, otherwise updates the item's price with the price defined in the json payload | `200 OK` if item added or updated |
| `DELETE`    | Deletes the item with name=\<name\> from the items list | `200 OK` if item successfully deleted |

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
