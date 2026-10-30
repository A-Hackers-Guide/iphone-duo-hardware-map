# `/System/Library/LaunchDaemons/com.apple.PurpleReverseProxy.ramdisk.plist`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 485 bytes.

- `EnablePressuredExit`: `True`
- `EnableTransactions`: `True`
- `Label`: `com.apple.PurpleReverseProxy.ramdisk`
- `POSIXSpawnType`: `Adaptive`
- `ProgramArguments`:
  - `/usr/libexec/PurpleReverseProxy`
  - `--ramdisk`
- `Sockets`:
  - `ctrl`:
    - `SockFamily`: `IPv4v6`
    - `SockServiceName`: `1082`
  - `notify`:
    - `SockFamily`: `IPv4`
    - `SockNodeName`: `127.0.0.1`
    - `SockServiceName`: `1084`
  - `socks`:
    - `SockFamily`: `IPv4`
    - `SockNodeName`: `127.0.0.1`
    - `SockServiceName`: `1081`
- `StandardErrorPath`: `/dev/console`
- `StandardOutPath`: `/dev/console`
