
import docker

client = docker.from_env()

try:
    client.images.build(path=".", tag="flask-apparmor")
    print("Docker image built successfully.")

    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5002},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    container_info = client.api.inspect_container(container.id)
    apparmor_profile = container_info["HostConfig"]["SecurityOpt"]

    print(f"Requested security options: {apparmor_profile}")
    print("Note: Recorded options do not prove AppArmor enforcement.")

finally:
    if "container" in locals():
        container.stop()
        container.remove()
        print("Test container stopped and removed.")
