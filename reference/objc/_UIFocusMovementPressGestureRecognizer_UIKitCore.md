# `_UIFocusMovementPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIRepeatingGestureClockDelegate`
- 5 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _shouldRepeat;
Q _focusHeading;
q _repeatCount;
@"_UIRepeatingGestureClock" _repeatingClock;
@"NSMutableOrderedSet" _trackedPresses;
```

## Properties

```
@property (T@"_UIRepeatingGestureClock",&,N,V_repeatingClock) repeatingClock;
@property (TB,R,N,G_isRecognizing) isRecognizing;
@property (TQ,N,V_focusHeading) focusHeading;
@property (T@"NSMutableOrderedSet",&,N,G_trackedPresses,S_setTrackedPresses:,V_trackedPresses) trackedPresses;
@property (TB,N,V_shouldRepeat) shouldRepeat;
@property (Tq,N,V_repeatCount) repeatCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusMovementPressGestureRecognizer shouldRepeat];
-[_UIFocusMovementPressGestureRecognizer shouldReceiveEvent:];
-[_UIFocusMovementPressGestureRecognizer setAllowedTouchTypes:];
-[_UIFocusMovementPressGestureRecognizer setRepeatCount:];
-[_UIFocusMovementPressGestureRecognizer repeatCount];
-[_UIFocusMovementPressGestureRecognizer pressesCancelled:withEvent:];
-[_UIFocusMovementPressGestureRecognizer setFocusHeading:];
-[_UIFocusMovementPressGestureRecognizer setShouldRepeat:];
-[_UIFocusMovementPressGestureRecognizer configureDefaults];
-[_UIFocusMovementPressGestureRecognizer pressesEnded:withEvent:];
-[_UIFocusMovementPressGestureRecognizer focusHeadingForPresses:];
-[_UIFocusMovementPressGestureRecognizer _isGestureType:];
-[_UIFocusMovementPressGestureRecognizer reset];
-[_UIFocusMovementPressGestureRecognizer focusHeading];
-[_UIFocusMovementPressGestureRecognizer initWithTarget:action:];
-[_UIFocusMovementPressGestureRecognizer pressesBegan:withEvent:];
-[_UIFocusMovementPressGestureRecognizer pressesChanged:withEvent:];
-[_UIFocusMovementPressGestureRecognizer initWithCoder:];
-[_UIFocusMovementPressGestureRecognizer _trackedPresses];
-[_UIFocusMovementPressGestureRecognizer _isRecognizing];
-[_UIFocusMovementPressGestureRecognizer _setTrackedPresses:];
-[_UIFocusMovementPressGestureRecognizer _startTrackingPresses:];
-[_UIFocusMovementPressGestureRecognizer _stopTrackingPresses:];
-[_UIFocusMovementPressGestureRecognizer _updateForPresses:action:];
-[_UIFocusMovementPressGestureRecognizer _verifyTrackingPresses:];
-[_UIFocusMovementPressGestureRecognizer repeatingClock];
-[_UIFocusMovementPressGestureRecognizer repeatingGestureClockDidTick:];
-[_UIFocusMovementPressGestureRecognizer setFocusHeading:omitStateUpdate:];
-[_UIFocusMovementPressGestureRecognizer setRepeatingClock:];
```
