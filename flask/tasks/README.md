# Too Doo!

## Description

This project allow you to create and manage a simple todo list via a HTML web interface and a JSON based Web API

## API Documentation

### Retrieve all tasks

This route retrieves all tasks from the database.

#### Route: GET /api/v1/tasks/

Example JSON response: `GET /api/v1/tasks`

```json
{
  "status": "success", 
  "tasks": [
    {
      "completed": 0, 
      "creation_datetime": "Thu, 21 Apr 2022 11:10:53 GMT", 
      "description": "Get Milk", 
      "id": 1
    }, 
    {
      "completed": 0, 
      "creation_datetime": "Thu, 21 Apr 2022 11:10:57 GMT", 
      "description": "Get Eggs", 
      "id": 2
    }, 
    {
      "completed": 0, 
      "creation_datetime": "Thu, 21 Apr 2022 11:11:04 GMT", 
      "description": "Get Bread", 
      "id": 3
    }
  ]
}
```

* `status` (string) - message to indicate whether the operation was successful or not and why
* `tasks` (array) - list of all task items currently in the list
  * `task` attributes:
    * `completed` (int) - values 1 or 0 representing if the task is completed or not respectively
    * `creation_date` (datetime) - timestamp indicating when the task was added
    * `description` (string) - text detailing the task to be completed
    * `id` (int) - unique identifier of the task within the database

### Search for task by description

This route retrieves all task which contains text provided to the search query string parameter anywhere in the description.

#### Route: GET /api/v1/tasks/?search=[str: search text]

Example JSON response: `GET /api/v1/tasks/?search=milk`

```json
{
  "status": "success", 
  "tasks": [
    {
      "completed": 0, 
      "creation_datetime": "Thu, 21 Apr 2022 11:10:53 GMT", 
      "description": "Get Milk", 
      "id": 1
    }, 
    {
      "completed": 0, 
      "creation_datetime": "Thu, 21 Apr 2022 11:24:44 GMT", 
      "description": "Get Milkshakes", 
      "id": 4
    }
  ]
}
```

* `status` (string) - message to indicate whether the operation was successful or not and why
* `tasks` (array) - list of task item matching the provided `<int:id>`

### Retrieve a specific task by id

This route retrieves a task matching the provided id within the route

#### Route: GET /api/v1/tasks/[int:id]/

Example JSON response: `GET /api/v1/tasks/1/`

```json
{
  "status": "success", 
  "tasks": [
    {
      "completed": 0, 
      "creation_datetime": "Thu, 21 Apr 2022 11:10:53 GMT", 
      "description": "Get Milk", 
      "id": 1
    }
  ]
}
```

* `status` (string) - message to indicate whether the operation was successful or not and why
* `tasks` (array) - list of task item matching the provided `<int:id>`

### Add a new task to the list

Add a new task to the todo list with a POST request and supplying JSON data in the following format.

Input JSON:

```json
{
    "description": "Too much info Prof!!"
}
```

* `description` (string) - text defining the purpose of goal of the task item

#### Route: POST /api/v1/tasks/

Example JSON response: `POST /api/v1/tasks/`

```json
{
  "id": 5,
  "status": "success"
}
```

* `status` (string) - message to indicate whether the operation was successful or not and why
* `id` (int) - unique identifier of the new task within the database

### Update a task description

Update an existing task item's description with a PUT request and supplying JSON data in the following format.

Input JSON:

```json
{
    "description": "Updated task description"
}
```

* `description` (string) - text to update a task item's description

#### Route: PUT /api/v1/tasks/[int:task_id]/

Example JSON response: `POST /api/v1/tasks/1/`

```json
{
  "id": 1,
  "status": "success"
}
```

* `status` (string) - message to indicate whether the operation was successful or not and why
* `id` (int) - unique identifier of the task that has been updated

### Delete a Task

Remove an existing task from the database.

#### Route: DELETE /api/v1/tasks/[int:task_id]/

Example JSON response: `DELETE /api/v1/tasks/1/`

```json
{
  "id": 1,
  "status": "success"
}
```

* `status` (string) - message to indicate whether the operation was successful or not and why
* `id` (int) - unique identifier of the task that has been deleted