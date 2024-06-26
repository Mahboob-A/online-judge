
## Licence 

[![Repo](https://img.shields.io/badge/https%3A%2F%2Fgithub.com%2FMahboob-A%2Fonline-judge
)](https://github.com/Mahboob-A/online-judge)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


# Online Judge - RCE Engine 

Online Judge is an RCE Engine for coding platform like LeetCode, Hackerrank. 

Online Judge can execute C++, Python and Java code in secure container, compare code output with testcases and return appropriate response to the client. 







## General Information

Online Judge is an experiment to implement the Judge with [AlgoCode](https://github.com/Mahboob-A/algocode-backend) Platform a DSA platfrom just like Leetcode. 

AlgoCode is a coding platfrom built in microservices architechture. To learn more about AlgoCode, please explore this repository: 
[AlgoCode Backend](https://github.com/Mahboob-A/algocode-backend)

Online Judge can execute user codes and run test cases against the code output. 

The Judge can handle the below events: 

    a. AC (Accepted) 
    b. WA (Wrong Answer)
    c. Compilation Error 
    d. Time Limit Exceed 
    e. Memory Limit Exceed 
    f. Segmentation Fault

*The Online Judge is a pure docker implementation and no other 3rd party API or service has been used.*





## Run Locally

#### Clone the project

```bash
  https://github.com/Mahboob-A/online-judge.git
```

#### Go to the project directory

```bash
  cd src 
```

#### Create a virtual environment 
For Linux/MacOS
```bash 
  python3 -m venv venv
```

For Windows 
```bash 
  python -m venv venv
```

#### Activate the virtual environment 
For Linux/MacOS
```bash 
  . venv/bin/activate
```

For Windows 
```bash 
  .\env\Scripts\activate.bat
```

#### Install the dependencies 
```bash 
  python -r requirements/dev.txt 
``` 

#### Create the docker image 

**You must creat the below image and volume in order to run the Judge successfully.**

Go the the path to Dockerfile 

```bash
  cd docker/lang/cpp
```
Run the command to create the required images 
```baah
  docker build -t algocode/revamped-cpp:v1 . 
```
Make sure to add the "dot" at the end of the line. 


#### Create the docker volume 
The main Judge Container and the Sibling Containers use a Volume to 
share data between them.

Run the command to create the desired volume: 
```bash 
  docker volume create user_code_files
``` 

You need to create the volume as this volume will be managed 
externally. 


#### Run the Judge 
Return to the `src` directory, and then run the bellow command to start the Judge. It will also run the development server. 

For Linux/MacOS 
```bash 
  make docker-up 
```

For Windows
```bash 
  docker compose -f dev.yml up --build -d --remove-orphans
```

Now you are ready to send request to the API asper API reference below. Wait for 5 seconds to propage the Judge before sending a request. 


#### Stop the Judge
To stop the Judge, run the below command. 

For Linux/MacOS 
```bash
  make docker-down
```

For Windows
```bash
  docker compose -f dev.yml down
```


## API Reference

#### Submit Code for Execution 

```http
  POST /submit/execute-robust/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `lang`    | `string` | **Required**. The language of the Code. Currently only `cpp` is available.  |
| `code`    | `string` | **Required**. The C++ code you want to execute.|
| `input`   | `list[string]` | Input for the program. Empty if no input is neeed. | 
| `testcase` | `list[string]` | Testcase that should be compared to check th e answer of the code execution. |   


All the code are pushed to the project as PR. Hence, you can view the work has been done in the closed PR of the project. Detailed explanation has been added to understand the PR. To learn more on API, please take a look at this PR: [Judge API](https://github.com/Mahboob-A/online-judge/pull/6)


## Judge Without API Call

If you are just curious to test it locally without calling any API, 
you can also do that. 

Follow the below steps - 

A. Clone This repository: [Judge without API Call](https://github.com/Mahboob-A/online-judge/tree/check-dnd-local)

B. A step by step guideline has been outlined in the below mentioned PR, please follow along the PR to run the Judge without calling the API: [See the PR.](https://github.com/Mahboob-A/online-judge/pull/9) It's really well documented, I promise!




## Troubleshoot

If the Judge is not responsive, you can stop and restart the Judge using the commands mentioned in the Run Locally section. 

If this didn't help, stop the Judge, go to `src/core_apps/judge_engine/containers.py`, add a print statement on `logs` and `status_code` after `line number 170 and 171`. 

Run the Judge, and notedown the container ID using: `docker ps`. 

Run `docker logs -f <container ID>` 

And you will be able to see the Judge container's development server's output in your terminal. 

## FAQ

#### What is the backend for this project 

The backend of this project is implemented with Django. 

#### Language

Python 

#### Why testcases and input are being passed from client 
This is a Revamped Implementation of Online Judge for AlgoCode - A DSA problem solving platform implemented in microservices architecture just like Leetcode.  

This Judge simplifies to the code execution. If you just want a monolithic application to test how an secure code execution should happend with test cases comparison to generate a DSA platform like answer, this is a handy tool. 

This Judge is implemented in the [Remote Code Execution Engine](https://github.com/Mahboob-A/rcee) Service of the [AlgoCode](https://github.com/Mahboob-A/algocode-backend) Platform. 


#### How secure is the execution 
The C++ code will be executed in a secure docker container. The container has no privileges and all other possible privileges has been dropped.

The container can handle any kind of `DoS Attack` like `fork bomb` and any other form of resource starvation attack. 

A new sibling container is spawn to execute the code.

As the container is auto terminated within `5 seconds`, and only allocated `.5 cpu`, `300mb` of RAM with no `swap` available, hard limit of `nproc` is set to `50` and hard limit of `nofile` set to `50`, 
it can not run any heavily `process` or `descriptor` oriented tasks. 

However, you can tweak the settings as per you need as well. 

#### Why only C++ can be executed 
The main AlgoCode platform is able to rub Python, C++ and Java code. However, This RCE engine will also be updated as I continiously develope the AlgoCode. 

In future updtes, Python and Java execution will be added. 

If you need immediate support of these languages, please do not hesitate to connect with me at: [connect.mahboobalam\@gmail.com](mailto:connect.mahboobalam@gmail.com?subject=OnlineJudge)
## Future Improvements 
Spawning new container and stop it and cleaning it is expensive process. Hence I am planning to optimize this use case and if the below are achieable, I will bring them in my future rolling of the Juddging engine. 

#### Explore the BOTEK Estimation 
As creating new contianers and deleting them are expensive process, maintain the container's state and execute the code in the contianer without stopping or closing them. 

As the image of the container is very lightweight, we might be able to run concurrent `100+ containers` with `64 GB of RAM`, and `2 Core CPU`.   

But the overhead here is not the number of containers, the overhead is networking and the bigger overhead is disk seek, as the judge needs to write the necessary files to the disk in order to mount it with the container, and again, delete them after the execution is successful. 

#### The Optimation 
If we constantly run 100+ contianers as per our above estimation, and we mount the user files directory dynamically before the code is executed, we can really mitigate almost `1.5/1.0 seconds of cold start` of the docker container. 

In this design, we can increase the speed and efficiency of a `Synchronous` backend like Django and it would able to handle more concurrent requests with less time. 


#### My Plan 
Yes, I will implement this in my next release. In the future release, the Online Judge RCE Engine will be faster and mitigate the cold start of the docker container.  
## Screenshots

#### API requst in postman
![image](https://github.com/Mahboob-A/online-judge/assets/109282492/dc23de2c-4ffb-4302-a307-dbb2e06b4d5a)



##### Wrong Answer Response 
![Screenshot from 2024-05-22 12-27-58](https://github.com/Mahboob-A/online-judge/assets/109282492/a9a242b5-d22a-406e-9016-0ee351dc00a8)

##### Logging Level 
![Screenshot from 2024-05-22 12-28-42](https://github.com/Mahboob-A/online-judge/assets/109282492/9e6dd81a-f999-4ce8-86c7-a29cda510bc2)

##### The architechture of [AlgoCode](https://github.com/Mahboob-A/algocode-backend) Platform.  
![Screenshot from 2024-05-21 13-22-07](https://github.com/Mahboob-A/online-judge/assets/109282492/96c4cda4-388f-417b-8f35-1bc75c0ed015)
## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/i-mahboob-alam/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/iMahboob_A)
