# `_UIMotionAnalyzerSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISettings`
- 15 instance variables, 15 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _showIdleIndicator;
B _jumpEnabled;
B _playJumpSound;
B _directionalLockEnabled;
B _showDirectionalLockIndicators;
B _referenceShiftEnabled;
d _inputSmoothingFactor;
d _referenceShiftSpeed;
d _idleLeeway;
d _delayBeforeIdle;
d _jumpThreshold;
d _directionalLockThreshold;
d _directionalLockStickiness;
d _directionalLockSharpness;
d _referenceShiftDistanceDependence;
```

## Properties

```
@property (Td,V_idleLeeway) idleLeeway;
@property (Td,V_delayBeforeIdle) delayBeforeIdle;
@property (TB,V_showIdleIndicator) showIdleIndicator;
@property (TB,V_jumpEnabled) jumpEnabled;
@property (Td,V_jumpThreshold) jumpThreshold;
@property (TB,V_playJumpSound) playJumpSound;
@property (TB,V_directionalLockEnabled) directionalLockEnabled;
@property (Td,V_directionalLockThreshold) directionalLockThreshold;
@property (Td,V_directionalLockStickiness) directionalLockStickiness;
@property (Td,V_directionalLockSharpness) directionalLockSharpness;
@property (TB,V_showDirectionalLockIndicators) showDirectionalLockIndicators;
@property (TB,V_referenceShiftEnabled) referenceShiftEnabled;
@property (Td,V_referenceShiftDistanceDependence) referenceShiftDistanceDependence;
@property (Td,V_inputSmoothingFactor) inputSmoothingFactor;
@property (Td,V_referenceShiftSpeed) referenceShiftSpeed;
```

## Instance methods

```
-[_UIMotionAnalyzerSettings setReferenceShiftSpeed:];
-[_UIMotionAnalyzerSettings playJumpSound];
-[_UIMotionAnalyzerSettings directionalLockSharpness];
-[_UIMotionAnalyzerSettings referenceShiftDistanceDependence];
-[_UIMotionAnalyzerSettings setReferenceShiftEnabled:];
-[_UIMotionAnalyzerSettings inputSmoothingFactor];
-[_UIMotionAnalyzerSettings setDirectionalLockStickiness:];
-[_UIMotionAnalyzerSettings directionalLockStickiness];
-[_UIMotionAnalyzerSettings setDefaultValues];
-[_UIMotionAnalyzerSettings referenceShiftSpeed];
-[_UIMotionAnalyzerSettings referenceShiftEnabled];
-[_UIMotionAnalyzerSettings setJumpEnabled:];
-[_UIMotionAnalyzerSettings setInputSmoothingFactor:];
-[_UIMotionAnalyzerSettings directionalLockThreshold];
-[_UIMotionAnalyzerSettings setIdleLeeway:];
-[_UIMotionAnalyzerSettings setReferenceShiftDistanceDependence:];
-[_UIMotionAnalyzerSettings hash];
-[_UIMotionAnalyzerSettings directionalLockEnabled];
-[_UIMotionAnalyzerSettings jumpThreshold];
-[_UIMotionAnalyzerSettings setPlayJumpSound:];
-[_UIMotionAnalyzerSettings setJumpThreshold:];
-[_UIMotionAnalyzerSettings jumpEnabled];
-[_UIMotionAnalyzerSettings setDelayBeforeIdle:];
-[_UIMotionAnalyzerSettings idleLeeway];
-[_UIMotionAnalyzerSettings setDirectionalLockThreshold:];
-[_UIMotionAnalyzerSettings isEqual:];
-[_UIMotionAnalyzerSettings showDirectionalLockIndicators];
-[_UIMotionAnalyzerSettings setDirectionalLockEnabled:];
-[_UIMotionAnalyzerSettings showIdleIndicator];
-[_UIMotionAnalyzerSettings setDirectionalLockSharpness:];
-[_UIMotionAnalyzerSettings delayBeforeIdle];
-[_UIMotionAnalyzerSettings setShowDirectionalLockIndicators:];
-[_UIMotionAnalyzerSettings setShowIdleIndicator:];
```
