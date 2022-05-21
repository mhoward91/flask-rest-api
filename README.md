# Flask-REST-API

Current project - development of RESTful APIs with Flask, ultimately using a SQLite database for data storage and Heroku for deployment. 

## Description

The intention of this project is to expand my knowledge of RESTful API development using Flask. The endpoints provide the ability for users to retrieve and modify a database of household items for sale. Each item has a `name` and a `price`. Initially, the database is an in-memory python list (which is lost everytime the program restarts), but will develop to become a SQLite database, through the use of the SQLAlchemy toolkit. 

The current code, which uses an in-memory database can be found [here](https://github.com/mhoward91/flask-rest-api/tree/master/in-memory). All methods are comprehensively tested using [Postman](https://www.postman.com/). 

## Features planned/in development
- Advanced request parsing
- Authentication
- Use of SQLite database instead of in-memory list
- Deployment to Heroku
- Additional security & token refreshing

## Endpoints

### 1. /items

**Available methods**

| Method   | Description                              |
| -------- | ---------------------------------------- |
| `GET`    | Returns the full items list as `json` data, displaying the names and prices of each item |

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
| `DELETE`    | Deletes the item with name=\<name\> from the items list | _In development_ |

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
