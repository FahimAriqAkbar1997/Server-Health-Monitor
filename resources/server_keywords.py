import os
import json
import psutil
from pathlib import Path

USE_MOCK = True

# Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent`
MOCK_FILE = PROJECT_ROOT / 'data' / 'mock_servers.json'

with open(MOCK_FILE, 'r') as f:
    MOCK_SERVERS = json.load(f)['servers']

print(f"Loaded mock data from: {MOCK_FILE}")

def _get_mock_server(ip):
    for srv in MOCK_SERVERS:
        if srv['ip'] == ip:
            return srv
    raise ValueError(f"Server with IP {ip} not found in mock data")

def check_cpu_usage(server_ip):
    if USE_MOCK:
        cpu_percent = _get_mock_server(server_ip)['cpu']
    else:
        cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage for {server_ip}: {cpu_percent}%")
    return cpu_percent < 80

def check_memory_usage(server_ip):
    if USE_MOCK:
        mem_percent = _get_mock_server(server_ip)['memory']
    else:
        mem_percent = psutil.virtual_memory().percent
    print(f"Memory usage for {server_ip}: {mem_percent}%")
    return mem_percent < 80

def check_disk_usage(server_ip):
    if USE_MOCK:
        disk_percent = _get_mock_server(server_ip)['disk']
    else:
        disk_percent = psutil.disk_usage('/').percent
    print(f"Disk usage for {server_ip}: {disk_percent}%")
    return disk_percent < 80