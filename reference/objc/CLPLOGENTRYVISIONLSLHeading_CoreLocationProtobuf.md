# `CLPLOGENTRYVISIONLSLHeading`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 37 instance methods, 0 class methods

## Instance variables

```
d _confidence;
i _globalReferenceFrame;
@"CLPLOGENTRYVISIONLSLLocation" _location;
@"CLPLOGENTRYVISIONSimdDoubleMxN" _rotationFromGlobalToCameraFrame;
@"CLPLOGENTRYVISIONSimdDoubleMxN" _rotationFromGlobalToDeviceFrame;
@"CLPLOGENTRYVISIONSimdDoubleM" _rotationalAccuracyInRadians;
@"CLPLOGENTRYVISIONLSLHeadingSupplInfo" _supplemantaryInfo;
@"CLPLOGENTRYVISIONTimeStamp" _timestamp;
{?="confidence"b1"globalReferenceFrame"b1} _has;
```

## Properties

```
@property (TB,R,N) hasTimestamp;
@property (T@"CLPLOGENTRYVISIONTimeStamp",&,N,V_timestamp) timestamp;
@property (TB,R,N) hasRotationFromGlobalToDeviceFrame;
@property (T@"CLPLOGENTRYVISIONSimdDoubleMxN",&,N,V_rotationFromGlobalToDeviceFrame) rotationFromGlobalToDeviceFrame;
@property (TB,R,N) hasRotationFromGlobalToCameraFrame;
@property (T@"CLPLOGENTRYVISIONSimdDoubleMxN",&,N,V_rotationFromGlobalToCameraFrame) rotationFromGlobalToCameraFrame;
@property (TB,R,N) hasRotationalAccuracyInRadians;
@property (T@"CLPLOGENTRYVISIONSimdDoubleM",&,N,V_rotationalAccuracyInRadians) rotationalAccuracyInRadians;
@property (TB,N) hasConfidence;
@property (Td,N,V_confidence) confidence;
@property (TB,N) hasGlobalReferenceFrame;
@property (Ti,N,V_globalReferenceFrame) globalReferenceFrame;
@property (TB,R,N) hasLocation;
@property (T@"CLPLOGENTRYVISIONLSLLocation",&,N,V_location) location;
@property (TB,R,N) hasSupplemantaryInfo;
@property (T@"CLPLOGENTRYVISIONLSLHeadingSupplInfo",&,N,V_supplemantaryInfo) supplemantaryInfo;
```

## Instance methods

```
-[CLPLOGENTRYVISIONLSLHeading hasTimestamp];
-[CLPLOGENTRYVISIONLSLHeading setTimestamp:];
-[CLPLOGENTRYVISIONLSLHeading writeTo:];
-[CLPLOGENTRYVISIONLSLHeading hasLocation];
-[CLPLOGENTRYVISIONLSLHeading location];
-[CLPLOGENTRYVISIONLSLHeading mergeFrom:];
-[CLPLOGENTRYVISIONLSLHeading timestamp];
-[CLPLOGENTRYVISIONLSLHeading setConfidence:];
-[CLPLOGENTRYVISIONLSLHeading hasConfidence];
-[CLPLOGENTRYVISIONLSLHeading setLocation:];
-[CLPLOGENTRYVISIONLSLHeading hash];
-[CLPLOGENTRYVISIONLSLHeading copyTo:];
-[CLPLOGENTRYVISIONLSLHeading description];
-[CLPLOGENTRYVISIONLSLHeading readFrom:];
-[CLPLOGENTRYVISIONLSLHeading copyWithZone:];
-[CLPLOGENTRYVISIONLSLHeading isEqual:];
-[CLPLOGENTRYVISIONLSLHeading setHasConfidence:];
-[CLPLOGENTRYVISIONLSLHeading confidence];
-[CLPLOGENTRYVISIONLSLHeading dictionaryRepresentation];
-[CLPLOGENTRYVISIONLSLHeading rotationFromGlobalToCameraFrame];
-[CLPLOGENTRYVISIONLSLHeading setRotationalAccuracyInRadians:];
-[CLPLOGENTRYVISIONLSLHeading rotationFromGlobalToDeviceFrame];
-[CLPLOGENTRYVISIONLSLHeading globalReferenceFrame];
-[CLPLOGENTRYVISIONLSLHeading rotationalAccuracyInRadians];
-[CLPLOGENTRYVISIONLSLHeading setGlobalReferenceFrame:];
-[CLPLOGENTRYVISIONLSLHeading setRotationFromGlobalToCameraFrame:];
-[CLPLOGENTRYVISIONLSLHeading setRotationFromGlobalToDeviceFrame:];
-[CLPLOGENTRYVISIONLSLHeading setSupplemantaryInfo:];
-[CLPLOGENTRYVISIONLSLHeading supplemantaryInfo];
-[CLPLOGENTRYVISIONLSLHeading StringAsGlobalReferenceFrame:];
-[CLPLOGENTRYVISIONLSLHeading globalReferenceFrameAsString:];
-[CLPLOGENTRYVISIONLSLHeading hasGlobalReferenceFrame];
-[CLPLOGENTRYVISIONLSLHeading hasRotationFromGlobalToCameraFrame];
-[CLPLOGENTRYVISIONLSLHeading hasRotationFromGlobalToDeviceFrame];
-[CLPLOGENTRYVISIONLSLHeading hasRotationalAccuracyInRadians];
-[CLPLOGENTRYVISIONLSLHeading hasSupplemantaryInfo];
-[CLPLOGENTRYVISIONLSLHeading setHasGlobalReferenceFrame:];
```
