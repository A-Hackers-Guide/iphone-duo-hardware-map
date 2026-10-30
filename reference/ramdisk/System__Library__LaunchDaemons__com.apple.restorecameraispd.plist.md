# `/System/Library/LaunchDaemons/com.apple.restorecameraispd.plist`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,416 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.restorecameraispd`
- `LaunchEvents`:
  - `com.apple.iokit.matching`:
    - `com.apple.restorecameraispd.destroy`:
      - `IOMatchAll`: `True`
      - `IOMatchLaunchStream`: `True`
      - `IOPropertyMatch`:
        - `restorecameraispd`: `False`
      - `IOProviderClass`: `IOResources`
    - `com.apple.restorecameraispd.launch`:
      - `IOMatchAll`: `True`
      - `IOMatchLaunchStream`: `True`
      - `IOPropertyMatch`:
        - `restorecameraispd`: `True`
      - `IOProviderClass`: `IOResources`
- `MachServices`:
  - `com.apple.restorecameraispd`: `True`
- `ProcessType`: `Interactive`
- `ProgramArguments`:
  - `/usr/libexec/restorecameraispd`
- `ThrottleInterval`: `5`
- `UserName`: `mobile`
