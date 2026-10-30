# `CLPPoiTriggerEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _muid;
d _triggerTimestamp;
i _providerIdentifier;
i _triggerSubType;
i _triggerType;
{?="triggerTimestamp"b1"providerIdentifier"b1"triggerSubType"b1"triggerType"b1} _has;
```

## Properties

```
@property (TQ,N,V_muid) muid;
@property (TB,N) hasProviderIdentifier;
@property (Ti,N,V_providerIdentifier) providerIdentifier;
@property (TB,N) hasTriggerType;
@property (Ti,N,V_triggerType) triggerType;
@property (TB,N) hasTriggerTimestamp;
@property (Td,N,V_triggerTimestamp) triggerTimestamp;
@property (TB,N) hasTriggerSubType;
@property (Ti,N,V_triggerSubType) triggerSubType;
```

## Instance methods

```
-[CLPPoiTriggerEvent writeTo:];
-[CLPPoiTriggerEvent providerIdentifier];
-[CLPPoiTriggerEvent mergeFrom:];
-[CLPPoiTriggerEvent setTriggerType:];
-[CLPPoiTriggerEvent setMuid:];
-[CLPPoiTriggerEvent muid];
-[CLPPoiTriggerEvent hash];
-[CLPPoiTriggerEvent triggerType];
-[CLPPoiTriggerEvent copyTo:];
-[CLPPoiTriggerEvent description];
-[CLPPoiTriggerEvent setProviderIdentifier:];
-[CLPPoiTriggerEvent readFrom:];
-[CLPPoiTriggerEvent copyWithZone:];
-[CLPPoiTriggerEvent isEqual:];
-[CLPPoiTriggerEvent dictionaryRepresentation];
-[CLPPoiTriggerEvent hasTriggerType];
-[CLPPoiTriggerEvent setHasTriggerType:];
-[CLPPoiTriggerEvent StringAsTriggerType:];
-[CLPPoiTriggerEvent triggerTypeAsString:];
-[CLPPoiTriggerEvent setTriggerSubType:];
-[CLPPoiTriggerEvent setTriggerTimestamp:];
-[CLPPoiTriggerEvent triggerSubType];
-[CLPPoiTriggerEvent triggerTimestamp];
-[CLPPoiTriggerEvent hasProviderIdentifier];
-[CLPPoiTriggerEvent hasTriggerSubType];
-[CLPPoiTriggerEvent hasTriggerTimestamp];
-[CLPPoiTriggerEvent setHasProviderIdentifier:];
-[CLPPoiTriggerEvent setHasTriggerSubType:];
-[CLPPoiTriggerEvent setHasTriggerTimestamp:];
```
