# `AWDMultitouchBootEvent`

- Image: [`/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`](../userland/System__Library__Extensions__AppleMultitouchSPI.kext__PlugIns__MultitouchHID.plugin__MultitouchHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _version;
{?="timestamp"b1"version"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasVersion;
@property (TI,N,V_version) version;
```

## Instance methods

```
-[AWDMultitouchBootEvent hasVersion];
-[AWDMultitouchBootEvent hasTimestamp];
-[AWDMultitouchBootEvent setHasTimestamp:];
-[AWDMultitouchBootEvent setTimestamp:];
-[AWDMultitouchBootEvent writeTo:];
-[AWDMultitouchBootEvent mergeFrom:];
-[AWDMultitouchBootEvent timestamp];
-[AWDMultitouchBootEvent setHasVersion:];
-[AWDMultitouchBootEvent version];
-[AWDMultitouchBootEvent hash];
-[AWDMultitouchBootEvent copyTo:];
-[AWDMultitouchBootEvent description];
-[AWDMultitouchBootEvent setVersion:];
-[AWDMultitouchBootEvent readFrom:];
-[AWDMultitouchBootEvent copyWithZone:];
-[AWDMultitouchBootEvent isEqual:];
-[AWDMultitouchBootEvent dictionaryRepresentation];
```
