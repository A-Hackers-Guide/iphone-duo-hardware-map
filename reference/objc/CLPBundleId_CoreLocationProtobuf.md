# `CLPBundleId`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
@"NSString" _fullName;
@"NSString" _shortKey;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,R,N) hasShortKey;
@property (T@"NSString",&,N,V_shortKey) shortKey;
@property (TB,R,N) hasFullName;
@property (T@"NSString",&,N,V_fullName) fullName;
```

## Instance methods

```
-[CLPBundleId hasTimestamp];
-[CLPBundleId setHasTimestamp:];
-[CLPBundleId setTimestamp:];
-[CLPBundleId writeTo:];
-[CLPBundleId mergeFrom:];
-[CLPBundleId timestamp];
-[CLPBundleId hasFullName];
-[CLPBundleId fullName];
-[CLPBundleId setFullName:];
-[CLPBundleId hash];
-[CLPBundleId copyTo:];
-[CLPBundleId description];
-[CLPBundleId readFrom:];
-[CLPBundleId copyWithZone:];
-[CLPBundleId isEqual:];
-[CLPBundleId dictionaryRepresentation];
-[CLPBundleId hasShortKey];
-[CLPBundleId setShortKey:];
-[CLPBundleId shortKey];
```
