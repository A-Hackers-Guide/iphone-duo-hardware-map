# `_UIKeyboardTextSelectionGestureController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 25 properties, 75 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _deallocHandlers;
B _wasScrollingEnabled;
B _wasNestedPinchingDisabled;
B _suppressTwoFingerPan;
B _didSuppressSelectionGrabbers;
B _isLongPressing;
B _isPanning;
B _isSpacePan;
B _hadAddedTouch;
B _didFloatCursor;
i _previousForcePressCount;
@"<_UIKeyboardTextSelectionGestureControllerDelegate>" _delegate;
d _lastPressTimestamp;
@"UITextMagnifierTimeWeightedPoint" _weightedPoint;
d _twoFingerTapTimestamp;
q _previousRepeatedGranularity;
q _panGestureState;
d _spacePanDistance;
@"NSMutableArray" _activeGestures;
@"UIDelayedAction" _tapLogTimer;
@"UIDelayedAction" _longForcePressAction;
@"_UIStatesFeedbackGenerator" _feedbackBehaviour;
{CGPoint="x"d"y"d} _lastPanTranslation;
{CGPoint="x"d"y"d} _accumulatedAcceleration;
{CGPoint="x"d"y"d} _accumulatedBounding;
{CGPoint="x"d"y"d} _cursorLocationBase;
```

## Properties

```
@property (T{CGPoint=dd},N,V_lastPanTranslation) lastPanTranslation;
@property (T{CGPoint=dd},N,V_accumulatedAcceleration) accumulatedAcceleration;
@property (T{CGPoint=dd},N,V_accumulatedBounding) accumulatedBounding;
@property (Td,N,V_lastPressTimestamp) lastPressTimestamp;
@property (T@"UITextMagnifierTimeWeightedPoint",&,N,V_weightedPoint) weightedPoint;
@property (Td,N,V_twoFingerTapTimestamp) twoFingerTapTimestamp;
@property (Tq,N,V_previousRepeatedGranularity) previousRepeatedGranularity;
@property (Tq,N,V_panGestureState) panGestureState;
@property (TB,N,V_wasScrollingEnabled) wasScrollingEnabled;
@property (TB,N,V_wasNestedPinchingDisabled) wasNestedPinchingDisabled;
@property (TB,N,V_suppressTwoFingerPan) suppressTwoFingerPan;
@property (TB,N,V_didSuppressSelectionGrabbers) didSuppressSelectionGrabbers;
@property (TB,N,V_isLongPressing) isLongPressing;
@property (TB,N,V_isPanning) isPanning;
@property (TB,N,V_isSpacePan) isSpacePan;
@property (TB,N,V_hadAddedTouch) hadAddedTouch;
@property (Td,N,V_spacePanDistance) spacePanDistance;
@property (T@"NSMutableArray",&,N,V_activeGestures) activeGestures;
@property (TB,N,V_didFloatCursor) didFloatCursor;
@property (T{CGPoint=dd},N,V_cursorLocationBase) cursorLocationBase;
@property (T@"UIDelayedAction",&,N,V_tapLogTimer) tapLogTimer;
@property (Ti,N,V_previousForcePressCount) previousForcePressCount;
@property (T@"UIDelayedAction",&,N,V_longForcePressAction) longForcePressAction;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_feedbackBehaviour) feedbackBehaviour;
@property (T@"<_UIKeyboardTextSelectionGestureControllerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[_UIKeyboardTextSelectionGestureController sharedInstance];
```

## Instance methods

```
-[_UIKeyboardTextSelectionGestureController setTwoFingerTapTimestamp:];
-[_UIKeyboardTextSelectionGestureController setPreviousForcePressCount:];
-[_UIKeyboardTextSelectionGestureController didRemoveSelectionController];
-[_UIKeyboardTextSelectionGestureController weightedPoint];
-[_UIKeyboardTextSelectionGestureController oneFingerForcePressShouldFailWithoutForce];
-[_UIKeyboardTextSelectionGestureController removeDeallocationHandler:];
-[_UIKeyboardTextSelectionGestureController textSelectionInteractionForRTIForwarding];
-[_UIKeyboardTextSelectionGestureController init];
-[_UIKeyboardTextSelectionGestureController textInteractionClass];
-[_UIKeyboardTextSelectionGestureController cursorLocationBase];
-[_UIKeyboardTextSelectionGestureController feedbackBehaviour];
-[_UIKeyboardTextSelectionGestureController dealloc];
-[_UIKeyboardTextSelectionGestureController lastPanTranslation];
-[_UIKeyboardTextSelectionGestureController shouldAddForceGesture];
-[_UIKeyboardTextSelectionGestureController longForcePressAction];
-[_UIKeyboardTextSelectionGestureController configureTwoFingerPanGestureRecognizer:];
-[_UIKeyboardTextSelectionGestureController setLongForcePressAction:];
-[_UIKeyboardTextSelectionGestureController oneFingerForcePressShouldCancelTouchesInView];
-[_UIKeyboardTextSelectionGestureController didSuppressSelectionGrabbers];
-[_UIKeyboardTextSelectionGestureController willRemoveSelectionController];
-[_UIKeyboardTextSelectionGestureController previousForcePressCount];
-[_UIKeyboardTextSelectionGestureController suppressTwoFingerPan];
-[_UIKeyboardTextSelectionGestureController isSpacePan];
-[_UIKeyboardTextSelectionGestureController configureOneFingerForcePressRecognizer:];
-[_UIKeyboardTextSelectionGestureController isLongPressing];
-[_UIKeyboardTextSelectionGestureController setWeightedPoint:];
-[_UIKeyboardTextSelectionGestureController wasNestedPinchingDisabled];
-[_UIKeyboardTextSelectionGestureController setFeedbackBehaviour:];
-[_UIKeyboardTextSelectionGestureController setIsPanning:];
-[_UIKeyboardTextSelectionGestureController setDelegate:];
-[_UIKeyboardTextSelectionGestureController setSpacePanDistance:];
-[_UIKeyboardTextSelectionGestureController setWasNestedPinchingDisabled:];
-[_UIKeyboardTextSelectionGestureController panGestureState];
-[_UIKeyboardTextSelectionGestureController accumulatedAcceleration];
-[_UIKeyboardTextSelectionGestureController tapLogTimer];
-[_UIKeyboardTextSelectionGestureController setSuppressTwoFingerPan:];
-[_UIKeyboardTextSelectionGestureController selectionController];
-[_UIKeyboardTextSelectionGestureController addOneFingerTextSelectionInteractionsToView:];
-[_UIKeyboardTextSelectionGestureController configureTwoFingerTapGestureRecognizer:];
-[_UIKeyboardTextSelectionGestureController wasScrollingEnabled];
-[_UIKeyboardTextSelectionGestureController setPreviousRepeatedGranularity:];
-[_UIKeyboardTextSelectionGestureController setLastPanTranslation:];
-[_UIKeyboardTextSelectionGestureController redisableEnclosingScrollViewNestedPinching];
-[_UIKeyboardTextSelectionGestureController setLastPressTimestamp:];
-[_UIKeyboardTextSelectionGestureController activeGestures];
-[_UIKeyboardTextSelectionGestureController oneFingerForcePressAllowableMovement];
-[_UIKeyboardTextSelectionGestureController delegate];
-[_UIKeyboardTextSelectionGestureController hadAddedTouch];
-[_UIKeyboardTextSelectionGestureController setCursorLocationBase:];
-[_UIKeyboardTextSelectionGestureController addDeallocationHandler:];
-[_UIKeyboardTextSelectionGestureController setPanGestureState:];
-[_UIKeyboardTextSelectionGestureController twoFingerTapTimestamp];
-[_UIKeyboardTextSelectionGestureController addTwoFingerTextSelectionInteractionsToView:];
-[_UIKeyboardTextSelectionGestureController setIsSpacePan:];
-[_UIKeyboardTextSelectionGestureController didFloatCursor];
-[_UIKeyboardTextSelectionGestureController _cleanupDeadGesturesIfNecessary];
-[_UIKeyboardTextSelectionGestureController setHadAddedTouch:];
-[_UIKeyboardTextSelectionGestureController setActiveGestures:];
-[_UIKeyboardTextSelectionGestureController _longPressAllowedForView:];
-[_UIKeyboardTextSelectionGestureController setTapLogTimer:];
-[_UIKeyboardTextSelectionGestureController lastPressTimestamp];
-[_UIKeyboardTextSelectionGestureController setDidFloatCursor:];
-[_UIKeyboardTextSelectionGestureController addLongPressTextSelectionInteractionsToView:];
-[_UIKeyboardTextSelectionGestureController enableEnclosingScrollViewNestedPinching];
-[_UIKeyboardTextSelectionGestureController oneFingerForcePressMinimumDuration];
-[_UIKeyboardTextSelectionGestureController spacePanDistance];
-[_UIKeyboardTextSelectionGestureController setAccumulatedAcceleration:];
-[_UIKeyboardTextSelectionGestureController isPanning];
-[_UIKeyboardTextSelectionGestureController setIsLongPressing:];
-[_UIKeyboardTextSelectionGestureController allowOneFingerDeepPress];
-[_UIKeyboardTextSelectionGestureController accumulatedBounding];
-[_UIKeyboardTextSelectionGestureController setAccumulatedBounding:];
-[_UIKeyboardTextSelectionGestureController previousRepeatedGranularity];
-[_UIKeyboardTextSelectionGestureController setDidSuppressSelectionGrabbers:];
-[_UIKeyboardTextSelectionGestureController setWasScrollingEnabled:];
```
