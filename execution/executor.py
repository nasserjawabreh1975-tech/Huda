import subprocess

print("[EXECUTION ENGINE ONLINE]")

while True:

    cmd = input("HUDA> ")

    if cmd == "exit":
        break

    subprocess.run(cmd,shell=True)
