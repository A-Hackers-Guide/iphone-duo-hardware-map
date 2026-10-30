# `/usr/sbin/ioreg`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 75,152 bytes.

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
can't create file
can't obtain parent
in
rel
IORegistryEntryName
}
<unknown object>
        bus: %lu dev: %lu func: %lu reg: %lu
IOPropertyMatch
can't obtain child
@%s
-
can't create array
can't create array for set replacement
can't obtain I/O Kit's root service
can't create retain count
<
\"
         parent: 
IORegistryEntryLocation
can't create key
assigned-addresses
#interrupt-cells
IORegistryEntryChildren
can't obtain identifier
%02x
#address-cells
AAPL,phandle
can't create location
can't create class
IOUserClasses
-parent-
-size---
unable to get path
edge
can't open file
IOServiceBusyState
can't create busy time
>
    %02ld: 
usage: ioreg [-abfilrtxyz] [-c class] [-d depth] [-k key] [-n name] [-p plane] [-w width]\nwhere options are:\n\t-a archive output\n\t-b show object name in bold\n\t-c list properties of objects with the given class\n\t-d limit tree to the 
IOObjectInheritance
)
]
64-bit
  child: 
<path error
[
Mem
TERM
 (non-blocking)
slot-names
    
HyperTransport vector: %04lx, 
{
\"%s\"
interrupt-map
interrupts
invalid ranges
-------- 
 (%s)
can't obtain state
  <class 
:
Yes
IODeviceTree
parent interrupt-map entry: %08lx
IOServiceBusyTime
0x%qx
, alias
        type: %s flags: %s%s%s
unable to get device tree parent
 
specifier: %08lx (vector: %02lx) sense: %08lx (
level
IOService
%qu
, prefetch
%s)
:abc:d:fik:ln:p:rsStw:xyz
/dev/stdout
can't obtain name
can't obtain class
<class error>
IOObjectRetainCount
, id 0x%llx
, retain %ld
ranges
unable to get properties
error looking up phandle
can't create identifier
Root object cannot be a CFSet
%s
 (%lld ms)
<>
#size-cells
can't allocate buffer
can't obtain properties
,\"
could not get name of parent
I/O
        size.hi: %08lx size.lo: %08lx
can't create state
@
abs
<%08lx>
md
IORegistryEntryID
Wait%s resolved by %s (0x%llx) from [%lld, %lld]
%c
| 
No
pci
    %02lu: %s
---------
IOServiceState
  
        phandle: %08lx (%s)
OSObject
+-o 
me
, busy %ld
 = 
,
can't obtain terminfo
!
=
%08lx 
    %s
can't create busy state
(
can't create path
<name error>
Config
    %02lu: phys.hi: %08lx phys.mid: %08lx phys.lo: %08lx
-child--
can't create dictionary
can't create name
invalid phys addr
ioreg: error: %s.\n
CFPropertyListWrite(): error
IOObjectClass
, %sregistered, %smatched, %sactive
reg
interrupt-parent
```
