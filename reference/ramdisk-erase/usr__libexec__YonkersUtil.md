# `/usr/libexec/YonkersUtil`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 71,344 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 1896)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (5)

- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.savage-tool</string>
	<key>com.apple.QuartzCore.displayable-context</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.backboard.client</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.private.applepearl.allow</key>
	<true/>
	<key>com.apple.private.hid.client.event-monitor</key>
	<true/>
	<key>com.apple.private.hid.client.service-protected</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleH10CamInUserClient</string>
		<string>AppleH13CamInUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (33)

```
%sUID
AppleCamera
OPTIONS:\n
%sMacAlgo
%s: ERROR: Did not specify which sensor cert data is needed \n
\t\t --help\t\t\t\t\t\tUsage
Yonkers
number
provCertData
YonkersUtil
\t\t --number\t\t\t\t\tSensor number (< %d) \n
%sChipID
%sPubKey
%sPubKeyHmac
YonkersIR2
AppleH10CamIn
AppleH13CamIn
Usage: %s -c [-h] .....\n
%sProvPubKey
%sProvPubKeyHmac
AppleH16CamIn
%s: ERROR: Sensor number out of bounds (sensorNumber = %ld) \n
%sMNS
%sECPubKey
certData
%sECPubKeyHmac
YonkersIR1
c:p:n:h
help
\t\t --certData\t\t\t\t\tGet the certification data struct
%s: ERROR: At least one option required\n
\t\t --provCertData\t\t\t\tGet the provenance certification data struct
\n
```
