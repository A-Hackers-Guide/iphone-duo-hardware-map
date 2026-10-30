# `/usr/sbin/ioreg`

From the upgrade restore ramdisk (141-29011-104.dmg). 75,152 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1768)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (145)

```
:
reg
64-bit
#size-cells
]
can't create array
IORegistryEntryName
, busy %ld
\"
ranges
invalid ranges
:abc:d:fik:ln:p:rsStw:xyz
, %sregistered, %smatched, %sactive
slot-names
interrupts
@%s
in
, retain %ld
Wait%s resolved by %s (0x%llx) from [%lld, %lld]
No
        phandle: %08lx (%s)
         parent: 
<unknown object>
%02x
-
can't obtain terminfo
#address-cells
IOObjectRetainCount
)
<
    
 (%s)
, id 0x%llx
| 
could not get name of parent
<%08lx>
{
%c
rel
        bus: %lu dev: %lu func: %lu reg: %lu
can't create location
OSObject
can't create retain count
,
-child--
Yes
\"%s\"
can't create array for set replacement
 (non-blocking)
    %02ld: 
    %s
IOService
/dev/stdout
CFPropertyListWrite(): error
IOObjectInheritance
  
  child: 
HyperTransport vector: %04lx, 
IORegistryEntryChildren
can't obtain name
can't obtain class
can't create busy time
IOServiceBusyTime
IOUserClasses
Mem
error looking up phandle
Root object cannot be a CFSet
interrupt-parent
<>
can't obtain properties
can't create key
IODeviceTree
assigned-addresses
usage: ioreg [-abfilrtxyz] [-c class] [-d depth] [-k key] [-n name] [-p plane] [-w width]\nwhere options are:\n\t-a archive output\n\t-b show object name in bold\n\t-c list properties of objects with the given class\n\t-d limit tree to the 
can't obtain I/O Kit's root service
invalid phys addr
abs
0x%qx
        size.hi: %08lx size.lo: %08lx
specifier: %08lx (vector: %02lx) sense: %08lx (
%s)
TERM
me
[
md
can't obtain child
<class error>
can't create busy state
=
-------- 
 
%08lx 
can't create file
can't open file
, prefetch
<path error
can't create name
 (%lld ms)
}
-size---
    %02lu: phys.hi: %08lx phys.mid: %08lx phys.lo: %08lx
    %02lu: %s
!
IORegistryEntryID
IOObjectClass
@
(
---------
-parent-
ioreg: error: %s.\n
%s
+-o 
interrupt-map
Config
can't create identifier
pci
        type: %s flags: %s%s%s
unable to get path
edge
IOServiceBusyState
 = 
IORegistryEntryLocation
,\"
<name error>
I/O
unable to get device tree parent
#interrupt-cells
AAPL,phandle
can't allocate buffer
can't create path
can't obtain identifier
IOPropertyMatch
>
level
can't create dictionary
can't create state
can't obtain parent
%qu
, alias
unable to get properties
parent interrupt-map entry: %08lx
can't create class
can't obtain state
IOServiceState
  <class 
```
