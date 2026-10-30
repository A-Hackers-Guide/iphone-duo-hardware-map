# `/usr/sbin/nvram`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 57,408 bytes.

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
Value exceeded max length of %d
IONVRAM-DELETEWRET-PROPERTY
%s\t%s\n
\t-X         use HEX format for printing or reading variables
no such option as --
Name exceeded max length of %d
\t-z         use system-options node if available (internal builds only)
Note that arguments and options are executed in order.
-x not supported with -X hex mode.\n
IONVRAM-SYNCNOW-PROPERTY
ClearOFVariable
Error clearing firmware variable %s: %s
\t-p         print all firmware variables
Error creating CFTypeRef for value %s
failed to allocate string
\t-s         force sync changes to storage
nvram is not supported on this system
No options-system node, using options.\n
substring %s not found in %s\n
\t-d         delete the named variable(does not return error code)
\t-b         set variable using binary file. invoked with the following format: nvram -b <variable name> <binary file>
IODeviceTree:/options
Error deleting variable - '%s': %s (0x%08x)
%%%02x
\tname=value set named variable
\tname       print variable
(usage: %s)
r
Last line ended abruptly
Could not open %s: %s
Could not allocate buffer
allocation failed
0x%x
%02x
%d
unsupported option -z
false
Error getting variable - '%s': %s
Error getting the firmware variables: %s
%s\t%zu\n
nvram [-x|-X] [-p] [-f filename] [-d name] [-c] [-s] name[=value] ...
\t           (must appear before -p or -f)
Unable to convert property name to C string
IONVRAM-FORCESYNCNOW-PROPERTY
missing name
Error setting variable - '%s': %s.\n
\t-c         delete all variables
IOService:/options/options-system
missing filename
Error creating CFString for key %s
Name must be followed by white space - '%s'
Could not create stream from serialized data
<UNPRINTABLE>
key\tbytes\n
Error creating xml plist for variable
Unable to convert value to C string
<INVALID>
Error converting variables to xml
nvram.c
Selecting options-system node.\n
Invalid file size %d
Error setting variable - '%s': %s
Couldn't open patch file - '%s'
Could not read %s: %s
CFGetTypeID(key) == CFStringGetTypeID()
Error getting the IOMainPort: %s
missing arguments
no arguments specified
too big for our purposes
Error creating dictionary for variable value
Could not fstat %s: %s
\t-x         use XML format for printing or reading variables
Couldn't open binary file - '%s'
true
Could not open the stream
Error parsing XML file
Unsupported named variable CFTypeID
i24@?0r^v8r^v16
\t-f         set firmware variables from a text file
\t-r         delete the named variable(returns error code if any)
-1
IONVRAM-DELETE-PROPERTY
-X hex mode not supported with -x XMLmode.\n
```
