# `/System/Library/DriverExtensions/AppleCentauriBeta.dext/AppleCentauriBeta`

From the upgrade restore ramdisk (141-29011-104.dmg). 36,496 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1344)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (6)

- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriBeta.framework/CentauriBeta (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/AirshipCentauriHelperServices.framework/AirshipCentauriHelperServices (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriDebug.framework/CentauriDebug (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/MobileBluetoothDK.framework/MobileBluetoothDK (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.driverkit</key>
	<true/>
	<key>com.apple.developer.driverkit.transport.afk</key>
	<true/>
	<key>com.apple.developer.driverkit.transport.pci</key>
	<true/>
	<key>com.apple.driver.centauri.publish</key>
	<true/>
	<key>com.apple.private.corecaptureclient.driverkit</key>
	<true/>
	<key>com.apple.private.custom-coredump-location</key>
	<string>AppleCentauriBeta-dextcrash-%P.%T.core</string>
	<key>com.apple.private.driverkit.driver-launch-configuration</key>
	<true/>
	<key>com.apple.private.enable-coredump-on-panic</key>
	<string>cent-beta</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>
```

## Strings (0)

```
```
