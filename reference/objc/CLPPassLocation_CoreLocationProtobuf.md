# `CLPPassLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 8 properties, 29 instance methods, 1 class methods

## Instance variables

```
d _age;
@"NSMutableArray" _associatedStoreIds;
@"CLPLocation" _location;
i _passSource;
@"NSString" _passTypeId;
i _serverHash;
{?="age"b1"serverHash"b1} _has;
```

## Properties

```
@property (T@"NSString",&,N,V_passTypeId) passTypeId;
@property (T@"NSMutableArray",&,N,V_associatedStoreIds) associatedStoreIds;
@property (Ti,N,V_passSource) passSource;
@property (TB,N) hasAge;
@property (Td,N,V_age) age;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,N) hasServerHash;
@property (Ti,N,V_serverHash) serverHash;
```

## Class methods

```
+[CLPPassLocation associatedStoreIdType];
```

## Instance methods

```
-[CLPPassLocation writeTo:];
-[CLPPassLocation location];
-[CLPPassLocation mergeFrom:];
-[CLPPassLocation age];
-[CLPPassLocation setServerHash:];
-[CLPPassLocation serverHash];
-[CLPPassLocation setHasServerHash:];
-[CLPPassLocation hasServerHash];
-[CLPPassLocation setLocation:];
-[CLPPassLocation hash];
-[CLPPassLocation copyTo:];
-[CLPPassLocation description];
-[CLPPassLocation readFrom:];
-[CLPPassLocation copyWithZone:];
-[CLPPassLocation isEqual:];
-[CLPPassLocation dictionaryRepresentation];
-[CLPPassLocation setAge:];
-[CLPPassLocation hasAge];
-[CLPPassLocation setHasAge:];
-[CLPPassLocation addAssociatedStoreId:];
-[CLPPassLocation associatedStoreIdAtIndex:];
-[CLPPassLocation associatedStoreIds];
-[CLPPassLocation associatedStoreIdsCount];
-[CLPPassLocation clearAssociatedStoreIds];
-[CLPPassLocation passSource];
-[CLPPassLocation passTypeId];
-[CLPPassLocation setAssociatedStoreIds:];
-[CLPPassLocation setPassSource:];
-[CLPPassLocation setPassTypeId:];
```
