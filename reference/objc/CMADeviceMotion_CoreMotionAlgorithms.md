# `CMADeviceMotion`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
{?="x"d"y"d"z"d} _rotationRate;
{?="x"d"y"d"z"d} _acceleration;
{?="x"d"y"d"z"d"w"d} _quaternion;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (T{?=dddd},N,V_quaternion) quaternion;
@property (T{?=ddd},N,V_rotationRate) rotationRate;
@property (T{?=ddd},N,V_acceleration) acceleration;
```

## Instance methods

```
-[CMADeviceMotion setTimestamp:];
-[CMADeviceMotion timestamp];
-[CMADeviceMotion acceleration];
-[CMADeviceMotion quaternion];
-[CMADeviceMotion rotationRate];
-[CMADeviceMotion setAcceleration:];
-[CMADeviceMotion setQuaternion:];
-[CMADeviceMotion setRotationRate:];
```
