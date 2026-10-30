# `CLPCellOutOfServiceInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"CLPLocation" _location;
@"NSString" _serviceProviderName;
B _hasWifiFallback;
B _uniqueCount;
{?="hasWifiFallback"b1"uniqueCount"b1} _has;
```

## Properties

```
@property (TB,R,N) hasLocation;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,R,N) hasServiceProviderName;
@property (T@"NSString",&,N,V_serviceProviderName) serviceProviderName;
@property (TB,N) hasUniqueCount;
@property (TB,N,V_uniqueCount) uniqueCount;
@property (TB,N) hasHasWifiFallback;
@property (TB,N,V_hasWifiFallback) hasWifiFallback;
```

## Instance methods

```
-[CLPCellOutOfServiceInfo writeTo:];
-[CLPCellOutOfServiceInfo hasHasWifiFallback];
-[CLPCellOutOfServiceInfo serviceProviderName];
-[CLPCellOutOfServiceInfo hasLocation];
-[CLPCellOutOfServiceInfo hasUniqueCount];
-[CLPCellOutOfServiceInfo location];
-[CLPCellOutOfServiceInfo mergeFrom:];
-[CLPCellOutOfServiceInfo hasWifiFallback];
-[CLPCellOutOfServiceInfo setServiceProviderName:];
-[CLPCellOutOfServiceInfo setUniqueCount:];
-[CLPCellOutOfServiceInfo setHasHasWifiFallback:];
-[CLPCellOutOfServiceInfo setLocation:];
-[CLPCellOutOfServiceInfo hash];
-[CLPCellOutOfServiceInfo copyTo:];
-[CLPCellOutOfServiceInfo hasServiceProviderName];
-[CLPCellOutOfServiceInfo description];
-[CLPCellOutOfServiceInfo uniqueCount];
-[CLPCellOutOfServiceInfo readFrom:];
-[CLPCellOutOfServiceInfo copyWithZone:];
-[CLPCellOutOfServiceInfo setHasWifiFallback:];
-[CLPCellOutOfServiceInfo setHasUniqueCount:];
-[CLPCellOutOfServiceInfo isEqual:];
-[CLPCellOutOfServiceInfo dictionaryRepresentation];
```
