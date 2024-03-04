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
### Section 1: Launch an EC2 instance with Linux AMI that will host your Docker.  

1.	Launch an EC2 instance with Linux AMI and install Docker on it. For details on how to, please refer to this github link.

### Section 2: Build Docker images for the API Endpoints and push them into an ECR repository.

2.	After logging into your EC2 instance,create a directory by the name Project and two subdirectories under it by the name GET and POST. Copy the respective files to each of the directories like its listed in the below screenshot.
![1-Displaying directories](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/5b09b121-074e-48e0-a94d-fa0d4a608153)

3. Navigate to GET directory and run the command **docker build -t <image-name> .** to create the image for Get container.  After the image is created you can run the command **docker images** to list the image created. Navigate to POST directory and do the same to create docker image for the post container.
![2-Docker Build](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/5e66c8f0-d7d8-4cf1-81f1-0eab98427c64)

4. After that go to your ECR repository page on your AWS console click on view push commands(Red Arrow from the below screenshot). Inside the Push commands page copy the first command under use the AWS CLI(Black Arrow) and paste it on the EC2 command prompt. After you run the command you should see a Login Succeeded message. Next copy the third command(Green Arrow) and paste it on the EC2 command prompt. This will tag the image which you created in step 3. FInally copy the fourth command(Green Arrow) and paste it on the EC2 command prompt. This will push the image onto your ECR repository.Once done click on the refresh button and you will be able to see the pushed image inside the repo(Yellow Arrow)
![3-ECR-Docker commands](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/5d53307b-5117-470f-8b5e-a30fc64a7624)
![4-Docker push to ECR](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/c9cc3dff-66e3-48e9-9561-1fc90e21942e)

### Section 3: Launch the ECS Containers to host the API Endpoint services and attach an ALB to them.  
5. Navigate to ECS page on the console and click on Task definitions (Red Arrow from the screenshot below) and create new task definition. Give a name for the Task definition family(Black Arrow) and select AWS Fargate as the launch type(Green Arrow).
![6-Task Definition 1](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/1c8cced1-8f2f-49d6-8113-ec69798ebda4)  

6. Give a name for the container (Red Arrow) and copy the image URI from the ECR repository (Green Arrow) and paste it in the image URI box (Black Arrow). Select the Container port as 80 and leave all the other options as it is. Click on the Create button at the page (Blue Arrow).  
![6-Task Definition 2](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/b74f4c14-0284-47f9-9454-7416cc4bd3e9)

7. Go back to the ECS page and click on Create Cluster button. Inside the Create Cluster page, give a name for the cluster and choose AWS Fargate as the infrastructure. Then click on the Create button at the bottom of the page (Red Arrow).  
![5-Creating ECS Cluster](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/aa8fd1c2-46df-4773-9ac4-b48b3b1b777a)

8. Once the cluster is created, go to the Services tab (Red Arrow from the screenshot below) and click on Create button. Under Application type choose the Service option. Under Task definition, select the Task definition which was created under Step 6. Give a Service Name and select the desired tasks as 3(Black Arrow).
9. ![7-Create Service 1](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/6d436ea9-613e-440c-b5cd-7e3dbc617ac8)

10. Under Networking select default VPC and select 2 availability zones. Create a new security group for outside traffic to access the container. Give the inbound rules like its shown in the below screenshot. And then click on the Create button at the bottom of the page(Red Arrow).  
![8-Create Service 2](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/75030b3a-977b-4925-a584-8b8aa33e7f07)

11. Next expand the Load Balancing – optional section. Choose Application Load Balancer as the Load Balancer type and then click on Create a new load balancer (Red Arrow from the below screenshot). Give a name for the Load balancer. Select ‘Create new listener’ (Black Arrow) and select Port 80 and HTTP protocol. Select ‘Create new target group’ and give a name to the Target group. Under ‘Health check path’(Green Arrow), give the same end point you have given in the Flask app which is /get in this case.  
![9-Load Balancer](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/397cf191-17ca-445d-abe0-993266fb1424)

12. Repeat step 3 to 10 for the POST method also. Make sure the Post service is also created inside the same ECS cluster. 

### Section 4: Testing the output.   

12. To test the output, you will need the tool Postman installed on your system. You can test the GET method through a browser as well. Go to your Load Balancers page and copy the DNS name (Red Arrow from the below screenshot). Open your Postman tool and select GET from the dropdown on the left(Black Arrow) and paste the ALB URL with a slash at the end, followed by the API endpoint which is /get in this case (Blue Arrow).Then click on the Send button and you will see a random number below 10 (Green Arrow) each time you click on it.  
![10-Test Get](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/a8c05ef0-ad3d-4dd6-b0bb-5983d3b21aca)

13. You cannot test the POST method through a browser hence you will need Postman installed. Go to your Load Balancers page for Post and copy the DNS name (Red Arrow from the below screenshot). Open your Postman tool and select POST from the dropdown on the left (Black Arrow) and paste the ALB URL with a slash at the end, followed by the API endpoint which is /post in this case. Under ‘Body’ tab (Yellow Arrow), select JSON(Green Arrow) .Make sure you pass the JSON input with the same variables you have provided in your POST Flask app which is ‘min’ and ‘max’ in this case. Give the range of numbers from which you want to generate a random number. Then click on the Send button and you will see a random number between the range you have provided each time.  
![11-Test Post](https://github.com/vmk81/Microservices-with-ECS/assets/157844406/343977f5-5a64-4a9e-81d8-77b78707ff50)











