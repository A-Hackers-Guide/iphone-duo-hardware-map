# `CLPIndoorCMAttitude`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 26 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
f _magneticAccuracy;
i _magneticCalibration;
@"CLPQuaternion" _quaternion;
{?="timestamp"b1"magneticAccuracy"b1"magneticCalibration"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,R,N) hasQuaternion;
@property (T@"CLPQuaternion",&,N,V_quaternion) quaternion;
@property (TB,N) hasMagneticAccuracy;
@property (Tf,N,V_magneticAccuracy) magneticAccuracy;
@property (TB,N) hasMagneticCalibration;
@property (Ti,N,V_magneticCalibration) magneticCalibration;
```

## Instance methods

```
-[CLPIndoorCMAttitude hasTimestamp];
-[CLPIndoorCMAttitude setHasTimestamp:];
-[CLPIndoorCMAttitude setTimestamp:];
-[CLPIndoorCMAttitude writeTo:];
-[CLPIndoorCMAttitude mergeFrom:];
-[CLPIndoorCMAttitude timestamp];
-[CLPIndoorCMAttitude hash];
-[CLPIndoorCMAttitude copyTo:];
-[CLPIndoorCMAttitude description];
-[CLPIndoorCMAttitude readFrom:];
-[CLPIndoorCMAttitude copyWithZone:];
-[CLPIndoorCMAttitude isEqual:];
-[CLPIndoorCMAttitude dictionaryRepresentation];
-[CLPIndoorCMAttitude quaternion];
-[CLPIndoorCMAttitude setQuaternion:];
-[CLPIndoorCMAttitude StringAsMagneticCalibration:];
-[CLPIndoorCMAttitude hasMagneticAccuracy];
-[CLPIndoorCMAttitude hasMagneticCalibration];
-[CLPIndoorCMAttitude hasQuaternion];
-[CLPIndoorCMAttitude magneticAccuracy];
-[CLPIndoorCMAttitude magneticCalibration];
-[CLPIndoorCMAttitude magneticCalibrationAsString:];
-[CLPIndoorCMAttitude setHasMagneticAccuracy:];
-[CLPIndoorCMAttitude setHasMagneticCalibration:];
-[CLPIndoorCMAttitude setMagneticAccuracy:];
-[CLPIndoorCMAttitude setMagneticCalibration:];
```
