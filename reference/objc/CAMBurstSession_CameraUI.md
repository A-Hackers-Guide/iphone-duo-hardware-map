# `CAMBurstSession`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _finalized;
Q _estimatedCount;
Q _count;
@"CAMBurstImageSet" __burstImageSet;
```

## Properties

```
@property (TQ,N,S_setEstimatedCount:,V_estimatedCount) estimatedCount;
@property (TQ,N,S_setCount:,V_count) count;
@property (TB,N,G_isFinalized,S_setFinalized:,V_finalized) finalized;
@property (T@"CAMBurstImageSet",R,N,V__burstImageSet) _burstImageSet;
@property (T@"NSString",R,C,N) identifier;
```

## Instance methods

```
-[CAMBurstSession identifier];
-[CAMBurstSession init];
-[CAMBurstSession count];
-[CAMBurstSession description];
-[CAMBurstSession estimatedCount];
-[CAMBurstSession _setCount:];
-[CAMBurstSession _burstImageSet];
-[CAMBurstSession _isFinalized];
-[CAMBurstSession _setEstimatedCount:];
-[CAMBurstSession _setFinalized:];
-[CAMBurstSession addStillImageCaptureResult:];
-[CAMBurstSession addStillImageLocalPersistenceResult:withFaces:];
-[CAMBurstSession performBurstAnalysisForDevice:];
```
