# `/System/Library/LaunchDaemons/com.apple.ReportCrash.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 429 bytes.

- `EfficiencyMode`: `Efficient`
- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.ReportCrash`
- `MachServices`:
  - `com.apple.ReportCrash`:
    - `ExceptionServer`: `{}`
  - `com.apple.usernotifications.delegate.com.apple.DiagnosticsReporter`: `True`
- `POSIXSpawnType`: `Interactive`
- `ProgramArguments`:
  - `/System/Library/CoreServices/ReportCrash`
  - `agent`
- `UserName`: `mobile`
