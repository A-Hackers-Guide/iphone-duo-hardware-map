# `UIKeyboardCameraPadPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardCameraBasePresentationController`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 4 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<_UIAssertion>" _keyboardSuppressionAssertion;
@"UIView" _shadowView;
@"UIDimmingView" _dimmingView;
@"<UIDimmingViewDelegate>" _dimmingViewDelegate;
```

## Properties

```
@property (T@"<UIDimmingViewDelegate>",W,N,V_dimmingViewDelegate) dimmingViewDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardCameraPadPresentationController presentationTransitionDidEnd:];
-[UIKeyboardCameraPadPresentationController animateTransition:];
-[UIKeyboardCameraPadPresentationController transitionDuration:];
-[UIKeyboardCameraPadPresentationController updatesGuideDuringRotation];
-[UIKeyboardCameraPadPresentationController viewWillTransitionToSize:withTransitionCoordinator:];
-[UIKeyboardCameraPadPresentationController frameOfPresentedViewInContainerView];
-[UIKeyboardCameraPadPresentationController dismissalTransitionWillBegin];
-[UIKeyboardCameraPadPresentationController dismissalTransitionDidEnd:];
-[UIKeyboardCameraPadPresentationController presentationTransitionWillBegin];
-[UIKeyboardCameraPadPresentationController _animateDismissTransition:];
-[UIKeyboardCameraPadPresentationController _animatePresentTransition:];
-[UIKeyboardCameraPadPresentationController dimmingViewDelegate];
-[UIKeyboardCameraPadPresentationController overrideTextEffectsVisibilityLevelForTransitionView:];
-[UIKeyboardCameraPadPresentationController setDimmingViewDelegate:];
```
