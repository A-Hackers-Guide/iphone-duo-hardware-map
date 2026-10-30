# `AWDMultitouchHardwareStatus`

- Image: [`/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`](../userland/System__Library__Extensions__AppleMultitouchSPI.kext__PlugIns__MultitouchHID.plugin__MultitouchHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
{?="list"^I"count"Q"size"Q} _openRows;
Q _timestamp;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TQ,R,N) openRowsCount;
@property (T^I,R,N) openRows;
```

## Instance methods

```
-[AWDMultitouchHardwareStatus hasTimestamp];
-[AWDMultitouchHardwareStatus setHasTimestamp:];
-[AWDMultitouchHardwareStatus setTimestamp:];
-[AWDMultitouchHardwareStatus writeTo:];
-[AWDMultitouchHardwareStatus mergeFrom:];
-[AWDMultitouchHardwareStatus dealloc];
-[AWDMultitouchHardwareStatus timestamp];
-[AWDMultitouchHardwareStatus hash];
-[AWDMultitouchHardwareStatus copyTo:];
-[AWDMultitouchHardwareStatus description];
-[AWDMultitouchHardwareStatus readFrom:];
-[AWDMultitouchHardwareStatus copyWithZone:];
-[AWDMultitouchHardwareStatus isEqual:];
-[AWDMultitouchHardwareStatus dictionaryRepresentation];
-[AWDMultitouchHardwareStatus addOpenRows:];
-[AWDMultitouchHardwareStatus clearOpenRows];
-[AWDMultitouchHardwareStatus openRows];
-[AWDMultitouchHardwareStatus openRowsAtIndex:];
-[AWDMultitouchHardwareStatus openRowsCount];
-[AWDMultitouchHardwareStatus setOpenRows:count:];
```
