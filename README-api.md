

GET http://127.0.0.1:8000/locations/

Returns 200 status code


POST http://127.0.0.1:8000/locations/ 

Content Type : application/json

json data: 

{
    "name":"howard_center", 
    "longitude": 38.921216999999999,
    "latitude": -77.020461999999995
}


Returns 201 status code with json data: 

{
    "name":"howard_center", 
    "longitude": 38.921216999999999,
    "latitude": -77.020461999999995
}