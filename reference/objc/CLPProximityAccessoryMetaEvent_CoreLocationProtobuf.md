# `CLPProximityAccessoryMetaEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
@"NSString" _make;
@"NSString" _model;
@"NSString" _version;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,R,N) hasMake;
@property (T@"NSString",&,N,V_make) make;
@property (TB,R,N) hasModel;
@property (T@"NSString",&,N,V_model) model;
@property (TB,R,N) hasVersion;
@property (T@"NSString",&,N,V_version) version;
```

## Instance methods

```
-[CLPProximityAccessoryMetaEvent model];
-[CLPProximityAccessoryMetaEvent hasVersion];
-[CLPProximityAccessoryMetaEvent hasTimestamp];
-[CLPProximityAccessoryMetaEvent setHasTimestamp:];
-[CLPProximityAccessoryMetaEvent setModel:];
-[CLPProximityAccessoryMetaEvent setTimestamp:];
-[CLPProximityAccessoryMetaEvent writeTo:];
-[CLPProximityAccessoryMetaEvent mergeFrom:];
-[CLPProximityAccessoryMetaEvent timestamp];
-[CLPProximityAccessoryMetaEvent version];
-[CLPProximityAccessoryMetaEvent hash];
-[CLPProximityAccessoryMetaEvent copyTo:];
-[CLPProximityAccessoryMetaEvent description];
-[CLPProximityAccessoryMetaEvent setVersion:];
-[CLPProximityAccessoryMetaEvent readFrom:];
-[CLPProximityAccessoryMetaEvent copyWithZone:];
-[CLPProximityAccessoryMetaEvent isEqual:];
-[CLPProximityAccessoryMetaEvent dictionaryRepresentation];
-[CLPProximityAccessoryMetaEvent make];
-[CLPProximityAccessoryMetaEvent hasMake];
-[CLPProximityAccessoryMetaEvent hasModel];
-[CLPProximityAccessoryMetaEvent setMake:];
```
