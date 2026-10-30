# `CLPAppLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 11 properties, 31 instance methods, 0 class methods

## Instance variables

```
d _age;
@"NSString" _appBundleId;
i _appState;
@"CLPLocation" _location;
i _loiType;
i _routineMode;
i _serverHash;
{?="age"b1"loiType"b1"routineMode"b1"serverHash"b1} _has;
```

## Properties

```
@property (T@"NSString",&,N,V_appBundleId) appBundleId;
@property (Ti,N,V_appState) appState;
@property (TB,N) hasAge;
@property (Td,N,V_age) age;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,N) hasServerHash;
@property (Ti,N,V_serverHash) serverHash;
@property (TB,N) hasRoutineMode;
@property (Ti,N,V_routineMode) routineMode;
@property (TB,N) hasLoiType;
@property (Ti,N,V_loiType) loiType;
```

## Instance methods

```
-[CLPAppLocation appBundleId];
-[CLPAppLocation writeTo:];
-[CLPAppLocation setLoiType:];
-[CLPAppLocation setAppBundleId:];
-[CLPAppLocation location];
-[CLPAppLocation mergeFrom:];
-[CLPAppLocation age];
-[CLPAppLocation setServerHash:];
-[CLPAppLocation serverHash];
-[CLPAppLocation setHasServerHash:];
-[CLPAppLocation hasServerHash];
-[CLPAppLocation setLocation:];
-[CLPAppLocation hash];
-[CLPAppLocation setAppState:];
-[CLPAppLocation copyTo:];
-[CLPAppLocation description];
-[CLPAppLocation readFrom:];
-[CLPAppLocation copyWithZone:];
-[CLPAppLocation isEqual:];
-[CLPAppLocation loiType];
-[CLPAppLocation dictionaryRepresentation];
-[CLPAppLocation appState];
-[CLPAppLocation setAge:];
-[CLPAppLocation hasAge];
-[CLPAppLocation setHasAge:];
-[CLPAppLocation hasLoiType];
-[CLPAppLocation setHasLoiType:];
-[CLPAppLocation setRoutineMode:];
-[CLPAppLocation hasRoutineMode];
-[CLPAppLocation routineMode];
-[CLPAppLocation setHasRoutineMode:];
```
