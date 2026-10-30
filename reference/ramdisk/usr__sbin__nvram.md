# `/usr/sbin/nvram`

From the upgrade restore ramdisk (141-29011-104.dmg). 57,408 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1792)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (3)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.amfi.version-restriction</key>
	<integer>1</integer>
	<key>com.apple.private.iokit.system-nvram-internal-allow</key>
	<true/>
</dict>
</plist>
```

## Strings (83)

```
Could not open %s: %s
Could not fstat %s: %s
<UNPRINTABLE>
Error creating dictionary for variable value
\t-d         delete the named variable(does not return error code)
\t-z         use system-options node if available (internal builds only)
Name must be followed by white space - '%s'
Couldn't open patch file - '%s'
Error parsing XML file
substring %s not found in %s\n
%02x
<INVALID>
IONVRAM-SYNCNOW-PROPERTY
Error clearing firmware variable %s: %s
-x not supported with -X hex mode.\n
-X hex mode not supported with -x XMLmode.\n
Error setting variable - '%s': %s
false
Could not read %s: %s
allocation failed
missing name
true
Name exceeded max length of %d
key\tbytes\n
\t-x         use XML format for printing or reading variables
\t-f         set firmware variables from a text file
\t-b         set variable using binary file. invoked with the following format: nvram -b <variable name> <binary file>
\tname       print variable
Selecting options-system node.\n
Unable to convert property name to C string
Error getting the firmware variables: %s
Note that arguments and options are executed in order.
Couldn't open binary file - '%s'
failed to allocate string
i24@?0r^v8r^v16
%d
IONVRAM-FORCESYNCNOW-PROPERTY
IOService:/options/options-system
Error creating CFString for key %s
Could not open the stream
Error setting variable - '%s': %s.\n
0x%x
Unable to convert value to C string
\t-p         print all firmware variables
missing filename
No options-system node, using options.\n
r
Last line ended abruptly
Error creating xml plist for variable
%s\t%s\n
\tname=value set named variable
too big for our purposes
%s\t%zu\n
-1
ClearOFVariable
CFGetTypeID(key) == CFStringGetTypeID()
\t-s         force sync changes to storage
nvram is not supported on this system
no arguments specified
(usage: %s)
Invalid file size %d
nvram [-x|-X] [-p] [-f filename] [-d name] [-c] [-s] name[=value] ...
Error creating CFTypeRef for value %s
Error getting the IOMainPort: %s
IODeviceTree:/options
%%%02x
Unsupported named variable CFTypeID
Could not allocate buffer
Error converting variables to xml
Could not create stream from serialized data
nvram.c
missing arguments
Error getting variable - '%s': %s
\t-X         use HEX format for printing or reading variables
\t-c         delete all variables
IONVRAM-DELETEWRET-PROPERTY
unsupported option -z
no such option as --
IONVRAM-DELETE-PROPERTY
\t           (must appear before -p or -f)
\t-r         delete the named variable(returns error code if any)
Error deleting variable - '%s': %s (0x%08x)
Value exceeded max length of %d
```
