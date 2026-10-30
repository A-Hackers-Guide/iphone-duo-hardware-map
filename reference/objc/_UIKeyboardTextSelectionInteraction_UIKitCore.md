# `_UIKeyboardTextSelectionInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteraction`
- Protocols: `_UIPanOrFlickGestureRecognizerDelegate`
- 8 instance variables, 4 properties, 68 instance methods, 1 class methods

## Instance variables

```
@"_UIKeyboardTextSelectionGestureController" _owner;
@"NSMapTable" _weakMap;
@ _deallocToken;
@"_UITouchesObservingGestureRecognizer" _addedTouchRecognizer;
@"NSTimer" _touchPadTimer;
@? _touchPadTimerCompletion;
@"_UIPanOrFlickGestureRecognizer" _activePress;
@"_UIKeyboardIndirectTextSelectionGestureState" _previousRemoteGestureState;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIKeyboardTextSelectionInteraction attachToExistingRecogniser:owner:forType:];
```

## Instance methods

```
-[_UIKeyboardTextSelectionInteraction handleRemoteIndirectGestureWithState:];
-[_UIKeyboardTextSelectionInteraction _gestureRecognizerFailed:];
-[_UIKeyboardTextSelectionInteraction owner];
-[_UIKeyboardTextSelectionInteraction _prepareForGesture];
-[_UIKeyboardTextSelectionInteraction hideRecogniser:forKey:];
-[_UIKeyboardTextSelectionInteraction acceleratedTranslation:velocity:isActive:];
-[_UIKeyboardTextSelectionInteraction layoutDirectionFromFlickDirection:];
-[_UIKeyboardTextSelectionInteraction registerOwner:];
-[_UIKeyboardTextSelectionInteraction _logTapCounts:];
-[_UIKeyboardTextSelectionInteraction gestureRecognizer:shouldReceiveTouch:];
-[_UIKeyboardTextSelectionInteraction finishLongPressWithExecutionContext:];
-[_UIKeyboardTextSelectionInteraction removeTemporaryGesture];
-[_UIKeyboardTextSelectionInteraction indirectPanGestureWithState:withTranslation:withFlickDirection:isShiftKeyBeingHeld:];
-[_UIKeyboardTextSelectionInteraction dealloc];
-[_UIKeyboardTextSelectionInteraction endLongPressWithExecutionContext:];
-[_UIKeyboardTextSelectionInteraction hideInsideRecogniser:];
-[_UIKeyboardTextSelectionInteraction cancelLongPressWithExecutionContext:];
-[_UIKeyboardTextSelectionInteraction _configureTwoFingerTapGestureRecognizer:];
-[_UIKeyboardTextSelectionInteraction detach];
-[_UIKeyboardTextSelectionInteraction indirectCursorPanGestureWithState:withTranslation:withFlickDirection:];
-[_UIKeyboardTextSelectionInteraction beginLongPressWithTranslation:touchCount:executionContext:];
-[_UIKeyboardTextSelectionInteraction _clearHiding];
-[_UIKeyboardTextSelectionInteraction cursorLocationForTranslation:];
-[_UIKeyboardTextSelectionInteraction oneFingerForcePan:];
-[_UIKeyboardTextSelectionInteraction cancelTwoFingerPanWithExecutionContext:];
-[_UIKeyboardTextSelectionInteraction indirectBlockPanGestureWithState:withTranslation:];
-[_UIKeyboardTextSelectionInteraction panningGesture:];
-[_UIKeyboardTextSelectionInteraction handleTwoFingerFlickInDirection:executionContext:];
-[_UIKeyboardTextSelectionInteraction oneFingerForcePress:];
-[_UIKeyboardTextSelectionInteraction gestureRecognizerShouldBegin:];
-[_UIKeyboardTextSelectionInteraction _tidyUpGesture];
-[_UIKeyboardTextSelectionInteraction updateIndirectBlockPanWithTranslation:executionContext:];
-[_UIKeyboardTextSelectionInteraction selectionController];
-[_UIKeyboardTextSelectionInteraction beginCursorManipulationFromRect:];
-[_UIKeyboardTextSelectionInteraction panningGestureAddedTouch:];
-[_UIKeyboardTextSelectionInteraction clearKeyboardTouchesForGesture:];
-[_UIKeyboardTextSelectionInteraction _configureLongPressRecognizer:];
-[_UIKeyboardTextSelectionInteraction longPressGestureWithState:withTranslation:touchCount:];
-[_UIKeyboardTextSelectionInteraction forwardIndirectGestureWithType:state:translation:flickDirection:touchCount:];
-[_UIKeyboardTextSelectionInteraction _cancelTouchPadTimer];
-[_UIKeyboardTextSelectionInteraction _willBeginIndirectSelectionGesture:];
-[_UIKeyboardTextSelectionInteraction additionalPressDurationForTypingCadence:];
-[_UIKeyboardTextSelectionInteraction isPlacedCarefully];
-[_UIKeyboardTextSelectionInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIKeyboardTextSelectionInteraction initWithView:owner:forTypes:];
-[_UIKeyboardTextSelectionInteraction gestures];
-[_UIKeyboardTextSelectionInteraction beginTwoFingerPanWithTranslation:isShiftKeyBeingHeld:executionContext:];
-[_UIKeyboardTextSelectionInteraction _clearTouchPadCallback];
-[_UIKeyboardTextSelectionInteraction boundedTranslation:];
-[_UIKeyboardTextSelectionInteraction _configureOneFingerForcePressRecognizer:];
-[_UIKeyboardTextSelectionInteraction _longForcePressDetected:];
-[_UIKeyboardTextSelectionInteraction endIndirectBlockPanWithExecutionContext:];
-[_UIKeyboardTextSelectionInteraction _granularityExpandingGestureWithTimeInterval:timeGranularity:isMidPan:];
-[_UIKeyboardTextSelectionInteraction endTwoFingerPanWithExecutionContext:];
-[_UIKeyboardTextSelectionInteraction _beginLongForcePressTimerForGesture:];
-[_UIKeyboardTextSelectionInteraction _configureTwoFingerPanGestureRecognizer:];
-[_UIKeyboardTextSelectionInteraction twoFingerTap:];
-[_UIKeyboardTextSelectionInteraction gestureRecognizerShouldBeginResponse:];
-[_UIKeyboardTextSelectionInteraction updateTwoFingerPanWithTranslation:executionContext:];
-[_UIKeyboardTextSelectionInteraction _configureLongPressAddedTouchRecognizer:];
-[_UIKeyboardTextSelectionInteraction updateLongPressWithTranslation:executionContext:];
-[_UIKeyboardTextSelectionInteraction beginIndirectBlockPanWithTranslation:executionContext:];
-[_UIKeyboardTextSelectionInteraction forceTouchGestureRecognizerShouldBegin:];
-[_UIKeyboardTextSelectionInteraction disableEnclosingScrollViewScrolling];
-[_UIKeyboardTextSelectionInteraction _didEndIndirectSelectionGesture:];
-[_UIKeyboardTextSelectionInteraction _cancelLongForcePressTimer];
-[_UIKeyboardTextSelectionInteraction _startTouchPadTimerWithCompletion:];
-[_UIKeyboardTextSelectionInteraction beginTwoFingerCursorPanWithTranslation:executionContext:];
```
