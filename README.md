# Server Health Monitor — Robot Framework

![Python](https://img.shields.io/badge/Python-3.10-blue)

A beginner-friendly automated server health monitoring project built with **Robot Framework** and **Python**. Tests CPU, memory, and disk usage across multiple servers using mock data — no real servers required.

---

## What This Project Does

This project uses Robot Framework to automatically run health checks against a set of servers and report whether each one is operating within safe thresholds. It was built as an introduction to test automation concepts including:

- Writing readable, keyword-driven test cases in `.robot` files
- Building reusable Python keyword libraries
- Organizing test data separately from test logic
- Running automated tests from the command line and reading HTML reports

---

## 📁 Project Structure

```
PythonProject1/
├── data/
│   └── mock_servers.json        # Mock server metrics (cpu, memory, disk)
├── resources/
│   └── server_keywords.py       # Python functions exposed as Robot keywords
├── tests/
│   └── server_health.robot      # Robot Framework test cases
├── results/
│   ├── log.html                 # Detailed test log (auto-generated)
│   └── report.html              # Test summary report (auto-generated)
└── README.md
```

---

## How Robot Framework Is Used

### Keywords (`resources/server_keywords.py`)
Custom Python functions are exposed as **Robot Framework keywords**. Each function checks one health metric for a given server IP and returns `True` (healthy) or `False` (unhealthy):

```python
def check_cpu_usage(server_ip, threshold=80):
    cpu = _get_mock_server(server_ip)['cpu']
    return cpu < threshold
```

### Test Cases (`tests/server_health.robot`)
Robot Framework test cases call these keywords in plain English-style syntax:

```robot
Check All Servers Memory
    ${servers}=    Get Servers From JSON
    FOR    ${srv}    IN    @{servers}
        ${mem_ok}=    Check Memory Usage    ${srv['ip']}
        Should Be True    ${mem_ok}    Memory usage too high on ${srv['name']}
    END
```

### Mock Data (`data/mock_servers.json`)
Server metrics are stored in a JSON file, making it easy to simulate different scenarios without needing real infrastructure:

```json
{
  "servers": [
    { "name": "web-server-01", "ip": "192.168.1.10", "cpu": 45, "memory": 62, "disk": 55 },
    { "name": "db-server-01",  "ip": "192.168.1.20", "cpu": 72, "memory": 87, "disk": 40 },
    { "name": "backup-server-01", "ip": "192.168.1.30", "cpu": 10, "memory": 30, "disk": 95 }
  ]
}
```

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/PythonProject1.git
cd PythonProject1
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install robotframework psutil
```

---

## Running the Tests

```bash
robot tests/server_health.robot
```

To save results to a specific folder:
```bash
robot --outputdir results tests/server_health.robot
```

Then open `results/report.html` in your browser to view the full test report.

---

## Expected Results

| Server | CPU | Memory | Disk | Result |
|---|---|---|---|---|
| web-server-01 | 45% | 62% | 55% | ✅ All checks pass |
| db-server-01 | 72% | 87% | 40% | ❌ Memory exceeds 80% threshold |
| backup-server-01 | 10% | 30% | 95% | ❌ Disk exceeds 90% threshold |

The failures are **intentional** — they demonstrate the monitoring system correctly detecting servers that need attention.

---

## Technologies Used

- [Robot Framework](https://robotframework.org/) — keyword-driven test automation
- [Python 3](https://www.python.org/) — custom keyword library
- [psutil](https://github.com/giampaolo/psutil) — system metrics library (used in live mode)
- JSON — mock server data storage
