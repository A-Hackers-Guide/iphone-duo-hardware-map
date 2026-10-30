# `/System/Library/LaunchDaemons/com.apple.restored_external.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 455 bytes.

- `EnablePressuredExit`: `False`
- `EnvironmentVariables`:
  - `ACTIVITY_LOG_STDERR`: `1`
  - `OS_ACTIVITY_DT_MODE`: `1`
  - `OS_ACTIVITY_MODE`: `info`
  - `OS_LOG_FAULT_REPORTS`: `always`
- `Label`: `com.apple.restored_external`
- `POSIXSpawnType`: `Interactive`
- `ProgramArguments`:
  - `/usr/local/bin/restored_external`
- `RunAtLoad`: `True`
- `StandardErrorPath`: `/dev/console`
- `StandardOutPath`: `/dev/console`
- `Umask`: `0`
