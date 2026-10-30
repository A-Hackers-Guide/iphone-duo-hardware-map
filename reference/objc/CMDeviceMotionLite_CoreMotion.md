# `CMDeviceMotionLite`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 14 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _usingCompass;
f _gyroTemperature;
f _compassTemperature;
@"CMAttitude" _attitude;
@"NSString" _physicalDeviceUniqueID;
Q _machTimestamp;
{?="x"d"y"d"z"d} _gravity;
{?="x"d"y"d"z"d} _userAcceleration;
{?="x"d"y"d"z"d} _rotationRate;
{?="x"d"y"d"z"d} _rawAcceleration;
{?="x"d"y"d"z"d} _rawRotationRate;
{?="x"d"y"d"z"d} _rawMagneticField;
```

## Properties

```
@property (T{?=ddd},R,N,V_rawAcceleration) rawAcceleration;
@property (T{?=ddd},R,N,V_rawRotationRate) rawRotationRate;
@property (TQ,R,N,V_machTimestamp) machTimestamp;
@property (Tf,R,N,V_gyroTemperature) gyroTemperature;
@property (Tf,R,N,V_compassTemperature) compassTemperature;
@property (T{?=ddd},R,N,V_rawMagneticField) rawMagneticField;
@property (T{?=ddd},R,N,V_gravity) gravity;
@property (T{?=ddd},R,N,V_userAcceleration) userAcceleration;
@property (Tf,R,N) tip;
@property (Tf,R,N) tilt;
@property (T@"CMAttitude",R,N,V_attitude) attitude;
@property (T{?=ddd},R,N,V_rotationRate) rotationRate;
@property (TB,R,N,GisUsingCompass,V_usingCompass) usingCompass;
@property (T@"NSString",R,C,N,V_physicalDeviceUniqueID) physicalDeviceUniqueID;
```

## Class methods

```
+[CMDeviceMotionLite supportsSecureCoding];
```

## Instance methods

```
-[CMDeviceMotionLite debugDescription];
-[CMDeviceMotionLite dealloc];
-[CMDeviceMotionLite gravity];
-[CMDeviceMotionLite encodeWithCoder:];
-[CMDeviceMotionLite description];
-[CMDeviceMotionLite initWithCoder:];
-[CMDeviceMotionLite copyWithZone:];
-[CMDeviceMotionLite attitude];
-[CMDeviceMotionLite tip];
-[CMDeviceMotionLite tilt];
-[CMDeviceMotionLite rotationRate];
-[CMDeviceMotionLite userAcceleration];
-[CMDeviceMotionLite rawRotationRate];
-[CMDeviceMotionLite gyroTemperature];
-[CMDeviceMotionLite rawAcceleration];
-[CMDeviceMotionLite compassTemperature];
-[CMDeviceMotionLite initWithDeviceMotionLite:andDeviceID:];
-[CMDeviceMotionLite isUsingCompass];
-[CMDeviceMotionLite machTimestamp];
-[CMDeviceMotionLite physicalDeviceUniqueID];
-[CMDeviceMotionLite rawMagneticField];
```
