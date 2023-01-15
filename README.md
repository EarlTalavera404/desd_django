# Assignment for DESD


This repository contains a virtual environment ```.venv``` and a folder for the django/docker project, ```web_project```.

# Author
<b> Name : Earl Talavera </b> <br/>
<b> ID : 20004263 </b>

## Prequisites
- Git Bash
- Docker Desktop

---

### Installation on local machine
1. Obtain the http link from the clone git lab repository.
2. Create a new bash shell.
3. Enter a folder and then in the bash shell enter : ```git clone '<http link>' ```

---

### Running the code
1. Enter the cloned repo.
```cmd
C:\Users\earl\Desktop\New folder\DESD_SUB
```
2. In command prompt enter the virtual environment.
```cmd
.venv\Scripts\activate
```
3. Enter the django project directory.
```cmd
(.venv) C:\Users\earl\Desktop\New folder\DESD_SUB>cd web_project

(.venv) C:\Users\earl\Desktop\New folder\DESD_SUB\web_project>
```
4. Before executing docker compuse up -d, ensure that the ```end of line sequence for the uweflix_project-entrypoint.sh``` is ```LF``` as GIT changes it CRLF which causes the docker cointainer to break as it cannot find the file.

5. Execute ```docker compose up -d ```to initialise the docker container.
```cmd
(.venv) C:\Users\earl\Desktop\New folder\DESD_SUB\web_project>docker compose up -d
```

6. Enter ```Docker Desktop``` and open the port in the browser.

---
