# `SBHingeMotionUnintendedInteractionMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDevicePoseProviderObserver`
- 11 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBFDevicePoseProvider" _devicePoseProvider;
@"SBUnintendedInteractionSuppressionCoordinator" _unintendedInteractionSuppressionCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
B _hingeMotionPastThreshold;
@"<BSInvalidatable>" _interactionSuppressionAssertion;
@"<BSInvalidatable>" _strictTouchCoverageAssertion;
{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d} _referenceAngle;
@"SBHingeMotionDetectionSettings" _detectionSettings;
d _detectionWindowBeganTimestamp;
d _motionBeganTimestamp;
d _motionEndedTimestamp;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHingeMotionUnintendedInteractionMonitor dealloc];
-[SBHingeMotionUnintendedInteractionMonitor poseProvider:didUpdateFromPose:toPose:];
-[SBHingeMotionUnintendedInteractionMonitor _armDetectorWithAngle:];
-[SBHingeMotionUnintendedInteractionMonitor _resetDetector];
-[SBHingeMotionUnintendedInteractionMonitor _setHingeMotionPastThreshold:];
-[SBHingeMotionUnintendedInteractionMonitor _timestampForAngle:];
-[SBHingeMotionUnintendedInteractionMonitor initWithDevicePoseProvider:unintendedInteractionSuppressionCoordinator:lockScreenCoordinator:];
-[SBHingeMotionUnintendedInteractionMonitor wasHingeMovingBetweenTimestamp:andTimestamp:];
```
