# Emissions & Generation Resource Integrated Database (eGRID) 

**The Purpose of this project to visualize the eGRID database.*Requirements of the project are:**
***
> - We want to show a map to visualize the annual net generation of power plants in the US
> - We want to display the top-n plants
> - We want to be able to filter by state
> - We want to be able to see a single plant's details, including the actual and percentage values of the plants' contribution to its federal state.


**The Stack which are used Python, Django, RESTful API,SQLite3 Pandas, Matplotlib, Nginx.**

Please go through the **Requirements.txt file:https://gitlab.com/ankurpython/power-plant/-/blob/master/requirements.txt** and install all the requirements.

## Required

* Install **the Docker:** **https://docs.docker.com/docker-for-windows/install/ (for Windows) and for other environment https://docs.docker.com/engine/install/**
* **Docker-compose: https://docs.docker.com/compose/install/**

## Steps to Run 
> 1. Download or Clone the Repository:    **https://gitlab.com/ankurpython/power-plant.git**
> 2. Run the container: **sudo docker-compose up**
> 3. Create the superuser using this command Run the: **docker exec -it container_id python manage.py createsuperuser**
> 4. Login with username and password.**http://localhost:8000/admin_login**. This will return the access token.
> 5. Request with Bearer token using this endpoint: **http://localhost:8000/api/v1/quotes**
> 6. For the GET and POST request 

## Steps to build the Docker(if it's not build)
>  Build the Docker container by using:   **docker-compose build**

## Screenshot

### 1. **Login Page**

![login](https://user-images.githubusercontent.com/48859058/137621082-f8131c79-652f-4748-8e3b-675e3ec6b46c.png)



### 2. **Returning all the data through GET request**

![Screenshot from 2021-10-17 12-23-31](https://user-images.githubusercontent.com/48859058/137621357-63d1bc26-e300-4e31-9cda-8c17dd44227b.png)


### 3. **Returning the data through POST request**

![Screenshot from 2021-10-18 10-49-07](https://user-images.githubusercontent.com/48859058/137682291-f660860a-f4e0-45f7-a100-8a8188c285a4.png)

### Screen Record 

https://user-images.githubusercontent.com/48859058/137687459-b6f56a8b-c042-43f3-b814-c906d32320f1.mov







## Thank You


