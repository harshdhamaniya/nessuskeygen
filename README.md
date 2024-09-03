# Nessus Professional Key Generator

This Python script allows you to generate Nessus Professional Keys directly without having to fill out the registration form. It simplifies the process and makes it more convenient for users to get started with Nessus.

### Generate Keys Effortlessly: No installation or setup required—seamlessly generate keys directly through our website, ensuring a smooth and efficient experience. [Click Here](https://harshdhamaniya.com/nessus)

## Updates 23-08-2024

- **Unified Key Generation**: Combined key generation for Nessus Professional and Expert into a single function.
- **Improved Request Handling**: Enhanced management of request fields and response parsing.
- **Debug Output**: Added debug output for better troubleshooting.
- **Simplified User Interface**: Removed redundant functions to streamline user interaction.
- **Updated API URL**: Changed API URL for both Nessus Professional and Expert key generation.

## Usage

https://github.com/harshdhamaniya/nessuskeygen/assets/116166209/b7cee19c-af86-44a7-9a55-4e8ce094a949

To generate a Nessus Professional Key using the script, simply run the following command:

```bash
python nessuskeygen.py
```

If you prefer a Windows executable, you can download `nessuskeygen.exe` and click the "Generate Key" button to generate a key.

## Start or Stop Nessus

### Windows Command-Line Operation

Start Nessus:

```
C:\Windows\system32>net start "Tenable Nessus"
```

Stop Nessus:

```
C:\Windows\system32>net stop "Tenable Nessus"
```

### Linux Command-Line Operation

#### RedHat, CentOS, and Oracle Linux

Start Nessus:

```
# systemctl start nessusd
```

Stop Nessus:

```
# systemctl stop nessusd
```

#### SUSE

Start Nessus:

```
# systemctl start nessusd
```

Stop Nessus:

```
# systemctl stop nessusd
```

#### FreeBSD

Start Nessus:

```
# service nessusd start
```

Stop Nessus:

```
# service nessusd stop
```

#### Debian, Kali, and Ubuntu

Start Nessus:

```
# systemctl start nessusd
```

Stop Nessus:

```
# systemctl stop nessusd
```

## Updating the Nessus Key

To update the Nessus key, you can use the following commands:

For all operating systems:

```
nessuscli fix --reset-all
```

### Linux

```
# /opt/nessus/sbin/nessuscli fetch --register xxxx-xxxx-xxxx-xxxx
```

### FreeBSD

```
# /usr/local/nessus/sbin/nessuscli fetch --register xxxx-xxxx-xxxx-xxxx
```

### Windows

```
C:\Program Files\Tenable\Nessus>nessuscli.exe fetch --register xxxx-xxxx-xxxx-xxxx
```

### macOS

```
# /Library/Nessus/run/sbin/nessuscli fetch --register xxxx-xxxx-xxxx-xxxx
```

Replace `xxxx-xxxx-xxxx-xxxx` with your new Nessus Professional Key.

Please note that this script is provided for educational purposes only and should be used responsibly and in compliance with the Nessus licensing terms.
