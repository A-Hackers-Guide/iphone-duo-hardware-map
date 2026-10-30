# `/System/Library/LaunchDaemons/com.apple.diskimagesiod.ram.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 696 bytes.

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
