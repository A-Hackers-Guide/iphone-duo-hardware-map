# `_CLLSLHeading`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 22 instance methods, 1 class methods

## Instance variables

```
d _timestamp;
d _confidence;
Q _globalReferenceFrame;
@"_CLLSLLocation" _location;
@"_CLLSLHeadingSupplInfo" _supplemantaryInfo;
_rotationalAccuracyInRadians;
{?="columns"[3]} _rotationFromGlobalToDeviceFrame;
{?="columns"[3]} _rotationFromGlobalToCameraFrame;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (T{?=[3]},N,V_rotationFromGlobalToDeviceFrame) rotationFromGlobalToDeviceFrame;
@property (T{?=[3]},N,V_rotationFromGlobalToCameraFrame) rotationFromGlobalToCameraFrame;
@property (T,N,V_rotationalAccuracyInRadians) rotationalAccuracyInRadians;
@property (Td,N,V_confidence) confidence;
@property (TQ,N,V_globalReferenceFrame) globalReferenceFrame;
@property (T@"_CLLSLLocation",C,N,V_location) location;
@property (T@"_CLLSLHeadingSupplInfo",C,N,V_supplemantaryInfo) supplemantaryInfo;
```

## Class methods

```
+[_CLLSLHeading supportsSecureCoding];
```

## Instance methods

```
-[_CLLSLHeading setTimestamp:];
-[_CLLSLHeading location];
-[_CLLSLHeading dealloc];
-[_CLLSLHeading timestamp];
-[_CLLSLHeading setConfidence:];
-[_CLLSLHeading setLocation:];
-[_CLLSLHeading encodeWithCoder:];
-[_CLLSLHeading description];
-[_CLLSLHeading initWithCoder:];
-[_CLLSLHeading copyWithZone:];
-[_CLLSLHeading confidence];
-[_CLLSLHeading rotationFromGlobalToCameraFrame];
-[_CLLSLHeading setRotationalAccuracyInRadians:];
-[_CLLSLHeading rotationFromGlobalToDeviceFrame];
-[_CLLSLHeading descriptionWithMemberIndent:endIndent:];
-[_CLLSLHeading globalReferenceFrame];
-[_CLLSLHeading rotationalAccuracyInRadians];
-[_CLLSLHeading setGlobalReferenceFrame:];
-[_CLLSLHeading setRotationFromGlobalToCameraFrame:];
-[_CLLSLHeading setRotationFromGlobalToDeviceFrame:];
-[_CLLSLHeading setSupplemantaryInfo:];
-[_CLLSLHeading supplemantaryInfo];
```
