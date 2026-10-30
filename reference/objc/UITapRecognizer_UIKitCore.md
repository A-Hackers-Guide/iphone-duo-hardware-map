# `UITapRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 26 instance variables, 16 properties, 56 instance methods, 1 class methods

## Instance variables

```
Q _numberOfTouchesRequired;
Q _numberOfTapsRequired;
q _buttonMaskRequired;
@"NSMutableSet" _activeTouches;
{CGPoint="x"d"y"d} _startPoint;
{CGPoint="x"d"y"d} _digitizerLocation;
d _allowableMovement;
d _allowableSeparation;
d _allowableTouchTimeSeparation;
d _maximumTapDuration;
d _minimumTapDuration;
d _startTime;
d _maximumIntervalBetweenSuccessiveTaps;
@"NSMutableArray" _touches;
q _strongestDirectionalAxis;
d _strongestDirectionalForce;
i _currentNumberOfTouches;
i _currentNumberOfTaps;
i _numberOfTouchesForCurrentTap;
b1 _timerOn;
b1 _multitouchTimerOn;
b1 _hasPointerTouch;
B _countsOnlyActiveTouches;
B _continuousTapRecognition;
@"<UITapRecognizerDelegate>" _delegate;
q _exclusiveDirectionalAxis;
```

## Properties

```
@property (T@"<UITapRecognizerDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_numberOfTapsRequired) numberOfTapsRequired;
@property (TB,N) continuousTapRecognition;
@property (TQ,R,N) currentNumberOfTaps;
@property (TQ,N,V_numberOfTouchesRequired) numberOfTouchesRequired;
@property (Tq,N,V_buttonMaskRequired) buttonMaskRequired;
@property (Td,N) allowableMovement;
@property (Td,N) allowableSeparation;
@property (Td,N,V_allowableTouchTimeSeparation) allowableTouchTimeSeparation;
@property (Td,N,V_maximumTapDuration) maximumTapDuration;
@property (Td,N,V_minimumTapDuration) minimumTapDuration;
@property (Td,N) maximumIntervalBetweenSuccessiveTaps;
@property (TB,N,V_countsOnlyActiveTouches) countsOnlyActiveTouches;
@property (Tq,N,V_exclusiveDirectionalAxis) exclusiveDirectionalAxis;
@property (T@"NSArray",R,N,V_touches) touches;
@property (T@"NSSet",R,N) activeTouches;
```

## Class methods

```
+[UITapRecognizer supportsSecureCoding];
```

## Instance methods

```
-[UITapRecognizer numberOfTapsRequired];
-[UITapRecognizer allowableMovement];
-[UITapRecognizer tooSlow:];
-[UITapRecognizer touchesEnded:withEvent:];
-[UITapRecognizer locationInViewNotTrackingTouches:];
-[UITapRecognizer _beginInteraction];
-[UITapRecognizer _reset];
-[UITapRecognizer buttonMaskRequired];
-[UITapRecognizer touchesCancelled:withEvent:];
-[UITapRecognizer setMaximumIntervalBetweenSuccessiveTaps:];
-[UITapRecognizer setAllowableMovement:];
-[UITapRecognizer setContinuousTapRecognition:];
-[UITapRecognizer _locationInSceneReferenceSpace];
-[UITapRecognizer init];
-[UITapRecognizer setButtonMaskRequired:];
-[UITapRecognizer pressesCancelled:withEvent:];
-[UITapRecognizer pressesEnded:withEvent:];
-[UITapRecognizer setMinimumTapDuration:];
-[UITapRecognizer touches];
-[UITapRecognizer countsOnlyActiveTouches];
-[UITapRecognizer multitouchExpired:];
-[UITapRecognizer startTapTimer:];
-[UITapRecognizer clearTapTimer];
-[UITapRecognizer dealloc];
-[UITapRecognizer maximumIntervalBetweenSuccessiveTaps];
-[UITapRecognizer locationInView:focusSystem:];
-[UITapRecognizer maximumTapDuration];
-[UITapRecognizer touchesBegan:withEvent:];
-[UITapRecognizer touchesMoved:withEvent:];
-[UITapRecognizer allowableTouchTimeSeparation];
-[UITapRecognizer _interactionEndedTouch:];
-[UITapRecognizer locationInView:];
-[UITapRecognizer setNumberOfTapsRequired:];
-[UITapRecognizer pressesBegan:withEvent:];
-[UITapRecognizer pressesChanged:withEvent:];
-[UITapRecognizer activeTouchesExceedAllowableSeparation];
-[UITapRecognizer setNumberOfTouchesRequired:];
-[UITapRecognizer setDelegate:];
-[UITapRecognizer allowableSeparation];
-[UITapRecognizer _effectiveAllowableMovement];
-[UITapRecognizer startMultitouchTimer:];
-[UITapRecognizer setExclusiveDirectionalAxis:];
-[UITapRecognizer encodeWithCoder:];
-[UITapRecognizer setAllowableTouchTimeSeparation:];
-[UITapRecognizer clearMultitouchTimer];
-[UITapRecognizer delegate];
-[UITapRecognizer minimumTapDuration];
-[UITapRecognizer activeTouches];
-[UITapRecognizer initWithCoder:];
-[UITapRecognizer numberOfTouchesRequired];
-[UITapRecognizer currentNumberOfTaps];
-[UITapRecognizer exclusiveDirectionalAxis];
-[UITapRecognizer setAllowableSeparation:];
-[UITapRecognizer continuousTapRecognition];
-[UITapRecognizer setMaximumTapDuration:];
-[UITapRecognizer setCountsOnlyActiveTouches:];
```
