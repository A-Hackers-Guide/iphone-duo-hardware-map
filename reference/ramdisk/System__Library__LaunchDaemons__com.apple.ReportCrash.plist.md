# `/System/Library/LaunchDaemons/com.apple.ReportCrash.plist`

From the upgrade restore ramdisk (141-29011-104.dmg). 429 bytes.

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
