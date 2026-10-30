# `ULAltitudeState`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _deviceIdentifier;
@"NSNumber" _altitudeMeters;
d _timestamp;
q _altitudeStatusInfo;
```

## Properties

```
@property (T@"NSString",R,N,V_deviceIdentifier) deviceIdentifier;
@property (T@"NSNumber",R,N,V_altitudeMeters) altitudeMeters;
@property (Td,R,N,V_timestamp) timestamp;
@property (Tq,R,N,V_altitudeStatusInfo) altitudeStatusInfo;
```

## Instance methods

```
-[ULAltitudeState timestamp];
-[ULAltitudeState deviceIdentifier];
-[ULAltitudeState altitudeMeters];
-[ULAltitudeState altitudeStatusInfo];
-[ULAltitudeState initWithDeviceIdentifier:altitudeMeters:timestamp:altitudeStatusInfo:];
```
