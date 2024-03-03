# Project to deploy Microservices using Docker, ECS on Fargate & ALB
Summary: 
This project is to demonstrate how we can deploy a simple microservices onto AWS ECS which can be assessed over the internet. Microservices are built using Python with Flask framework, implementing a RESTful API architecture and an Nginx Webserver. All the codes are provided in the Github page. 

The end user will access a webpage running on an Nginx Webserver which is hosted on an ECS container attached to an ALB. If the user chooses to generate a random number, then it will invoke a GET API endpoint running on an ECS Container hosted in the same ECS Cluster as the Nginx Webserver. If the user chooses to generate a random number by providing a range, then it will invoke a POST API endpoint running on another ECS Container hosted in the same ECS Cluster.  
 
This project will involve 4 sections. 

Section1: Launch an EC2 instance with Linux AMI that will host your Docker.
Section 2: Build Docker images for API Endpoints and push them into an ECR repository.
Section 3: Launch the ECS Containers to host the API Endpoint services and attach an ALB to them.
Section 4: Repeat Section 2 & 3 for the Nginx Webserver with the ALB DNS endpoints added in the HTML page. 
Section 5: Testing the output. 
