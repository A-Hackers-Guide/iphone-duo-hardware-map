# `/usr/lib/libIOReport.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 121,840 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1888)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libIOReport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (150)

```
Stale samplesDict, IOReporter elements count changed
IOReportLegendPublic
m
C
couldn't create channel legend
error
LowBound
BucketMax
kIOReportUserClientConfigureInterests failed
24M
StateReport
InTransitions
GiB
QueryOpts
M
ticks
1G
BucketHits
IOReportDrivers
IOConnectMapMemory() failed
channel pruning failed
Didn't find provider_id channel_id match for samplesDict channel
%s <id %#llx>
bad argument
Mi
hwticks?
error extracting driver info
BucketMin
??
i16@?0^{__CFDictionary=}8
HighBound
%@: %@
bad arguments
unknown error
events
i32@?0^{__CFDictionary=}8^{__CFDictionary=}16^{__CFDictionary=}24
error processing simple report sample
error processing histogram report sample
HistogramReport
RawElements
prop create failed
MiB
invalid driver
dict create failed
KiB
could not allocate collection
%#llx
A
SimpleReport
v8@?0
no matching dict
IOReportChannelUnit
UnitLabel
ProcessedChannelConfig
%s%20s[%8s] = { # %-8llu %9.3e %s / %4.1f%% }\n
%s%20s[%12lld - %12lld %@] = { m %12lld; M %12lld; s %12lld; # %12llu }\n
BucketIndex
<unknown> function
kIOReportUserClientOpen failed
IOReportSubGroupName
J
channel filter returned an error
_addChannel() failed
Units
IOReportChannelConfig
%@: %s
???
<unknown> error
couldn't iterate samples
%s%32s =  %s \n
BaseUnitLabel
IOReportGroupName
%s%20s[%12lld - %12lld %@] = { <no hits>; # 0 }\n
couldn't create samples
no group or subgroup!
ChannelName
hwpage?
StateNames
n
BucketSum
bad raw data from provider
absurd element count
DriverID
DutyCycle
StateID
(none)
DriverName
IOReportHub
%s <pid %d>
4KiB
B
i24@?0^{__CFDictionary=}8^{__CFDictionary=}16
Ti
Residency
IOReportLegend
no legend
IOReportChannelGroups
F
Format
T
LegendChannel
createInterestList() failed
absurd element count from provider
Could not open IOReportHub
couldn't make dict
i12@?0I8
G
Couldn't find kIOReportRawElementsKey in samplesDict
_updateKernelBufferWithDeltas() failed
couldn't create channel
Unit
samplesDict has bad elemsData error
%s%28s[%4d] = { %12lld %@ }\n
UnitScale
Hz
%s%@ %@ < %#llx (%@) | G/g %@/%@ | cat %#04x | format %#04x | elts %u >\n
Ki
8KiB
IOReportChannelInfo
%s%32s = { %12lld %@ }\n
IOReportChannels
no channels
IOReportSubscription
V
unknown report format
StateName
<unknown>
Gi
p
u
s
H
b
packets
iteration error
_updateKernelBuffer() failed
IOPropertyMatch
TiB
k
W
bad legend
%s%s
mismatched formats
error processing state report sample
Stale samplesDict, IOReporter elements count changed %@ -- %@ -- %@ -- %@
samplesDict has bad elemsData error, %@ -- %@ -- %@ -- %@
Couldn't find kIOReportRawElementsKey, %@ -- %@ -- %@ -- %@
Didn't find provider_id channel_id match for samplesDict channel %@ -- %@ -- %@ -- %@
iterated %d channels with %d iterations
absurd element count! nelems=%d, %@ -- %@ -- %@ -- %@
```
