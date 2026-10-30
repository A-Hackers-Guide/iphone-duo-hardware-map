# `/System/Library/LaunchDaemons/com.apple.driverkitd.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 760 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `KeepAlive`:
  - `SuccessfulExit`: `False`
- `Label`: `com.apple.driverkitd`
- `LaunchEvents`:
  - `com.apple.distnoted.matching`:
    - `Application Installed`:
      - `Name`: `com.apple.LaunchServices.applicationRegistered`
    - `Application Uninstalled`:
      - `Name`: `com.apple.LaunchServices.applicationUnregistered`
- `MachServices`:
  - `com.apple.DriverKitAppServer`: `True`
  - `com.apple.DriverKitExtensionServer`: `True`
  - `com.apple.KernelManagementPingServer`:
    - `HostSpecialPort`: `15`
- `POSIXSpawnType`: `Interactive`
- `ProgramArguments`:
  - `/usr/libexec/driverkitd`
- `PublishesEvents`: `com.apple.driverkitd.DriverApprovalsChanged`
- `RunAtLoad`: `True`
