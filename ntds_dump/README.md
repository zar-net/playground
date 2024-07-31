# NTDS.dit Parser Scripts

## Description
I needed to do some quick parsing of an NTDS.dit file to get the NT hashes today for an exploit as well as details for a report. I threw together some Python code and then thought it would be a good
exercise to build out the script a bit more (for fun) and do a Rosetta Stone approach; covering three languages. These scripts are designed to parse NTDS.dit data extracted using tools like Invoke-DCSync 
in PowerShell. The scripts can output the parsed data into a CSV file with headers or list NT hashes only.

## Files

- `parse_ntds.sh`: A Bash script to parse NTDS.dit data.
- `parse_ntds.py`: A Python script to parse NTDS.dit data.
- `parse_ntds.ps1`: A PowerShell script to parse NTDS.dit data.
- `README.md`: This file.

## Usage

### Bash Script

To parse the NTDS.dit data into a CSV file:
```bash
./parse_ntds.sh -c inputfile.txt
```
To list NT hashes only:
```bash
./parse_ntds.sh -nt inputfile.txt
```

### Python Script
To parse the NTDS.dit data into a CSV file:

```bash
python parse_ntds.py -c inputfile.txt
```
To list NT hashes only:

```
python parse_ntds.py -nt inputfile.txt
```

### PowerShell Script
To parse the NTDS.dit data into a CSV file:

```
.\parse_ntds.ps1 -Option -c -InputFile inputfile.txt
```

To list NT hashes only:

```
.\parse_ntds.ps1 -Option -nt -InputFile inputfile.txt
```

## Definition of NTDS Content
The NTDS.dit file is a database that stores Active Directory data, including user account information and password hashes. Each line typically contains the following fields separated by colons (:):

- **Username:** The name of the user.
- **RID:** Relative Identifier, a unique identifier for the user within the domain.
- **LM Hash:** The Lan Manager hash of the user's password (usually empty or placeholder if LM hashing is disabled).
- **NT Hash:** The NT hash of the user's password.

### Example

```
John Smith:1001:AAD3B435B51404EEAAD3B435B51404EE:E52CAC67419A9A22A47E1519D1E8A70C:::
Jane Doe:1002:AAD3B435B51404EEAAD3B435B51404EE:C27AD7E6842A1A22C2B7B7A4B8E7A6A4:::
```
## Handling Issues
If an error occurs because the execution policy on your system is set to prevent the running of unsigned scripts, use the following steps:

```
# Open PowerShell as Administrator
# Check current execution policy
Get-ExecutionPolicy

# Temporarily set execution policy to Bypass
Set-ExecutionPolicy Bypass -Scope Process

# Run the script
.\parse_ntds.ps1 -Option -c -InputFile inputfile.txt

# Revert execution policy (if needed)
Set-ExecutionPolicy Restricted -Scope Process
```
