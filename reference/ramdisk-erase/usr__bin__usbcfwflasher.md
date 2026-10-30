# `/usr/bin/usbcfwflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 72,416 bytes.

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
silentFailBackflashing
fileName
Firmware Data
kCommandModeFlash - flashing...
\t usbcfwflasher [--rid=<index>] --flash=<file_path> [--reset] [--noreset] [--noretries]
\t usbcfwflasher --version
backflashingAllowed
gaidExpected
\tOTP Key Hash: %@
quiet
gaidDisabled
Bad argument
Updates to be done:
Error disabling retries
kCommandModeFlash - flashing result: %s
firmware not found or of invalid length
pipe failed while preparing to execute %s: %s
version
reset
stashExpectedFWVersion
\t        Name: %@
queryInfo
usbcfwupdater version %s
HCPM
i
usbcfwflasher
\t         RID: %@
\t     Version: %@
usbcfwupdater - no command specified
flash
RID
gaidEnabled... applying to all updates
Help
Options to both enable and disable GAID were specified.  Uncertain how to proceed.  Aborting.
ERROR!  ABORTED!
No errors
\t usbcfwflasher --help
/usr/sbin/nvram
usbcfwflash-factory=1
restoreEmbedded
factory
    rid: %@
No flash operations specified
Firmware found is %lu (0x%lX) bytes
Flash
stashFirmwareFileName
Error storing expected firmware version
YES
---
Firmware Path
Using firmware at: %s
Using firmware at hardcoded path: %s
performFlash
\t%s
posix_spawn %s failed: %s
kern.bootargs
-d
verbose
%@
Multiple flash instructions without unique RID specifiers
Allowing backflashing attempts because 'usbcfw-attempt-backflash' bootarg is set
Saving firmware version string to: %s
NO
%s was terminated by signal %d
noretries
Gaid
usbcfw-attempt-backflash
Version
flashing error: firmware not found or of invalid length
%.*s
%s was stopped by signal %d
waitpid failed for %s: %s
Usage:
isRestoreMode
commandmode
1.1.43
gaidEnabled
\t        UUID: %@
%s=%@
help
force
255
isFactory
gaidDisabled... applying to all updates
Path to Firmware Version
usbcfwflasherResult
options
restore
noreset
 
Error enabling/disabling GAID
Silence backflashing failures
USBC FW Flasher: Total elapsed time: %f seconds
\t usbcfwflasher --restore [--reset] [--Gaid] [--noGaid] [--noretries] [--stashExpectedFWVersion <filename>] [--flash=<file_path>]
rid
f:rEvqhngxXz:R:VFA
retriesDisabled
New updatesDict:
Hardware Present:
RID number didn't match any valid updater instance
Backflashing allowed
\t usbcfwflasher [--rid=<index>] --verbose [--flash=<file path>]
dictionaryWithCapacity:
dictionaryWithObject:forKey:
enableDisableGAID:
length
name
stringWithFormat:
UTF8String
enableDisableRetries:
execCmd:withInput:andOutput:andErrorResponse:
objectForKey:
removeAllObjects
removeObjectForKey:
updaterSupported:
boolValue
objectForKeyedSubscript:
timeIntervalSinceDate:
numberWithBool:
date
errorWithDomain:code:userInfo:
mutableCopy
numberWithInteger:
setObject:forKey:
selectUpdaterWithRID:
uuid
countByEnumeratingWithState:objects:count:
dataWithContentsOfFile:
description
setVerbose:
stashFirmwareVersionInFile:
string
appendFormat:
code
compare:
unsignedLongValue
sharedInstance:
dictionary
integerValue
locatedDevices
optkeyshash
setObject:forKeyedSubscript:
stringWithUTF8String:
version
count
```
