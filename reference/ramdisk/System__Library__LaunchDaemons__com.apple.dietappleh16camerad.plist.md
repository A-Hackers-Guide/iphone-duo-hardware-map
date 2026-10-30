# `/System/Library/LaunchDaemons/com.apple.dietappleh16camerad.plist`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,427 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.dietappleh16camerad`
- `LaunchEvents`:
  - `com.apple.iokit.matching`:
    - `com.apple.dietappleh16camerad.destroy`:
      - `IOMatchAll`: `True`
      - `IOMatchLaunchStream`: `True`
      - `IOPropertyMatch`:
        - `dietappleh16camerad`: `False`
      - `IOProviderClass`: `IOResources`
    - `com.apple.dietappleh16camerad.launch`:
      - `IOMatchAll`: `True`
      - `IOMatchLaunchStream`: `True`
      - `IOPropertyMatch`:
        - `dietappleh16camerad`: `True`
      - `IOProviderClass`: `IOResources`
- `MachServices`:
  - `com.apple.dietappleh16camerad`: `True`
- `ProcessType`: `Interactive`
- `ProgramArguments`:
  - `/usr/sbin/dietappleh16camerad`
- `ThrottleInterval`: `5`
- `UserName`: `mobile`
