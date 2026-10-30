# `_UIPassthroughScrollInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPassthroughGestureDelegate`, `UIInteraction`
- 9 instance variables, 14 properties, 37 instance methods, 2 class methods

## Instance variables

```
B _recognizeOnPrimaryButtonDown;
B _recognizeOnSecondaryButtonDown;
B _eatsTouches;
B _configuredForInactiveInteractionEventsOnly;
@"UIView" _view;
@"UIView" _touchFallbackView;
@"_UIPassthroughScrollGestureRecognizer" _passthroughScrollGestureRecognizer;
@"_UIPassthroughGateGestureRecognizer" _gestureGate;
@"<_UIPassthroughScrollInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"UIView",R,N,V_touchFallbackView) _touchFallbackView;
@property (T@"_UIPassthroughScrollGestureRecognizer",R,N,V_passthroughScrollGestureRecognizer) _passthroughScrollGestureRecognizer;
@property (T@"_UIPassthroughGateGestureRecognizer",R,N,V_gestureGate) _gestureGate;
@property (T@"<_UIPassthroughScrollInteractionDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_recognizeOnPrimaryButtonDown) recognizeOnPrimaryButtonDown;
@property (TB,N,V_recognizeOnSecondaryButtonDown) recognizeOnSecondaryButtonDown;
@property (TB,N,V_eatsTouches) eatsTouches;
@property (TB,N) hitTestsAsOpaque;
@property (TB,N,V_configuredForInactiveInteractionEventsOnly) configuredForInactiveInteractionEventsOnly;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[_UIPassthroughScrollInteraction _isPassthroughGestureRecognizer:];
+[_UIPassthroughScrollInteraction _shouldEventBePassedThrough:];
```

## Instance methods

```
-[_UIPassthroughScrollInteraction _gestureRecognizerFailed:];
-[_UIPassthroughScrollInteraction _setOverrideAllowsHitTestingOnTouchFallbackView:];
-[_UIPassthroughScrollInteraction _handlePassthroughRecognizer:];
-[_UIPassthroughScrollInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UIPassthroughScrollInteraction configuredForInactiveInteractionEventsOnly];
-[_UIPassthroughScrollInteraction recognizeOnSecondaryButtonDown];
-[_UIPassthroughScrollInteraction recognizeOnPrimaryButtonDown];
-[_UIPassthroughScrollInteraction init];
-[_UIPassthroughScrollInteraction dealloc];
-[_UIPassthroughScrollInteraction _handlePassthroughGestureRecognizerEndWithReason:atLocation:];
-[_UIPassthroughScrollInteraction _didMoveFromWindow:toWindow:];
-[_UIPassthroughScrollInteraction setRecognizeOnPrimaryButtonDown:];
-[_UIPassthroughScrollInteraction _updateGesturesEatTouches];
-[_UIPassthroughScrollInteraction _delegateShouldInteractAtLocation:withEvent:];
-[_UIPassthroughScrollInteraction view];
-[_UIPassthroughScrollInteraction _touchFallbackView];
-[_UIPassthroughScrollInteraction setDelegate:];
-[_UIPassthroughScrollInteraction __forciblyEndWithReason:];
-[_UIPassthroughScrollInteraction _passthroughScrollGestureRecognizerShouldRequireFailureOfGestureRecognizer:];
-[_UIPassthroughScrollInteraction _setUpForWindow:];
-[_UIPassthroughScrollInteraction willMoveToView:];
-[_UIPassthroughScrollInteraction _gestureGate];
-[_UIPassthroughScrollInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIPassthroughScrollInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIPassthroughScrollInteraction delegate];
-[_UIPassthroughScrollInteraction hitTestsAsOpaque];
-[_UIPassthroughScrollInteraction _passthroughScrollGestureRecognizer];
-[_UIPassthroughScrollInteraction eatsTouches];
-[_UIPassthroughScrollInteraction description];
-[_UIPassthroughScrollInteraction setHitTestsAsOpaque:];
-[_UIPassthroughScrollInteraction _tearDown];
-[_UIPassthroughScrollInteraction _passthroughGestureRecognizer:shouldInteractAtLocation:withEvent:];
-[_UIPassthroughScrollInteraction setEatsTouches:];
-[_UIPassthroughScrollInteraction _delegatePassthroughInteractionDidRecognize:];
-[_UIPassthroughScrollInteraction setRecognizeOnSecondaryButtonDown:];
-[_UIPassthroughScrollInteraction didMoveToView:];
-[_UIPassthroughScrollInteraction setConfiguredForInactiveInteractionEventsOnly:];
```
