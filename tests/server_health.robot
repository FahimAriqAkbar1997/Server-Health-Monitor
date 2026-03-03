*** Settings ***
Library    ../resources/server_keywords.py
Library    Collections
Library    OperatingSystem

*** Variables ***
${MOCK_FILE}    data/mock_servers.json

*** Keywords ***
Get Servers From JSON
    ${json_str}=    Get File    ${MOCK_FILE}
    ${json}=        Evaluate    __import__('json').loads('''${json_str}''')
    ${servers}=     Get From Dictionary    ${json}    servers
    RETURN          ${servers}

*** Test Cases ***
Check All Servers CPU
    ${servers}=    Get Servers From JSON
    FOR    ${srv}    IN    @{servers}
        ${cpu_ok}=    Check CPU Usage    ${srv['ip']}
        Should Be True    ${cpu_ok}    CPU usage too high on ${srv['name']}
    END

Check All Servers Memory
    ${servers}=    Get Servers From JSON
    FOR    ${srv}    IN    @{servers}
        ${mem_ok}=    Check Memory Usage    ${srv['ip']}
        Should Be True    ${mem_ok}    Memory usage too high on ${srv['name']}
    END

Check All Servers Disk
    ${servers}=    Get Servers From JSON
    FOR    ${srv}    IN    @{servers}
        ${disk_ok}=    Check Disk Usage    ${srv['ip']}
        Should Be True    ${disk_ok}    Disk usage too high on ${srv['name']}
    END