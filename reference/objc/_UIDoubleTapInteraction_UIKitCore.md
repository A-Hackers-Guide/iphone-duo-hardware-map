# `_UIDoubleTapInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 13 instance variables, 17 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _ignoresUIControls;
B _neverRecognizeSimultaneouslyWithOtherGestures;
B _disableDoubleTapAction;
B _receivedTouchInRequiredToFailRegion;
@"UIView" _view;
@? _shouldContinueProcessingSecondTap;
@? _didDoubleTap;
@? _didTimeOut;
d _heightFromTopToAcceptTouches;
d _heightFromTopToFailOtherGestures;
@"_UIDoubleTapInteractionGestureRecognizer" _tapGesture;
@"UIDelayedAction" _doubleTapAction;
{CGPoint="x"d"y"d} _initialTapLocationInView;
```

## Properties

```
@property (TB,N,V_ignoresUIControls) ignoresUIControls;
@property (TB,N,V_neverRecognizeSimultaneouslyWithOtherGestures) neverRecognizeSimultaneouslyWithOtherGestures;
@property (Td,N,V_heightFromTopToAcceptTouches) heightFromTopToAcceptTouches;
@property (Td,N,V_heightFromTopToFailOtherGestures) heightFromTopToFailOtherGestures;
@property (TB,N,V_disableDoubleTapAction) disableDoubleTapAction;
@property (T@"_UIDoubleTapInteractionGestureRecognizer",&,N,V_tapGesture) tapGesture;
@property (T{CGPoint=dd},N,V_initialTapLocationInView) initialTapLocationInView;
@property (T@"UIDelayedAction",&,N,V_doubleTapAction) doubleTapAction;
@property (TB,N,V_receivedTouchInRequiredToFailRegion) receivedTouchInRequiredToFailRegion;
@property (T@?,C,N,V_shouldContinueProcessingSecondTap) shouldContinueProcessingSecondTap;
@property (T@?,C,N,V_didDoubleTap) didDoubleTap;
@property (T@?,C,N,V_didTimeOut) didTimeOut;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIDoubleTapInteraction resetState];
-[_UIDoubleTapInteraction _gestureRecognizerFailed:];
-[_UIDoubleTapInteraction heightFromTopToFailOtherGestures];
-[_UIDoubleTapInteraction gestureRecognizer:shouldReceiveTouch:];
-[_UIDoubleTapInteraction setShouldContinueProcessingSecondTap:];
-[_UIDoubleTapInteraction didDoubleTap];
-[_UIDoubleTapInteraction _gestureRecognizer:acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIDoubleTapInteraction _handleTap:];
-[_UIDoubleTapInteraction setDisableDoubleTapAction:];
-[_UIDoubleTapInteraction gestureRecognizer:shouldReceiveEvent:];
-[_UIDoubleTapInteraction _invalidateDoubleTap];
-[_UIDoubleTapInteraction setDoubleTapAction:];
-[_UIDoubleTapInteraction setDidTimeOut:];
-[_UIDoubleTapInteraction _gestureRecognizer:acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIDoubleTapInteraction _gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIDoubleTapInteraction doubleTapAction];
-[_UIDoubleTapInteraction doubleTapOccurredAtLocation:];
-[_UIDoubleTapInteraction heightFromTopToAcceptTouches];
-[_UIDoubleTapInteraction view];
-[_UIDoubleTapInteraction continueProcessingSecondTapAtLocation:];
-[_UIDoubleTapInteraction setReceivedTouchInRequiredToFailRegion:];
-[_UIDoubleTapInteraction setDidDoubleTap:];
-[_UIDoubleTapInteraction neverRecognizeSimultaneouslyWithOtherGestures];
-[_UIDoubleTapInteraction willMoveToView:];
-[_UIDoubleTapInteraction didTimeOut];
-[_UIDoubleTapInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIDoubleTapInteraction setHeightFromTopToAcceptTouches:];
-[_UIDoubleTapInteraction setInitialTapLocationInView:];
-[_UIDoubleTapInteraction setIgnoresUIControls:];
-[_UIDoubleTapInteraction tapGesture];
-[_UIDoubleTapInteraction initialTapLocationInView];
-[_UIDoubleTapInteraction ignoresUIControls];
-[_UIDoubleTapInteraction setHeightFromTopToFailOtherGestures:];
-[_UIDoubleTapInteraction setNeverRecognizeSimultaneouslyWithOtherGestures:];
-[_UIDoubleTapInteraction receivedTouchInRequiredToFailRegion];
-[_UIDoubleTapInteraction setTapGesture:];
-[_UIDoubleTapInteraction shouldContinueProcessingSecondTap];
-[_UIDoubleTapInteraction disableDoubleTapAction];
-[_UIDoubleTapInteraction didMoveToView:];
```
