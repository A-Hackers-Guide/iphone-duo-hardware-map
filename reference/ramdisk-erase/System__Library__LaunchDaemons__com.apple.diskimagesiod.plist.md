# `/System/Library/LaunchDaemons/com.apple.diskimagesiod.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 722 bytes.

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
