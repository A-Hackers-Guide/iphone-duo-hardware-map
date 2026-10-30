# `CTStewieDeviceOrientationData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _targetLocked;
B _isDeviceStationary;
@"NSDate" _timestamp;
q _x;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TB,N,V_targetLocked) targetLocked;
@property (TB,N,V_isDeviceStationary) isDeviceStationary;
@property (Tq,N,V_x) x;
```

## Class methods

```
+[CTStewieDeviceOrientationData supportsSecureCoding];
```

## Instance methods

```
-[CTStewieDeviceOrientationData setTimestamp:];
-[CTStewieDeviceOrientationData timestamp];
-[CTStewieDeviceOrientationData setX:];
-[CTStewieDeviceOrientationData x];
-[CTStewieDeviceOrientationData encodeWithCoder:];
-[CTStewieDeviceOrientationData description];
-[CTStewieDeviceOrientationData initWithCoder:];
-[CTStewieDeviceOrientationData copyWithZone:];
-[CTStewieDeviceOrientationData isEqual:];
-[CTStewieDeviceOrientationData isDeviceStationary];
-[CTStewieDeviceOrientationData setIsDeviceStationary:];
-[CTStewieDeviceOrientationData setTargetLocked:];
-[CTStewieDeviceOrientationData targetLocked];
```
