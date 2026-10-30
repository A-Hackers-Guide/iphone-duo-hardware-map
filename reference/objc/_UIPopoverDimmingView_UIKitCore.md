# `_UIPopoverDimmingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDimmingView`
- Protocols: `_UIPassthroughScrollInteractionDelegate`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _lastHitTestWasPassedThrough;
B _passThroughDismissalTaps;
@"_UIPassthroughScrollInteraction" _passthroughScrollInteraction;
@"UIView" _transitionContainerView;
```

## Properties

```
@property (T@"_UIPassthroughScrollInteraction",R,N,V_passthroughScrollInteraction) _passthroughScrollInteraction;
@property (T@"<_UIPopoverDimmingViewDelegate>",W,D,N) delegate;
@property (T@"UIView",W,N,V_transitionContainerView) transitionContainerView;
@property (TB,N,V_passThroughDismissalTaps) passThroughDismissalTaps;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPopoverDimmingView _setOverrideAllowsHitTestingOnTouchFallbackView:];
-[_UIPopoverDimmingView didMoveToWindow];
-[_UIPopoverDimmingView hitTest:withEvent:];
-[_UIPopoverDimmingView passthroughScrollInteractionDidRecognize:atLocation:];
-[_UIPopoverDimmingView transitionContainerView];
-[_UIPopoverDimmingView passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UIPopoverDimmingView willMoveToWindow:];
-[_UIPopoverDimmingView setTransitionContainerView:];
-[_UIPopoverDimmingView _delegateAllowsInteraction];
-[_UIPopoverDimmingView _passthroughScrollInteraction];
-[_UIPopoverDimmingView _sendDelegateDimmingViewWasTapped];
-[_UIPopoverDimmingView _updatePassthroughInteraction];
-[_UIPopoverDimmingView passThroughDismissalTaps];
-[_UIPopoverDimmingView setPassThroughDismissalTaps:];
```
