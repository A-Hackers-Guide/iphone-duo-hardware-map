# `AAHIDDevice`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _isSetupComplete;
B _isSubscribed;
@"HIDDevice" _hidDevice;
@"AASensorInfo" _sensorInfo;
```

## Properties

```
@property (T@"HIDDevice",R,C,N,V_hidDevice) hidDevice;
@property (TB,N,V_isSetupComplete) isSetupComplete;
@property (TB,N,V_isSubscribed) isSubscribed;
@property (T@"AASensorInfo",C,N,V_sensorInfo) sensorInfo;
```

## Instance methods

```
-[AAHIDDevice setIsSubscribed:];
-[AAHIDDevice isSetupComplete];
-[AAHIDDevice isSubscribed];
-[AAHIDDevice hidDevice];
-[AAHIDDevice setIsSetupComplete:];
-[AAHIDDevice initWithHIDDeviceAndSensorInfo:sensorInfo:];
-[AAHIDDevice sensorInfo];
-[AAHIDDevice setSensorInfo:];
```
