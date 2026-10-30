# `BKFaceDetectStateInfo`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _faceDetected;
B _tooCloseToCamera;
B _tooFarFromCamera;
B _multipleFaces;
B _flare;
B _occlusion;
B _partiallyOutOfView;
B _unsupportedGlasses;
B _glassesMismatch;
B _inadequateLight;
B _excessiveLight;
@"NSNumber" _pitch;
@"NSNumber" _yaw;
@"NSNumber" _roll;
@"NSNumber" _distance;
Q _orientation;
Q _eyeReliefStatus;
@"NSNumber" _isCameraObstructed;
@"NSNumber" _cameraObstructionScore;
@"NSNumber" _frameNumber;
@"NSNumber" _attentionScore;
@"NSNumber" _faceDetectionScore;
```

## Properties

```
@property (TB,N,V_faceDetected) faceDetected;
@property (TB,N,V_tooCloseToCamera) tooCloseToCamera;
@property (TB,N,V_tooFarFromCamera) tooFarFromCamera;
@property (TB,N,V_multipleFaces) multipleFaces;
@property (TB,N,V_flare) flare;
@property (TB,N,V_occlusion) occlusion;
@property (T@"NSNumber",&,N,V_pitch) pitch;
@property (T@"NSNumber",&,N,V_yaw) yaw;
@property (T@"NSNumber",&,N,V_roll) roll;
@property (T@"NSNumber",&,N,V_distance) distance;
@property (TQ,N,V_orientation) orientation;
@property (TQ,N,V_eyeReliefStatus) eyeReliefStatus;
@property (T@"NSNumber",R,N,V_isCameraObstructed) isCameraObstructed;
@property (T@"NSNumber",R,N,V_cameraObstructionScore) cameraObstructionScore;
@property (T@"NSNumber",R,N,V_frameNumber) frameNumber;
@property (T@"NSNumber",R,N,V_attentionScore) attentionScore;
@property (T@"NSNumber",R,N,V_faceDetectionScore) faceDetectionScore;
@property (TB,R,N,V_partiallyOutOfView) partiallyOutOfView;
@property (TB,R,N,V_unsupportedGlasses) unsupportedGlasses;
@property (TB,R,N,V_glassesMismatch) glassesMismatch;
@property (TB,R,N,V_inadequateLight) inadequateLight;
@property (TB,R,N,V_excessiveLight) excessiveLight;
```

## Instance methods

```
-[BKFaceDetectStateInfo pitch];
-[BKFaceDetectStateInfo setOrientation:];
-[BKFaceDetectStateInfo distance];
-[BKFaceDetectStateInfo yaw];
-[BKFaceDetectStateInfo setDistance:];
-[BKFaceDetectStateInfo setYaw:];
-[BKFaceDetectStateInfo orientation];
-[BKFaceDetectStateInfo initFromDictionary:];
-[BKFaceDetectStateInfo dictionary];
-[BKFaceDetectStateInfo setPitch:];
-[BKFaceDetectStateInfo roll];
-[BKFaceDetectStateInfo setRoll:];
-[BKFaceDetectStateInfo eyeReliefStatus];
-[BKFaceDetectStateInfo inadequateLight];
-[BKFaceDetectStateInfo attentionScore];
-[BKFaceDetectStateInfo cameraObstructionScore];
-[BKFaceDetectStateInfo excessiveLight];
-[BKFaceDetectStateInfo faceDetectionScore];
-[BKFaceDetectStateInfo flare];
-[BKFaceDetectStateInfo isCameraObstructed];
-[BKFaceDetectStateInfo multipleFaces];
-[BKFaceDetectStateInfo occlusion];
-[BKFaceDetectStateInfo tooCloseToCamera];
-[BKFaceDetectStateInfo tooFarFromCamera];
-[BKFaceDetectStateInfo frameNumber];
-[BKFaceDetectStateInfo setOcclusion:];
-[BKFaceDetectStateInfo faceDetected];
-[BKFaceDetectStateInfo setEyeReliefStatus:];
-[BKFaceDetectStateInfo glassesMismatch];
-[BKFaceDetectStateInfo initFromFaceInfo:];
-[BKFaceDetectStateInfo initWithPresenceState:];
-[BKFaceDetectStateInfo initWithPresenceState:details:];
-[BKFaceDetectStateInfo partiallyOutOfView];
-[BKFaceDetectStateInfo setFaceDetected:];
-[BKFaceDetectStateInfo setFlare:];
-[BKFaceDetectStateInfo setMultipleFaces:];
-[BKFaceDetectStateInfo setTooCloseToCamera:];
-[BKFaceDetectStateInfo setTooFarFromCamera:];
-[BKFaceDetectStateInfo unsupportedGlasses];
```
