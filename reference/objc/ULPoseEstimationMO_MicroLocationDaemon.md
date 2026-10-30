# `ULPoseEstimationMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 27 properties, 1 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",&,D,N) queryFrameIdentifier;
@property (Tq,D,N) queryFrameIndex;
@property (Ti,D,N) queryFrameCameraIdentifier;
@property (Td,D,N) queryFrameTimestamp;
@property (T@"NSSet",&,D,N) relativePoses;
@property (T@"ULLoiMO",&,D,N) loi;
@property (Tf,D,N) deviceMotionTranslationX;
@property (Tf,D,N) deviceMotionTranslationY;
@property (Tf,D,N) deviceMotionTranslationZ;
@property (Tf,D,N) deviceMotionAttitudeX;
@property (Tf,D,N) deviceMotionAttitudeY;
@property (Tf,D,N) deviceMotionAttitudeZ;
@property (Tf,D,N) deviceMotionAttitudeW;
@property (Td,D,N) deviceMotionTimestamp;
@property (TB,D,N) hasMorePending;
@property (Tq,D,N) batchGroupIndex;
@property (Tf,D,N) dualBudAttitudeDiffX;
@property (Tf,D,N) dualBudAttitudeDiffY;
@property (Tf,D,N) dualBudAttitudeDiffZ;
@property (Tf,D,N) dualBudAttitudeDiffW;
@property (Tf,D,N) gyroToGyroRotationX;
@property (Tf,D,N) gyroToGyroRotationY;
@property (Tf,D,N) gyroToGyroRotationZ;
@property (Tf,D,N) gyroToGyroRotationW;
@property (Tf,D,N) gyroToGyroTranslationX;
@property (Tf,D,N) gyroToGyroTranslationY;
@property (Tf,D,N) gyroToGyroTranslationZ;
```

## Class methods

```
+[ULPoseEstimationMO fetchRequest];
+[ULPoseEstimationMO createFromDO:withLoiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULPoseEstimationMO convertToDO];
```
