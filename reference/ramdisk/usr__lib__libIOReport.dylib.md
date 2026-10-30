# `/usr/lib/libIOReport.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 121,840 bytes.

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
iterated %d channels with %d iterations
absurd element count! nelems=%d, %@ -- %@ -- %@ -- %@
Stale samplesDict, IOReporter elements count changed %@ -- %@ -- %@ -- %@
samplesDict has bad elemsData error, %@ -- %@ -- %@ -- %@
Couldn't find kIOReportRawElementsKey, %@ -- %@ -- %@ -- %@
Didn't find provider_id channel_id match for samplesDict channel %@ -- %@ -- %@ -- %@
couldn't iterate samples
_updateKernelBuffer() failed
bad argument
hwticks?
IOReportDrivers
i24@?0^{__CFDictionary=}8^{__CFDictionary=}16
G
UnitScale
BucketMin
absurd element count from provider
v8@?0
no channels
IOReportGroupName
no matching dict
LegendChannel
p
n
u
V
ProcessedChannelConfig
error processing simple report sample
<unknown> error
i12@?0I8
M
F
InTransitions
BucketHits
%s%@ %@ < %#llx (%@) | G/g %@/%@ | cat %#04x | format %#04x | elts %u >\n
C
bad arguments
_addChannel() failed
StateReport
%@: %s
%s%s
QueryOpts
bad legend
RawElements
%s <id %#llx>
%s <pid %d>
<unknown>
m
24M
channel filter returned an error
IOReportHub
ChannelName
unknown report format
DutyCycle
Couldn't find kIOReportRawElementsKey in samplesDict
ticks
%#llx
error
HighBound
TiB
StateNames
no group or subgroup!
IOReportLegendPublic
W
%s%20s[%8s] = { # %-8llu %9.3e %s / %4.1f%% }\n
StateID
events
DriverName
IOReportChannels
IOReportSubGroupName
MiB
KiB
Gi
error extracting driver info
IOReportChannelGroups
UnitLabel
SimpleReport
absurd element count
4KiB
no legend
i32@?0^{__CFDictionary=}8^{__CFDictionary=}16^{__CFDictionary=}24
%s%20s[%12lld - %12lld %@] = { m %12lld; M %12lld; s %12lld; # %12llu }\n
bad raw data from provider
%@: %@
createInterestList() failed
IOReportChannelUnit
prop create failed
DriverID
Ki
8KiB
kIOReportUserClientConfigureInterests failed
Didn't find provider_id channel_id match for samplesDict channel
invalid driver
A
BaseUnitLabel
Residency
IOReportSubscription
dict create failed
Ti
B
b
??
error processing state report sample
BucketMax
unknown error
IOConnectMapMemory() failed
1G
%s%20s[%12lld - %12lld %@] = { <no hits>; # 0 }\n
Format
Units
HistogramReport
_updateKernelBufferWithDeltas() failed
hwpage?
could not allocate collection
StateName
IOPropertyMatch
Mi
Hz
%s%32s = { %12lld %@ }\n
???
GiB
s
J
mismatched formats
BucketIndex
couldn't create samples
iteration error
k
packets
Unit
i16@?0^{__CFDictionary=}8
Could not open IOReportHub
couldn't make dict
(none)
T
IOReportChannelInfo
kIOReportUserClientOpen failed
couldn't create channel legend
couldn't create channel
IOReportLegend
samplesDict has bad elemsData error
Stale samplesDict, IOReporter elements count changed
channel pruning failed
IOReportChannelConfig
H
%s%32s =  %s \n
error processing histogram report sample
LowBound
<unknown> function
%s%28s[%4d] = { %12lld %@ }\n
BucketSum
```
