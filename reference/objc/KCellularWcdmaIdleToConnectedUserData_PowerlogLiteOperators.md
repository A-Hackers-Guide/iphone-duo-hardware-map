# `KCellularWcdmaIdleToConnectedUserData`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _subsId;
@"NSData" _userData;
B _isUplink;
{?="timestamp"b1"subsId"b1"isUplink"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasIsUplink;
@property (TB,N,V_isUplink) isUplink;
@property (TB,R,N) hasUserData;
@property (T@"NSData",&,N,V_userData) userData;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularWcdmaIdleToConnectedUserData hasTimestamp];
-[KCellularWcdmaIdleToConnectedUserData setHasTimestamp:];
-[KCellularWcdmaIdleToConnectedUserData setTimestamp:];
-[KCellularWcdmaIdleToConnectedUserData writeTo:];
-[KCellularWcdmaIdleToConnectedUserData mergeFrom:];
-[KCellularWcdmaIdleToConnectedUserData timestamp];
-[KCellularWcdmaIdleToConnectedUserData userData];
-[KCellularWcdmaIdleToConnectedUserData hash];
-[KCellularWcdmaIdleToConnectedUserData copyTo:];
-[KCellularWcdmaIdleToConnectedUserData description];
-[KCellularWcdmaIdleToConnectedUserData readFrom:];
-[KCellularWcdmaIdleToConnectedUserData copyWithZone:];
-[KCellularWcdmaIdleToConnectedUserData isEqual:];
-[KCellularWcdmaIdleToConnectedUserData dictionaryRepresentation];
-[KCellularWcdmaIdleToConnectedUserData setUserData:];
-[KCellularWcdmaIdleToConnectedUserData hasUserData];
-[KCellularWcdmaIdleToConnectedUserData isUplink];
-[KCellularWcdmaIdleToConnectedUserData setIsUplink:];
-[KCellularWcdmaIdleToConnectedUserData hasSubsId];
-[KCellularWcdmaIdleToConnectedUserData setHasSubsId:];
-[KCellularWcdmaIdleToConnectedUserData setSubsId:];
-[KCellularWcdmaIdleToConnectedUserData subsId];
-[KCellularWcdmaIdleToConnectedUserData setHasIsUplink:];
-[KCellularWcdmaIdleToConnectedUserData hasIsUplink];
```
