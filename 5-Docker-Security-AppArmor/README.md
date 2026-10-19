# Assignment 5: Docker Security with AppArmor

## Objective
To secure a Dockerized Flask application using an AppArmor security profile and automate container management using the Python Docker SDK.

## Project Files
- `app.py` — Flask web application running on port 5000.
- `Dockerfile` — Builds the Flask application image.
- `my-apparmor-profile` — AppArmor profile provided for the assignment.
- `apply_apparmor.py` — Builds the image, starts a container with the requested security option, and inspects its configuration.
- `test_restricted_actions.py` — Tests file access and command execution inside the container.
- `screenshots/` — Evidence of the application and security tests.

## Implementation

### 1. Build the Docker Image
```bash
docker build -t flask-apparmor .
```

### 2. Run the Flask Application
```bash
docker run -d --name flask-apparmor-test -p 5000:5000 flask-apparmor
```

Open `http://localhost:5000/` in a browser or test it with:
```bash
curl http://localhost:5000/
```

### 3. AppArmor Profile
The profile specifies restrictions for access to `/etc` and `/var`, execution of binaries, and system capabilities. It also specifies network access and permissions for `/app`.

### 4. Python Docker SDK
Install the SDK in a Python virtual environment:
```bash
python -m pip install docker
```

Run the automation and restriction tests:
```bash
python apply_apparmor.py
python test_restricted_actions.py
```

## Observed Results
- The Flask application returned HTTP 200.
- The Python automation built the image and recorded `apparmor=my-apparmor-profile` in the container security options.
- The restriction tests returned exit code `0` for reading `/etc/passwd` and executing `/bin/bash`. These actions were not blocked.
- `aa-status` reported that the AppArmor module was loaded but the AppArmor filesystem was not mounted.
- Docker's security options did not advertise AppArmor support.

## Environment Limitation
The environment recorded the requested AppArmor security option, but actual enforcement was not verified. The restriction tests did not produce the expected denials. Therefore, these results must not be interpreted as proof that the profile is enforcing the intended restrictions. A compatible Linux environment with AppArmor enabled and mounted is needed to verify enforcement.

## Viva Questions

**1. What is AppArmor?**  
AppArmor is a Linux security module that confines applications according to defined security policies.

**2. How do AppArmor profiles improve container security?**  
They can restrict file access, executable permissions, network operations, and capabilities.

**3. Why restrict access to `/etc` and `/var`?**  
To reduce access to sensitive configuration and system data.

**4. How can the requested security option be inspected?**  
Use `docker inspect` to examine `HostConfig.SecurityOpt`. This confirms the recorded option, not enforcement.

**5. What did the restriction tests show?**  
Both commands succeeded, so the expected restrictions were not demonstrated in the current environment.
