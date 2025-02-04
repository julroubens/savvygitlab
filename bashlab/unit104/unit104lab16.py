# We are going to use the psutil command to format a script to check these items.  cpu times, cpu percentatge, disk partion's, users and net connections.  
# You may have to do some extra modification to make the ouput be more readable.


import psutil


# Get CPU times
print("\nCPU Times:")
cpu_times = psutil.cpu_times()
print(f"User: {cpu_times.user:.2f}s")
print(f"System: {cpu_times.system:.2f}s")
print(f"Idle: {cpu_times.idle:.2f}s")

# Get CPU usage percentage
print("\nCPU Usage:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"CPU {i}: {percentage}%")

# Get disk partitions and usage
print("\nDisk Partitions:")
for partition in psutil.disk_partitions():
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"\nDevice: {partition.device}")
        print(f"Mount Point: {partition.mountpoint}")
        print(f"File System Type: {partition.fstype}")
        print(f"Total: {usage.total / (1024**3):.2f} GB")
        print(f"Used: {usage.used / (1024**3):.2f} GB")
        print(f"Free: {usage.free / (1024**3):.2f} GB")
        print(f"Usage: {usage.percent}%")
    except PermissionError:
        continue

# Get users
print("\nConnected Users:")
for user in psutil.users():
    print(f"\nUsername: {user.name}")
    print(f"Terminal: {user.terminal}")
    print(f"Host: {user.host}")
    print(f"Started: {user.started}")

# Get network connections
print("\nNetwork Connections:")
for conn in psutil.net_connections():
    try:
        print(f"\nLocal Address: {conn.laddr.ip}:{conn.laddr.port}")
        if conn.raddr:
            print(f"Remote Address: {conn.raddr.ip}:{conn.raddr.port}")
        print(f"Status: {conn.status}")
        print(f"PID: {conn.pid}")
    except (AttributeError, IndexError):
        continue
