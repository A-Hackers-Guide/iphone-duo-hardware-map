# `/System/Library/LaunchDaemons/com.apple.dietappleh13camerad.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,431 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.dietappleh13camerad`
- `LaunchEvents`:
  - `com.apple.iokit.matching`:
    - `com.apple.dietappleh13camerad.destroy`:
      - `IOMatchAll`: `True`
      - `IOMatchLaunchStream`: `True`
      - `IOPropertyMatch`:
        - `dietappleh13camerad`: `False`
      - `IOProviderClass`: `IOResources`
    - `com.apple.dietappleh13camerad.launch - 2`:
      - `IOMatchAll`: `True`
      - `IOMatchLaunchStream`: `True`
      - `IOPropertyMatch`:
        - `dietappleh13camerad`: `True`
      - `IOProviderClass`: `IOResources`
- `MachServices`:
  - `com.apple.dietappleh13camerad`: `True`
- `ProcessType`: `Interactive`
- `ProgramArguments`:
  - `/usr/sbin/dietappleh13camerad`
- `ThrottleInterval`: `5`
- `UserName`: `mobile`
