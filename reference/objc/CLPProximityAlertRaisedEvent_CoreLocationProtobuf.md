# `CLPProximityAlertRaisedEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
B _alertRaised;
{?="timestamp"b1"alertRaised"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasAlertRaised;
@property (TB,N,V_alertRaised) alertRaised;
```

## Instance methods

```
-[CLPProximityAlertRaisedEvent hasTimestamp];
-[CLPProximityAlertRaisedEvent setHasTimestamp:];
-[CLPProximityAlertRaisedEvent setTimestamp:];
-[CLPProximityAlertRaisedEvent writeTo:];
-[CLPProximityAlertRaisedEvent mergeFrom:];
-[CLPProximityAlertRaisedEvent timestamp];
-[CLPProximityAlertRaisedEvent hash];
-[CLPProximityAlertRaisedEvent copyTo:];
-[CLPProximityAlertRaisedEvent description];
-[CLPProximityAlertRaisedEvent readFrom:];
-[CLPProximityAlertRaisedEvent copyWithZone:];
-[CLPProximityAlertRaisedEvent isEqual:];
-[CLPProximityAlertRaisedEvent dictionaryRepresentation];
-[CLPProximityAlertRaisedEvent setAlertRaised:];
-[CLPProximityAlertRaisedEvent alertRaised];
-[CLPProximityAlertRaisedEvent hasAlertRaised];
-[CLPProximityAlertRaisedEvent setHasAlertRaised:];
```
