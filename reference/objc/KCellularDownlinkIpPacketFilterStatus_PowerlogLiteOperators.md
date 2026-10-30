# `KCellularDownlinkIpPacketFilterStatus`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 11 properties, 35 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _bearerContextId;
@"NSMutableArray" _filters;
I _subsId;
B _isActivated;
B _isEchoReqBlocked;
{?="timestamp"b1"bearerContextId"b1"subsId"b1"isActivated"b1"isEchoReqBlocked"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasBearerContextId;
@property (TI,N,V_bearerContextId) bearerContextId;
@property (TB,N) hasIsActivated;
@property (TB,N,V_isActivated) isActivated;
@property (TB,N) hasIsEchoReqBlocked;
@property (TB,N,V_isEchoReqBlocked) isEchoReqBlocked;
@property (T@"NSMutableArray",&,N,V_filters) filters;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Class methods

```
+[KCellularDownlinkIpPacketFilterStatus filtersType];
```

## Instance methods

```
-[KCellularDownlinkIpPacketFilterStatus hasTimestamp];
-[KCellularDownlinkIpPacketFilterStatus isActivated];
-[KCellularDownlinkIpPacketFilterStatus setHasTimestamp:];
-[KCellularDownlinkIpPacketFilterStatus setTimestamp:];
-[KCellularDownlinkIpPacketFilterStatus writeTo:];
-[KCellularDownlinkIpPacketFilterStatus filtersAtIndex:];
-[KCellularDownlinkIpPacketFilterStatus setIsActivated:];
-[KCellularDownlinkIpPacketFilterStatus clearFilters];
-[KCellularDownlinkIpPacketFilterStatus mergeFrom:];
-[KCellularDownlinkIpPacketFilterStatus timestamp];
-[KCellularDownlinkIpPacketFilterStatus setFilters:];
-[KCellularDownlinkIpPacketFilterStatus filters];
-[KCellularDownlinkIpPacketFilterStatus filtersCount];
-[KCellularDownlinkIpPacketFilterStatus hash];
-[KCellularDownlinkIpPacketFilterStatus copyTo:];
-[KCellularDownlinkIpPacketFilterStatus description];
-[KCellularDownlinkIpPacketFilterStatus addFilters:];
-[KCellularDownlinkIpPacketFilterStatus readFrom:];
-[KCellularDownlinkIpPacketFilterStatus copyWithZone:];
-[KCellularDownlinkIpPacketFilterStatus isEqual:];
-[KCellularDownlinkIpPacketFilterStatus dictionaryRepresentation];
-[KCellularDownlinkIpPacketFilterStatus hasIsActivated];
-[KCellularDownlinkIpPacketFilterStatus setHasIsActivated:];
-[KCellularDownlinkIpPacketFilterStatus hasSubsId];
-[KCellularDownlinkIpPacketFilterStatus setHasSubsId:];
-[KCellularDownlinkIpPacketFilterStatus setSubsId:];
-[KCellularDownlinkIpPacketFilterStatus subsId];
-[KCellularDownlinkIpPacketFilterStatus bearerContextId];
-[KCellularDownlinkIpPacketFilterStatus hasBearerContextId];
-[KCellularDownlinkIpPacketFilterStatus hasIsEchoReqBlocked];
-[KCellularDownlinkIpPacketFilterStatus isEchoReqBlocked];
-[KCellularDownlinkIpPacketFilterStatus setBearerContextId:];
-[KCellularDownlinkIpPacketFilterStatus setHasBearerContextId:];
-[KCellularDownlinkIpPacketFilterStatus setHasIsEchoReqBlocked:];
-[KCellularDownlinkIpPacketFilterStatus setIsEchoReqBlocked:];
```
