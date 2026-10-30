# `CMMagicPoseEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 1 instance variables, 10 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"CMDeviceStateEvent" _event;
```

## Properties

```
@property (Tq,R,N) deviceOrientation;
@property (Tq,R,N) deviceOrientation0;
@property (Tq,R,N) deviceOrientation1;
@property (Tq,R,N) hingeState;
@property (Tq,R,N) tabletopPose;
@property (Tq,R,N) stableOrientationState;
@property (TB,R,N) progressValid;
@property (Tq,R,N) fromHingeState;
@property (Tq,R,N) toHingeState;
@property (Td,R,N) progressValue;
```

## Class methods

```
+[CMMagicPoseEvent stringForDeviceOrientation:];
+[CMMagicPoseEvent stringForHingeState:];
+[CMMagicPoseEvent stringForStableOrientationState:];
+[CMMagicPoseEvent stringForTabletopPose:];
```

## Instance methods

```
-[CMMagicPoseEvent deviceOrientation];
-[CMMagicPoseEvent dealloc];
-[CMMagicPoseEvent description];
-[CMMagicPoseEvent hingeState];
-[CMMagicPoseEvent progressValue];
-[CMMagicPoseEvent deviceOrientation0];
-[CMMagicPoseEvent deviceOrientation1];
-[CMMagicPoseEvent fromHingeState];
-[CMMagicPoseEvent initWithDeviceOrientation:deviceOrientation0:deviceOrientation1:hingeState:tabletopPose:stableOrientationState:timestamp:continuousTimestamp:];
-[CMMagicPoseEvent initWithDeviceOrientation:hingeState:tabletopPose:stableOrientationState:timestamp:continuousTimestamp:];
-[CMMagicPoseEvent initWithDeviceOrientation:hingeState:tabletopPose:timestamp:continuousTimestamp:];
-[CMMagicPoseEvent progressValid];
-[CMMagicPoseEvent stableOrientationState];
-[CMMagicPoseEvent tabletopPose];
-[CMMagicPoseEvent toHingeState];
```
