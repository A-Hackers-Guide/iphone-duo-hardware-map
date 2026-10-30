# `CLPPassKitEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 11 properties, 37 instance methods, 1 class methods

## Instance variables

```
Q _muid;
d _timestamp;
d _transactionDate;
@"NSMutableArray" _associatedStoreIds;
i _eventType;
i _providerIdentifier;
{?="muid"b1"timestamp"b1"transactionDate"b1"eventType"b1"providerIdentifier"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasEventType;
@property (Ti,N,V_eventType) eventType;
@property (TB,N) hasMuid;
@property (TQ,N,V_muid) muid;
@property (TB,N) hasProviderIdentifier;
@property (Ti,N,V_providerIdentifier) providerIdentifier;
@property (TB,N) hasTransactionDate;
@property (Td,N,V_transactionDate) transactionDate;
@property (T@"NSMutableArray",&,N,V_associatedStoreIds) associatedStoreIds;
```

## Class methods

```
+[CLPPassKitEvent associatedStoreIdsType];
```

## Instance methods

```
-[CLPPassKitEvent hasTimestamp];
-[CLPPassKitEvent setHasTimestamp:];
-[CLPPassKitEvent setTimestamp:];
-[CLPPassKitEvent eventType];
-[CLPPassKitEvent writeTo:];
-[CLPPassKitEvent setEventType:];
-[CLPPassKitEvent providerIdentifier];
-[CLPPassKitEvent hasEventType];
-[CLPPassKitEvent mergeFrom:];
-[CLPPassKitEvent eventTypeAsString:];
-[CLPPassKitEvent setMuid:];
-[CLPPassKitEvent timestamp];
-[CLPPassKitEvent setHasEventType:];
-[CLPPassKitEvent muid];
-[CLPPassKitEvent setHasMuid:];
-[CLPPassKitEvent StringAsEventType:];
-[CLPPassKitEvent hash];
-[CLPPassKitEvent copyTo:];
-[CLPPassKitEvent description];
-[CLPPassKitEvent setProviderIdentifier:];
-[CLPPassKitEvent readFrom:];
-[CLPPassKitEvent copyWithZone:];
-[CLPPassKitEvent isEqual:];
-[CLPPassKitEvent hasMuid];
-[CLPPassKitEvent dictionaryRepresentation];
-[CLPPassKitEvent transactionDate];
-[CLPPassKitEvent setTransactionDate:];
-[CLPPassKitEvent addAssociatedStoreIds:];
-[CLPPassKitEvent associatedStoreIds];
-[CLPPassKitEvent associatedStoreIdsAtIndex:];
-[CLPPassKitEvent associatedStoreIdsCount];
-[CLPPassKitEvent clearAssociatedStoreIds];
-[CLPPassKitEvent hasProviderIdentifier];
-[CLPPassKitEvent hasTransactionDate];
-[CLPPassKitEvent setAssociatedStoreIds:];
-[CLPPassKitEvent setHasProviderIdentifier:];
-[CLPPassKitEvent setHasTransactionDate:];
```
