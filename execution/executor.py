import subprocess

print("[EXECUTION ENGINE ONLINE]")

while True:

    cmd=input("HUDA> ")

    if cmd=="exit":
        break

    result=subprocess.getoutput(cmd)

    print(result)
