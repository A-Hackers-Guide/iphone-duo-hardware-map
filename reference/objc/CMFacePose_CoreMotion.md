# `CMFacePose`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _tooDark;
B _sensorCovered;
i _failureCode;
f _confidence;
d _localMachtime;
d _globalMachtime;
@"NSString" _failureDescription;
@"NSArray" _blendShapeWeights;
d _roll;
_translation;
_gaze;
_leftEyePosition;
_rightEyePosition;
{?="columns"[3]} _rotation;
```

## Properties

```
@property (Td,N,V_localMachtime) localMachtime;
@property (Td,N,V_globalMachtime) globalMachtime;
@property (Ti,N,V_failureCode) failureCode;
@property (T@"NSString",N,V_failureDescription) failureDescription;
@property (TB,N,V_tooDark) tooDark;
@property (TB,N,V_sensorCovered) sensorCovered;
@property (Tf,N,V_confidence) confidence;
@property (T,N,V_translation) translation;
@property (T{?=[3]},N,V_rotation) rotation;
@property (T,N,V_gaze) gaze;
@property (T,N,V_leftEyePosition) leftEyePosition;
@property (T,N,V_rightEyePosition) rightEyePosition;
@property (T@"NSArray",&,N,V_blendShapeWeights) blendShapeWeights;
@property (Td,N,V_roll) roll;
```

## Instance methods

```
-[CMFacePose rotation];
-[CMFacePose setRotation:];
-[CMFacePose setConfidence:];
-[CMFacePose setTranslation:];
-[CMFacePose setFailureDescription:];
-[CMFacePose translation];
-[CMFacePose setSensorCovered:];
-[CMFacePose confidence];
-[CMFacePose roll];
-[CMFacePose setRoll:];
-[CMFacePose leftEyePosition];
-[CMFacePose rightEyePosition];
-[CMFacePose gaze];
-[CMFacePose setGaze:];
-[CMFacePose tooDark];
-[CMFacePose setFailureCode:];
-[CMFacePose blendShapeWeights];
-[CMFacePose failureCode];
-[CMFacePose failureDescription];
-[CMFacePose globalMachtime];
-[CMFacePose localMachtime];
-[CMFacePose sensorCovered];
-[CMFacePose setBlendShapeWeights:];
-[CMFacePose setGlobalMachtime:];
-[CMFacePose setLeftEyePosition:];
-[CMFacePose setLocalMachtime:];
-[CMFacePose setRightEyePosition:];
-[CMFacePose setTooDark:];
```
