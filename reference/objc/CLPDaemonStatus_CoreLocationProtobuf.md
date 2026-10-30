# `CLPDaemonStatus`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _notificationType;
{?="timestamp"b1"notificationType"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasNotificationType;
@property (Ti,N,V_notificationType) notificationType;
```

## Instance methods

```
-[CLPDaemonStatus hasTimestamp];
-[CLPDaemonStatus setHasTimestamp:];
-[CLPDaemonStatus setTimestamp:];
-[CLPDaemonStatus notificationType];
-[CLPDaemonStatus writeTo:];
-[CLPDaemonStatus setNotificationType:];
-[CLPDaemonStatus mergeFrom:];
-[CLPDaemonStatus timestamp];
-[CLPDaemonStatus hash];
-[CLPDaemonStatus copyTo:];
-[CLPDaemonStatus description];
-[CLPDaemonStatus readFrom:];
-[CLPDaemonStatus copyWithZone:];
-[CLPDaemonStatus isEqual:];
-[CLPDaemonStatus dictionaryRepresentation];
-[CLPDaemonStatus StringAsNotificationType:];
-[CLPDaemonStatus hasNotificationType];
-[CLPDaemonStatus notificationTypeAsString:];
-[CLPDaemonStatus setHasNotificationType:];
```
