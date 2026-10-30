# `BKUIFaceDetectStateInfo` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 13 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) faceDetected;
@property (T@"NSNumber",R,N) pitch;
@property (T@"NSNumber",R,N) yaw;
@property (T@"NSNumber",R,N) roll;
@property (TQ,R,N) orientation;
@property (TB,R,N) tooCloseToCamera;
@property (TB,R,N) tooFarFromCamera;
@property (TB,R,N) multipleFaces;
@property (TB,R,N) flare;
@property (TB,R,N) occlusion;
@property (TB,R,N) partiallyOutOfView;
@property (TB,R,N) unsupportedGlasses;
@property (TB,R,N) glassesMismatch;
```

## Instance methods

```
-[BKUIFaceDetectStateInfo pitch];
-[BKUIFaceDetectStateInfo yaw];
-[BKUIFaceDetectStateInfo orientation];
-[BKUIFaceDetectStateInfo roll];
-[BKUIFaceDetectStateInfo flare];
-[BKUIFaceDetectStateInfo multipleFaces];
-[BKUIFaceDetectStateInfo occlusion];
-[BKUIFaceDetectStateInfo tooCloseToCamera];
-[BKUIFaceDetectStateInfo tooFarFromCamera];
-[BKUIFaceDetectStateInfo faceDetected];
-[BKUIFaceDetectStateInfo glassesMismatch];
-[BKUIFaceDetectStateInfo partiallyOutOfView];
-[BKUIFaceDetectStateInfo unsupportedGlasses];
```
