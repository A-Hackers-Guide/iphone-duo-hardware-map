# `/usr/sbin/hdik`

From the upgrade restore ramdisk (141-29011-104.dmg). 58,480 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1632)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (3)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.diskimages.kext.user-client-access</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOHDIXControllerUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (72)

```
IOResources
/dev/%@
unable to locate attached image
writeable-components
Content
/dev/
could not open %s
%-20.20s
image-path
-e
-shadow option not supported
%02x
\t%s -e <device>\n
\t    -encryption <encryption-key+hmacsha1-key>\n
content-hint
no
unable to process -drivekey parameter \"%s\"
improper encryption-key portion of string
image-secrets
must be run by root
\toptions:\n
\t    -drivekey <key>=<value>\n
file
%s ejected successfully.\n
-help
attach failed: error 0x%x = %d
Usage:\t%s [options] <image>\n
BSD Name
%-31.31s
-drivekey
IOService
eject requires input of the form %sdiskX
%s doesn't appear to be a device node
false
encryption-key
hmacsha1-key
only one image may be specified
-h
\t    -nomount\n
backingstore-id
IOKit timed out waiting for driver to load: error %08x.
could not eject %s
no image specified
-shadow
image-encrypted
unknown option \"%s\"
couldn't construct backing store identifier
 
true
%s
you must specify a device to eject
autodiskmount
encryption-key:
eject failed: error 0x%x = %d
d%d:i%llu
-encryption
<encryption-key+hmacsha1-key> must be 72 ASCII chars
%02hhx
hdik-unique-identifier
missing <encryption-key+hmacsha1-key> parameter
dev-entry
IOHDIXController
IOMedia
hmacsha1-key:
\t%s -help\n
-nomount
missing -drivekey parameter
improper hmacsha1-key portion of string
yes
unable to load driver
com.apple.AppleDiskImageController.load
IOServiceMatched
```
