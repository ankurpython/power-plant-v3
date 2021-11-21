# Emissions & Generation Resource Integrated Database (eGRID) 

**The Purpose of this project to visualize the eGRID database.Requirements of the project are:**

> - We want to show a map to visualize the annual net generation of power plants in the US.
> - We want to display the top-n plants.
> - We want to be able to filter by state.
> - We want to be able to see a single plant's details, including the actual and percentage values of the plants' contribution to its federal state.


**The Stack which are used Python, Django, RESTful API,SQLite3 Pandas, Matplotlib, Nginx.**

Please go through the **Requirements.txt file: https://gitlab.com/ankurpython/power-plant/-/blob/main/requirements.txt** and install all the requirements.

* ```pip install -r requirements.txt```

## Required

* Install **the Docker:** **https://docs.docker.com/docker-for-windows/install/ (for Windows) and for other environment https://docs.docker.com/engine/install/**
* **Docker-compose: https://docs.docker.com/compose/install/**

## Steps to Run 
> 1. Download or Clone the Repository:    **https://gitlab.com/ankurpython/power-plant.git**
> 2. Run the container: * ```docker-compose up```
> 3. Create the superuser using this command Run the: **docker exec -it container_id python manage.py createsuperuser**
> 4. Login with username and password.**http://localhost:8000/admin_login** .This will return the access token which will require in all the endpoints.
> 5. GET request with Bearer token using this endpoint for set of map data: **http://127.0.0.1:8000/map/**
> 6. Request for visualize map : **http://127.0.0.1:8080/lib_map**
> 7. Request for display the top n-plants : **http://127.0.0.1:8000/plant_states**
> 8. Request for filter by state : **http://127.0.0.1:8000/plant_states/?plant_state=AL**
> 9. Request for single plant details : **http://127.0.0.1:8000/plant_states/699**



## Steps to build the Docker(if it's not build)
>  Build the Docker container by using:   **docker-compose build**

## Screenshot

### 1. **Login Page**

![admin_login](/uploads/ae63c2a3e2d15b7f39bc17edbb9a1153/admin_login.png)



### 2. **Returning all the data of Annual net generation of power plants in US.**


![map](/uploads/002c42f073453443df50f5d5e88fca97/map.png)


### 3. **Returning the data of top n-plants**

![n-plant_states](/uploads/a048bc9377bbf74b0d2703384c5d252a/n-plant_states.png)

### 4. **Returning the data filter by state**

![filter_by_state](/uploads/8ec4fcd886c253368a01c4ee1195ade5/filter_by_state.png)



### 5. **Returning the data of single plant details**

![single_plant_details](/uploads/775ccc6039fd8794bf95ebfeaeea5871/single_plant_details.png)

### 6. **Pagination**

![pagination](/uploads/3ff892b8f31017b4a33a281d06d64282/pagination.png)


### 7. **MAP of the annual net generation of power plants in the US.**

![visualize_map](/uploads/952caced461f121d39532ac6269bb00f/visualize_map.png)

## Screen Record 

![Untitled__1___1_](/uploads/6436757e9b54f9b417a77e3f1ab0e275/Untitled__1___1_.mp4)

## AWS deployment  

### Admin : **http://ec2-13-126-248-147.ap-south-1.compute.amazonaws.com/admin_login/**

      >> 1. username == ankur
      >> 2. password == 1234

### List of MAP Data: **http://ec2-13-126-248-147.ap-south-1.compute.amazonaws.com/plant_states/**

### Top N-Plant data : **use the map data link with /states/?limit=20&offset=0&ordering=-annual_net_gen&plant_state=AK**

### Filter by state: **/?plant_state=AK**

### Single Plant details: **/656/**



## Thank You


