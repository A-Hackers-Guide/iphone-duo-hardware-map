# `CLPProximityVIOPoseEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 36 instance methods, 0 class methods

## Instance variables

```
{?="list"^d"count"Q"size"Q} _poseMatrixs;
d _lightEstimateLumens;
d _timestamp;
i _trackingState;
B _majorRelocalization;
B _minorRelocalization;
{?="lightEstimateLumens"b1"timestamp"b1"trackingState"b1"majorRelocalization"b1"minorRelocalization"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TQ,R,N) poseMatrixsCount;
@property (T^d,R,N) poseMatrixs;
@property (TB,N) hasTrackingState;
@property (Ti,N,V_trackingState) trackingState;
@property (TB,N) hasLightEstimateLumens;
@property (Td,N,V_lightEstimateLumens) lightEstimateLumens;
@property (TB,N) hasMajorRelocalization;
@property (TB,N,V_majorRelocalization) majorRelocalization;
@property (TB,N) hasMinorRelocalization;
@property (TB,N,V_minorRelocalization) minorRelocalization;
```

## Instance methods

```
-[CLPProximityVIOPoseEvent hasTimestamp];
-[CLPProximityVIOPoseEvent setHasTimestamp:];
-[CLPProximityVIOPoseEvent setTimestamp:];
-[CLPProximityVIOPoseEvent writeTo:];
-[CLPProximityVIOPoseEvent mergeFrom:];
-[CLPProximityVIOPoseEvent dealloc];
-[CLPProximityVIOPoseEvent timestamp];
-[CLPProximityVIOPoseEvent hash];
-[CLPProximityVIOPoseEvent copyTo:];
-[CLPProximityVIOPoseEvent description];
-[CLPProximityVIOPoseEvent readFrom:];
-[CLPProximityVIOPoseEvent copyWithZone:];
-[CLPProximityVIOPoseEvent isEqual:];
-[CLPProximityVIOPoseEvent dictionaryRepresentation];
-[CLPProximityVIOPoseEvent trackingState];
-[CLPProximityVIOPoseEvent setTrackingState:];
-[CLPProximityVIOPoseEvent majorRelocalization];
-[CLPProximityVIOPoseEvent minorRelocalization];
-[CLPProximityVIOPoseEvent addPoseMatrix:];
-[CLPProximityVIOPoseEvent clearPoseMatrixs];
-[CLPProximityVIOPoseEvent hasLightEstimateLumens];
-[CLPProximityVIOPoseEvent hasMajorRelocalization];
-[CLPProximityVIOPoseEvent hasMinorRelocalization];
-[CLPProximityVIOPoseEvent hasTrackingState];
-[CLPProximityVIOPoseEvent lightEstimateLumens];
-[CLPProximityVIOPoseEvent poseMatrixAtIndex:];
-[CLPProximityVIOPoseEvent poseMatrixs];
-[CLPProximityVIOPoseEvent poseMatrixsCount];
-[CLPProximityVIOPoseEvent setHasLightEstimateLumens:];
-[CLPProximityVIOPoseEvent setHasMajorRelocalization:];
-[CLPProximityVIOPoseEvent setHasMinorRelocalization:];
-[CLPProximityVIOPoseEvent setHasTrackingState:];
-[CLPProximityVIOPoseEvent setLightEstimateLumens:];
-[CLPProximityVIOPoseEvent setMajorRelocalization:];
-[CLPProximityVIOPoseEvent setMinorRelocalization:];
-[CLPProximityVIOPoseEvent setPoseMatrixs:count:];
```
