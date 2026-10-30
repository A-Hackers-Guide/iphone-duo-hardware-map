# `ABPKBreakthroughResult`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"ABPK2dSkeleton" _skeleton2D;
I _trackingId;
B _isFaceVisible;
B _isRaisingHand;
B _isWavingHand;
B _isPoseValid;
```

## Properties

```
@property (T@"ABPK2dSkeleton",R,N) skeleton2D;
@property (TB,R,N,V_isPoseValid) isPoseValid;
@property (TI,R,N) trackingId;
@property (TB,R,N) isFaceVisible;
@property (TB,R,N) isRaisingHand;
@property (TB,R,N) isWavingHand;
```

## Instance methods

```
-[ABPKBreakthroughResult init];
-[ABPKBreakthroughResult trackingId];
-[ABPKBreakthroughResult skeleton2D];
-[ABPKBreakthroughResult isFaceVisible];
-[ABPKBreakthroughResult isPoseValid];
-[ABPKBreakthroughResult isRaisingHand];
-[ABPKBreakthroughResult isWavingHand];
-[ABPKBreakthroughResult overlayResultOnImage:withResult:withColor:];
-[ABPKBreakthroughResult set2dSkeleton:isPoseValid:trackingId:isFaceVisible:isRaisingHand:isWavingHand:];
```
