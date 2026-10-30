# `/usr/bin/usbcfwflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 72,416 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2232)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (6)

- `/usr/lib/libUSBCfwflasher.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleAstrisGpioProbeUserClient</string>
		<string>AppleHPMUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (145)

```
%s was terminated by signal %d
isRestoreMode
fileName
Multiple flash instructions without unique RID specifiers
Error disabling retries
quiet
force
kern.bootargs
gaidEnabled
isFactory
 
Hardware Present:
Error enabling/disabling GAID
options
\t        UUID: %@
No flash operations specified
queryInfo
Backflashing allowed
Firmware Path
%.*s
silentFailBackflashing
retriesDisabled
RID
%@
usbcfw-attempt-backflash
Using firmware at: %s
Using firmware at hardcoded path: %s
Path to Firmware Version
rid
Flash
i
gaidDisabled... applying to all updates
\t         RID: %@
performFlash
flashing error: firmware not found or of invalid length
No errors
usbcfwupdater version %s
New updatesDict:
Gaid
\t usbcfwflasher [--rid=<index>] --verbose [--flash=<file path>]
\t        Name: %@
---
Silence backflashing failures
ERROR!  ABORTED!
\t usbcfwflasher --restore [--reset] [--Gaid] [--noGaid] [--noretries] [--stashExpectedFWVersion <filename>] [--flash=<file_path>]
usbcfwflasherResult
stashExpectedFWVersion
verbose
Allowing backflashing attempts because 'usbcfw-attempt-backflash' bootarg is set
Options to both enable and disable GAID were specified.  Uncertain how to proceed.  Aborting.
waitpid failed for %s: %s
restoreEmbedded
stashFirmwareFileName
Version
\t%s
USBC FW Flasher: Total elapsed time: %f seconds
restore
f:rEvqhngxXz:R:VFA
Help
RID number didn't match any valid updater instance
%s was stopped by signal %d
flash
\t usbcfwflasher --version
commandmode
backflashingAllowed
255
usbcfwflasher
Error storing expected firmware version
Firmware found is %lu (0x%lX) bytes
Updates to be done:
Saving firmware version string to: %s
Firmware Data
YES
posix_spawn %s failed: %s
\t usbcfwflasher [--rid=<index>] --flash=<file_path> [--reset] [--noreset] [--noretries]
reset
    rid: %@
noreset
gaidEnabled... applying to all updates
pipe failed while preparing to execute %s: %s
HCPM
noretries
factory
Usage:
\t usbcfwflasher --help
%s=%@
usbcfwflash-factory=1
/usr/sbin/nvram
-d
help
gaidExpected
1.1.43
Bad argument
\tOTP Key Hash: %@
kCommandModeFlash - flashing...
version
gaidDisabled
\t     Version: %@
kCommandModeFlash - flashing result: %s
NO
firmware not found or of invalid length
usbcfwupdater - no command specified
numberWithInteger:
version
countByEnumeratingWithState:objects:count:
dictionary
objectForKeyedSubscript:
selectUpdaterWithRID:
setObject:forKeyedSubscript:
unsignedLongValue
updaterSupported:
count
date
name
optkeyshash
stringWithFormat:
numberWithBool:
enableDisableGAID:
removeAllObjects
setObject:forKey:
stringWithUTF8String:
uuid
mutableCopy
timeIntervalSinceDate:
sharedInstance:
compare:
execCmd:withInput:andOutput:andErrorResponse:
locatedDevices
setVerbose:
string
UTF8String
integerValue
stashFirmwareVersionInFile:
appendFormat:
dataWithContentsOfFile:
length
objectForKey:
removeObjectForKey:
boolValue
code
description
dictionaryWithCapacity:
dictionaryWithObject:forKey:
enableDisableRetries:
errorWithDomain:code:userInfo:
```
