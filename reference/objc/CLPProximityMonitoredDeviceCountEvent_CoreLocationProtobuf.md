# `CLPProximityMonitoredDeviceCountEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _count;
{?="timestamp"b1"count"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasCount;
@property (Ti,N,V_count) count;
```

## Instance methods

```
-[CLPProximityMonitoredDeviceCountEvent hasTimestamp];
-[CLPProximityMonitoredDeviceCountEvent setHasTimestamp:];
-[CLPProximityMonitoredDeviceCountEvent setTimestamp:];
-[CLPProximityMonitoredDeviceCountEvent writeTo:];
-[CLPProximityMonitoredDeviceCountEvent setCount:];
-[CLPProximityMonitoredDeviceCountEvent mergeFrom:];
-[CLPProximityMonitoredDeviceCountEvent timestamp];
-[CLPProximityMonitoredDeviceCountEvent count];
-[CLPProximityMonitoredDeviceCountEvent hash];
-[CLPProximityMonitoredDeviceCountEvent copyTo:];
-[CLPProximityMonitoredDeviceCountEvent description];
-[CLPProximityMonitoredDeviceCountEvent readFrom:];
-[CLPProximityMonitoredDeviceCountEvent copyWithZone:];
-[CLPProximityMonitoredDeviceCountEvent isEqual:];
-[CLPProximityMonitoredDeviceCountEvent dictionaryRepresentation];
-[CLPProximityMonitoredDeviceCountEvent hasCount];
-[CLPProximityMonitoredDeviceCountEvent setHasCount:];
```
