# Server Health Monitor — Robot Framework

A beginner-friendly automated server health monitoring project built with Robot Framework and Python. Tests CPU, memory, and disk usage across multiple servers using mock data — no real servers required.

📋 What This Project Does
This project uses Robot Framework to automatically run health checks against a set of servers and report whether each one is operating within safe thresholds. It was built as an introduction to test automation concepts including:

Writing readable, keyword-driven test cases in .robot files
Building reusable Python keyword libraries
Organizing test data separately from test logic
Running automated tests from the command line and reading HTML reports

# How Robot Framework Is Used
Keywords (resources/server_keywords.py)
Custom Python functions are exposed as Robot Framework keywords. Each function checks one health metric for a given server IP and returns True (healthy) or False (unhealthy):
pythondef check_cpu_usage(server_ip, threshold=80):
    cpu = _get_mock_server(server_ip)['cpu']
    return cpu < threshold
Test Cases (tests/server_health.robot)
Robot Framework test cases call these keywords in plain English-style syntax:
robotCheck All Servers Memory
    ${servers}=    Get Servers From JSON
    FOR    ${srv}    IN    @{servers}
        ${mem_ok}=    Check Memory Usage    ${srv['ip']}
        Should Be True    ${mem_ok}    Memory usage too high on ${srv['name']}
    END
Mock Data (data/mock_servers.json)
Server metrics are stored in a JSON file, making it easy to simulate different scenarios without needing real infrastructure:
json{
  "servers": [
    { "name": "web-server-01", "ip": "192.168.1.10", "cpu": 45, "memory": 62, "disk": 55 },
    { "name": "db-server-01",  "ip": "192.168.1.20", "cpu": 72, "memory": 87, "disk": 40 },
    { "name": "backup-server-01", "ip": "192.168.1.30", "cpu": 10, "memory": 30, "disk": 95 }
  ]
}

# Setup & Installation
1. Clone the repository
bashgit clone https://github.com/YOUR_USERNAME/PythonProject1.git
cd PythonProject1
2. Create and activate a virtual environment
bashpython -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
3. Install dependencies
bashpip install robotframework psutil

# Running the Tests
bashrobot tests/server_health.robot
To save results to a specific folder:
bashrobot --outputdir results tests/server_health.robot
Then open results/report.html in your browser to view the full test report.

# Expected Results
ServerCPUMemoryDiskResultweb-server-0145%62%55%✅ All checks passdb-server-0172%87%40%❌ Memory exceeds 80% thresholdbackup-server-0110%30%95%❌ Disk exceeds 90% threshold
The failures are intentional — they demonstrate the monitoring system correctly detecting servers that need attention.

# Technologies Used

Robot Framework — keyword-driven test automation
Python 3 — custom keyword library
psutil — system metrics library (used in live mode)
JSON — mock server data storage
