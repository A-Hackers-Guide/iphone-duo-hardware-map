# `/usr/libexec/YonkersUtil`

From the upgrade restore ramdisk (141-29011-104.dmg). 71,344 bytes.

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
YonkersIR1
AppleH13CamIn
\n
%sProvPubKeyHmac
YonkersIR2
%s: ERROR: At least one option required\n
%s: ERROR: Did not specify which sensor cert data is needed \n
provCertData
OPTIONS:\n
\t\t --certData\t\t\t\t\tGet the certification data struct
%sECPubKey
%sProvPubKey
AppleH16CamIn
%sECPubKeyHmac
%s: ERROR: Sensor number out of bounds (sensorNumber = %ld) \n
number
help
\t\t --provCertData\t\t\t\tGet the provenance certification data struct
YonkersUtil
%sChipID
AppleCamera
certData
%sMNS
AppleH10CamIn
\t\t --help\t\t\t\t\t\tUsage
Usage: %s -c [-h] .....\n
%sUID
%sPubKey
%sPubKeyHmac
Yonkers
c:p:n:h
\t\t --number\t\t\t\t\tSensor number (< %d) \n
%sMacAlgo
```
