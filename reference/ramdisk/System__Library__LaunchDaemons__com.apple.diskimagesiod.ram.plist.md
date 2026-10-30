# `/System/Library/LaunchDaemons/com.apple.diskimagesiod.ram.plist`

From the upgrade restore ramdisk (141-29011-104.dmg). 696 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.diskimagesiod.ram`
- `MachServices`:
  - `com.apple.diskimagesiod.ram.xpc`: `True`
- `MultipleInstances`: `True`
- `ProcessType`: `Interactive`
- `ProgramArguments`:
  - `/usr/libexec/diskimagesiod`
  - `--ram`
- `UserName`: `_diskimagesiod`
