# Project to deploy Microservices using Docker, ECS on Fargate & ALB
## Summary: 
This project is to demonstrate how we can deploy a simple microservices onto AWS ECS which can be assessed over the internet. Microservices are built using Python with Flask framework, implementing a RESTful API architecture and an Nginx Webserver. All the codes are provided in the Github page. 

![MicroserviceECS-Final](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/b1dad4d0-adc4-4389-b83e-18aa9fec4a22)

The end user will access a webpage running on an Nginx Webserver which is hosted on an ECS container attached to an ALB. If the user chooses to generate a random number, then it will invoke a GET API endpoint running on an ECS Container hosted in the same ECS Cluster as the Nginx Webserver. If the user chooses to generate a random number by providing a range, then it will invoke a POST API endpoint running on another ECS Container hosted in the same ECS Cluster.  
 
This project will involve 5 sections. 

Section 1: Launch an EC2 instance with Linux AMI that will host your Docker.  
Section 2: Build Docker images for API Endpoints and push them into an ECR repository.  
Section 3: Launch the ECS Containers to host the API Endpoint services and attach an ALB to them.  
Section 4: Testing the output.   

## Detailed Procedure 
### Section1: Launch an EC2 instance with Linux AMI that will host your Docker.  

1.	Launch an EC2 instance with Linux AMI and install Docker on it. For details on how to, please refer to this github link.

### Section 2: Build Docker images for the API Endpoints and push them into an ECR repository.

2.	After logging into your EC2 instance,create a directory by the name Project and two subdirectories under it by the name GET and POST. Copy the respective files to each of the directories like its listed in the below screenshot.
![1-Displaying directories](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/5b09b121-074e-48e0-a94d-fa0d4a608153)

3. Navigate to GET directory and run the command **docker build -t <image-name> .** to create the image for Get container.  After the image is created you can run the command **docker images** to list the image created. Navigate to POST directory and do the same to create docker image for the post container.
![2-Docker Build](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/5e66c8f0-d7d8-4cf1-81f1-0eab98427c64)

4. After that go to your ECR repository page on your AWS console click on view push commands(Red Arrow from the below screenshot). Inside the Push commands page copy the first command under use the AWS CLI(Black Arrow) and paste it on the EC2 command prompt. After you run the command you should see a Login Succeeded message. Next copy the third command(Green Arrow) and paste it on the EC2 command prompt. This will tag the image which you created in step 3. FInally copy the fourth command(Green Arrow) and paste it on the EC2 command prompt. This will push the image onto your ECR repository.
![4-Docker push to ECR](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/7709ce23-cec8-423a-8a08-6eaf82fcda2a)



