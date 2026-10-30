# `SBMotionDetectionWakeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AMMotionDetectionTriggerManagerObserver`
- 5 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _enablementAssertions;
@"AMMotionDetectionTriggerManager" _triggerManager;
B _motionDetected;
B _enabled;
@"<SBMotionDetectionWakeControllerDelegate>" _delegate;
```

## Properties

```
@property (TB,N,G_isEnabled,S_setEnabled:,V_enabled) enabled;
@property (TB,N,GisMotionDetected,S_setMotionDetected:,V_motionDetected) motionDetected;
@property (T@"<SBMotionDetectionWakeControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMotionDetectionWakeController isMotionDetected];
-[SBMotionDetectionWakeController initWithDelegate:];
-[SBMotionDetectionWakeController _setEnabled:];
-[SBMotionDetectionWakeController _isEnabled];
-[SBMotionDetectionWakeController setDelegate:];
-[SBMotionDetectionWakeController delegate];
-[SBMotionDetectionWakeController _setMotionDetected:];
-[SBMotionDetectionWakeController acquireMotionDetectionWakeAssertionForReason:];
-[SBMotionDetectionWakeController motionDetectionManager:didUpdateMotionDetectionTriggerState:];
```
