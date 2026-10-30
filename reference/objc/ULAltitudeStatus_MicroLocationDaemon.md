# `ULAltitudeStatus`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _deviceIdentifier;
@"NSNumber" _altitudeMeters;
@"NSDate" _statusDate;
q _altitudeStatusInfo;
```

## Properties

```
@property (T@"NSString",R,N,V_deviceIdentifier) deviceIdentifier;
@property (T@"NSNumber",R,N,V_altitudeMeters) altitudeMeters;
@property (T@"NSDate",R,N,V_statusDate) statusDate;
@property (Tq,R,N,V_altitudeStatusInfo) altitudeStatusInfo;
```

## Instance methods

```
-[ULAltitudeStatus deviceIdentifier];
-[ULAltitudeStatus statusDate];
-[ULAltitudeStatus altitudeMeters];
-[ULAltitudeStatus altitudeStatusInfo];
-[ULAltitudeStatus initWithDeviceIdentifier:altitudeMeters:date:altitudeStatusInfo:];
```
