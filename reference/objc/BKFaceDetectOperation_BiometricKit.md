# `BKFaceDetectOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKPresenceDetectOperation`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _highPriority;
B _eyeRelief;
B _motionDetect;
q _mode;
d _timeout;
```

## Properties

```
@property (Tq,N,V_mode) mode;
@property (Td,N,V_timeout) timeout;
@property (TB,N,V_highPriority) highPriority;
@property (TB,N,V_eyeRelief) eyeRelief;
@property (TB,N,V_motionDetect) motionDetect;
@property (T@"<BKFaceDetectOperationDelegate>",W,D,N) delegate;
```

## Instance methods

```
-[BKFaceDetectOperation statusMessage:client:];
-[BKFaceDetectOperation initWithDevice:];
-[BKFaceDetectOperation setHighPriority:];
-[BKFaceDetectOperation statusMessage:details:client:];
-[BKFaceDetectOperation eyeRelief];
-[BKFaceDetectOperation highPriority];
-[BKFaceDetectOperation setEyeRelief:];
-[BKFaceDetectOperation motionDetect];
-[BKFaceDetectOperation startBioOperation:reply:];
-[BKFaceDetectOperation timeout];
-[BKFaceDetectOperation setMode:];
-[BKFaceDetectOperation setMotionDetect:];
-[BKFaceDetectOperation setTimeout:];
-[BKFaceDetectOperation mode];
```
