# `BWSensorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _portType;
@"NSString" _sensorIDString;
@"NSDictionary" _sensorIDDictionary;
@"NSDictionary" _cameraInfo;
@? _cameraInfoProvider;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cameraInfoLock;
@"CMIModuleCalibration" _moduleCalibration;
```

## Properties

```
@property (T@"NSString",R,N,V_portType) portType;
@property (T@"NSString",R,N,V_sensorIDString) sensorIDString;
@property (T@"NSDictionary",R,N,V_sensorIDDictionary) sensorIDDictionary;
@property (T@"NSDictionary",R,N) cameraInfo;
@property (T@"CMIModuleCalibration",R,N,V_moduleCalibration) moduleCalibration;
```

## Instance methods

```
-[BWSensorConfiguration sensorIDString];
-[BWSensorConfiguration portType];
-[BWSensorConfiguration dealloc];
-[BWSensorConfiguration description];
-[BWSensorConfiguration cameraInfo];
-[BWSensorConfiguration sensorIDDictionary];
-[BWSensorConfiguration initWithPortType:sensorIDString:sensorIDDictionary:cameraInfo:];
-[BWSensorConfiguration initWithPortType:sensorIDString:sensorIDDictionary:cameraInfo:moduleCalibration:];
-[BWSensorConfiguration initWithPortType:sensorIDString:sensorIDDictionary:cameraInfoProvider:moduleCalibration:];
-[BWSensorConfiguration moduleCalibration];
```
