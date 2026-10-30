# `/System/Library/LaunchDaemons/com.apple.diskimagesiod.plist`

From the upgrade restore ramdisk (141-29011-104.dmg). 722 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.diskimagesiod`
- `MachServices`:
  - `com.apple.diskimagesiod.cachedelete`: `True`
  - `com.apple.diskimagesiod.xpc`: `True`
- `MultipleInstances`: `True`
- `ProcessType`: `Interactive`
- `ProgramArguments`:
  - `/usr/libexec/diskimagesiod`
- `UserName`: `_diskimagesiod`
