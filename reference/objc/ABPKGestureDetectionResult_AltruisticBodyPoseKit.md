# `ABPKGestureDetectionResult`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"ABPK2dSkeleton" _skeleton2D;
I _trackingId;
@"NSArray" _gestureTypes;
B _isPoseValid;
```

## Properties

```
@property (T@"ABPK2dSkeleton",R,N,V_skeleton2D) skeleton2D;
@property (TB,R,N,V_isPoseValid) isPoseValid;
@property (TI,R,N,V_trackingId) trackingId;
@property (T@"NSArray",R,N,V_gestureTypes) gestureTypes;
```

## Instance methods

```
-[ABPKGestureDetectionResult init];
-[ABPKGestureDetectionResult trackingId];
-[ABPKGestureDetectionResult skeleton2D];
-[ABPKGestureDetectionResult gestureTypes];
-[ABPKGestureDetectionResult isPoseValid];
-[ABPKGestureDetectionResult overlayResultOnImage:withResult:withColor:];
-[ABPKGestureDetectionResult set2dSkeleton:isPoseValid:trackingId:gestureTypes:];
```
