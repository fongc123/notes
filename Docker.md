# Docker
## Quick Commands
-   `docker version`
-   `docker build -t <container-name> .`
-   `docker build -f <project_dir>/Dockerfile -t <container-name> .`
-   `pip list --format=freeze > requirements.txt`
-   `docker run <container-name>`
-   `aws lightsail push-container-image --region <Region> --service-name <ContainerServiceName> --label <ContainerImageLabel> --image <LocalContainerImageName>:<ImageTag>`

## What is Docker?
**Docker** is a framework that is used to **containerize and deploy** applications. Each container must have all the dependencies, configurations, scripts, etc. to accomplish a specific task (i.e., run a program). Docker is useful when there are multiple projects each requiring their own dependencies and versions.

Docker containers are similar to virutal machines in that they host programs. However, Docker containers run on the same operating system, while virtual machines create new operating systems. As such, Docker containers are less resource intensive.

## Docker Implementation

### Install Docker
1.  Go to [https://www.docker.com/get-started/](https://www.docker.com/get-started/) to download Docker.
    1.  For Windows systems, make sure that:
        1.  Hyper-V and Containers Windows features are enabled (_enter BIOS to change settings_)
        2.  Install any incomplete requirements (WSL 2 Linux Kernel)
2.  Run `docker version` in the command line to verify that the installation is complete.

### Create a Workflow Process

1.  Create a program (what you want to achieve).
2.  Establish the instructions and requirements to run the program. For example:
    1.  Programming language (i.e., JavaScript, Python)
    2.  Third-party libraries
    3.  Other files
3.  Containerize the program with Docker.

## Create a Dockerfile

A **Dockerfile** is an image (a set of instructions) that tells Docker how to set up the container. Instead of having to figure out the requirements and running the program individually, the entire container can then be simply run with `docker run <container-name>`.

### Instructions & Guidelines

1.  Create a Dockerfile in the program's directory.
2.  Navigate to the directory.
3.  Build the Docker image with `docker build -t <container-name> .`
    1.  `.` represents the path. As we should be in the same directory as the program directory, `.` should suffice.
4.  Run the image with `docker run <container-name>` .

### Keywords

Here are some keywords found in a Dockerfile.
|   **Keyword**   | **Description**                      |
|:---------------:| ------------------------------------ |
|     `FROM`      | Denote the source image              |
|  `COPY <dir>`   | Copy the files in the directory      |
| `WORKDIR <dir>` | Change the current working directory |
| `RUN <command>` | Run a command                        |
| `CMD <command>` | Execute a command                    |

## A Sample Dockerfile
A Docker file and the corresponding JavaScript program to run is shown below.

```dockerfile
# filename: Dockerfile
# sample Dockerfile that runs "app.js"

FROM node:alpine

COPY . /app

WORKDIR /app

CMD node app.js
```

```js
// filename: app.js
// sample program to containerize

console.log("hello");
```

## Another Sample Dockerfile
A Dockerfile and the corresponding Python program is shown below.

```dockerfile
# filename: Dockerfile
# sample Dockerfile that runs "hello.py"

FROM python:3 # use python:2 for Python 2

COPY . .

CMD python hello.py
```

```python
# filename: hello.py

print('hello')
```

## Changing Build COntexts
To include files outside of the current directory, we need to build the Docker image from a certain directory such that all files can be accessible. Consider the following file structure.

```
projects
|---<other projects>...
|---utils
    |---utils.py
    |---config.json
|---my_project
    |---main.py
    |---Dockerfile
```

`main.py` uses functions that are in a different directory (`../utils`). The Docker image must be built from the `projects` directory. Accordingly, the Docker file must be changed to incorporate this change.

```dockerfile
# filename: Dockerfile
COPY utils /app/utils
COPY my_project /app/my_project
```

Once in the `projects` directory, the Docker command that must be run is: `docker build -f my_project/Dockerfile -t <container-name> .` . Note that `.` is used again, as the build context is the `projects` directory.

## Docker Hub

### Pushing Docker Images

Dockerfiles can be uploaded to Docker Hub, allowing Docker images to be run anywhere. The following steps show how to upload an image to a repository under your account.

### Instruction & Guidelines

1.  Create a Docker account on [https://hub.docker.com/](https://hub.docker.com/).
2.  Create a repository under your account. Set it to private if necessary.
3.  Tag the image under your account with `docker tag <image_ID> <username>/<name>`.
    1.  You may need to **log out** and **log in** before performing this step.
    2.  The image ID can be found in `docker image ls`.
    3.  Example:
        1.  Docker image ID built: `9ac23fe32bb8`
        2.  Docker username: `midas`
        3.  Command line to run: `docker tag 9ac23fe32bb8 midas/docker-test`
4.  Push the image with the new tag with `docker push <username>/<name>`.
5.  Pull the image from another machine with `docker pull <username>/<name>`.
    1.  You may need to **log in** before performing this step.

## Notes
-   You can try Docker out using the _Getting Started_ Docker image, which is included in the download.
-   Docker images are _magically_ stored locally on the machine. Run `docker image ls` to list all images.
-   Logging into and out of Docker through the command line:
    -   Log in: `docker login`
    -   Log out: `docker logout`
- For Visual Studio Code users, you can download the Docker extension from the Marketplace!
-   Find source images on [https://hub.docker.com/](https://hub.docker.com/).
-   Docker eats up a lot of space! Run `docker system prune` to free up some space.
-   Docker Hub: registry/storage in the cloud for Docker images (similar to Git and GitHub)
    -   Don't actually upload it, though, unless you want everyone to see it. Ensure that you upload it to a private Docker repository by setting the repository to private.

# External References

Here are some external references I found useful:

-   Stack Overflow: Request denied when pushing to Docker Hub ([https://stackoverflow.com/questions/41984399/denied-requested-access-to-the-resource-is-denied-docker](https://stackoverflow.com/questions/41984399/denied-requested-access-to-the-resource-is-denied-docker))
-   Stack Overflow: Difference between `RUN` and `CMD` in a Dockerfile ([https://stackoverflow.com/questions/37461868/difference-between-run-and-cmd-in-a-dockerfile](https://stackoverflow.com/questions/37461868/difference-between-run-and-cmd-in-a-dockerfile))
-   Stack Overflow: Get `requirements.txt` for `pip` from `conda` ([https://stackoverflow.com/questions/50777849/from-conda-create-requirements-txt-for-pip3](https://stackoverflow.com/questions/50777849/from-conda-create-requirements-txt-for-pip3)) (`pip freeze > requirements.txt` or `pip list --format=freeze > requirements.txt`)
- Stack Overflow: Launching Selenium in Docker (a Linux system) ([https://stackoverflow.com/questions/22424737/unknown-error-chrome-failed-to-start-exited-abnormally](https://stackoverflow.com/questions/22424737/unknown-error-chrome-failed-to-start-exited-abnormally))

