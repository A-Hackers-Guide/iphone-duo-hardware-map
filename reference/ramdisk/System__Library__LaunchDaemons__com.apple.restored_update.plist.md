# `/System/Library/LaunchDaemons/com.apple.restored_update.plist`

From the upgrade restore ramdisk (141-29011-104.dmg). 451 bytes.

- `EnablePressuredExit`: `False`
- `EnvironmentVariables`:
  - `ACTIVITY_LOG_STDERR`: `1`
  - `OS_ACTIVITY_DT_MODE`: `1`
  - `OS_ACTIVITY_MODE`: `info`
  - `OS_LOG_FAULT_REPORTS`: `always`
- `Label`: `com.apple.restored_update`
- `POSIXSpawnType`: `Interactive`
- `ProgramArguments`:
  - `/usr/local/bin/restored_update`
- `RunAtLoad`: `True`
- `StandardErrorPath`: `/dev/console`
- `StandardOutPath`: `/dev/console`
- `Umask`: `0`
