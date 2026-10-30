# `_UIFeedbackStateChangeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _thresholdFeedback;
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _approachFeedback;
d _approachStart;
d _approachEnd;
d _approachCurvature;
d _approachVolumeMax;
@"NSString" _hidThresholdFeedbackPatternName;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_thresholdFeedback) thresholdFeedback;
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,V_approachFeedback) approachFeedback;
@property (Td,N,V_approachStart) approachStart;
@property (Td,N,V_approachEnd) approachEnd;
@property (Td,N,V_approachCurvature) approachCurvature;
@property (Td,N,V_approachVolumeMax) approachVolumeMax;
@property (T@"NSString",&,N,V_hidThresholdFeedbackPatternName) hidThresholdFeedbackPatternName;
```

## Instance methods

```
-[_UIFeedbackStateChangeConfiguration copyWithZone:];
-[_UIFeedbackStateChangeConfiguration isEqual:];
-[_UIFeedbackStateChangeConfiguration hidThresholdFeedbackPatternName];
-[_UIFeedbackStateChangeConfiguration setApproachEnd:];
-[_UIFeedbackStateChangeConfiguration approachCurvature];
-[_UIFeedbackStateChangeConfiguration approachEnd];
-[_UIFeedbackStateChangeConfiguration approachFeedback];
-[_UIFeedbackStateChangeConfiguration approachStart];
-[_UIFeedbackStateChangeConfiguration approachVolumeMax];
-[_UIFeedbackStateChangeConfiguration setApproachCurvature:];
-[_UIFeedbackStateChangeConfiguration setApproachFeedback:];
-[_UIFeedbackStateChangeConfiguration setApproachStart:];
-[_UIFeedbackStateChangeConfiguration setApproachVolumeMax:];
-[_UIFeedbackStateChangeConfiguration setHidThresholdFeedbackPatternName:];
-[_UIFeedbackStateChangeConfiguration setThresholdFeedback:];
-[_UIFeedbackStateChangeConfiguration thresholdFeedback];
```
