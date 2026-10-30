# `/usr/sbin/hdik`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 58,480 bytes.

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
%s
 
autodiskmount
image-secrets
\t    -nomount\n
%s doesn't appear to be a device node
hmacsha1-key
-shadow
encryption-key:
improper encryption-key portion of string
\t%s -e <device>\n
IOResources
IOServiceMatched
true
couldn't construct backing store identifier
IOService
unknown option \"%s\"
Content
you must specify a device to eject
only one image may be specified
BSD Name
could not eject %s
no image specified
unable to process -drivekey parameter \"%s\"
missing <encryption-key+hmacsha1-key> parameter
content-hint
/dev/
improper hmacsha1-key portion of string
image-path
no
false
-h
-e
-drivekey
-encryption
<encryption-key+hmacsha1-key> must be 72 ASCII chars
hmacsha1-key:
unable to load driver
attach failed: error 0x%x = %d
-help
file
/dev/%@
IOHDIXController
IOKit timed out waiting for driver to load: error %08x.
eject requires input of the form %sdiskX
encryption-key
\t%s -help\n
\t    -drivekey <key>=<value>\n
IOMedia
could not open %s
\t    -encryption <encryption-key+hmacsha1-key>\n
dev-entry
%-31.31s
-shadow option not supported
%02hhx
Usage:\t%s [options] <image>\n
com.apple.AppleDiskImageController.load
yes
image-encrypted
must be run by root
\toptions:\n
d%d:i%llu
writeable-components
backingstore-id
%s ejected successfully.\n
%-20.20s
-nomount
missing -drivekey parameter
%02x
eject failed: error 0x%x = %d
hdik-unique-identifier
unable to locate attached image
```
