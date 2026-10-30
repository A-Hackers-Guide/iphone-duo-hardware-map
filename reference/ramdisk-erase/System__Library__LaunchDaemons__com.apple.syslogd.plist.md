# `/System/Library/LaunchDaemons/com.apple.syslogd.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 347 bytes.

- `Disabled`: `True`
- `EnablePressuredExit`: `False`
- `EnableTransactions`: `True`
- `EnvironmentVariables`:
  - `ASL_DISABLE`: `1`
- `KeepAlive`: `True`
- `Label`: `com.apple.syslogd`
- `MachServices`:
  - `com.apple.system.logger`: `True`
- `POSIXSpawnType`: `Adaptive`
- `ProgramArguments`:
  - `/usr/sbin/syslogd`
