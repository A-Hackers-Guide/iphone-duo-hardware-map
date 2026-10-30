# `_UIProgressiveBlurPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- 2 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
q _blurStyle;
@"UIVisualEffectView" _visualEffectView;
```

## Properties

```
@property (T@"UIVisualEffectView",R,N,V_visualEffectView) visualEffectView;
@property (Tq,N,V_blurStyle) blurStyle;
```

## Instance methods

```
-[_UIProgressiveBlurPresentationController visualEffectView];
-[_UIProgressiveBlurPresentationController presentationStyle];
-[_UIProgressiveBlurPresentationController initWithPresentedViewController:presentingViewController:];
-[_UIProgressiveBlurPresentationController _mayChildGrabPresentedViewControllerView];
-[_UIProgressiveBlurPresentationController dismissalTransitionWillBegin];
-[_UIProgressiveBlurPresentationController presentationTransitionWillBegin];
-[_UIProgressiveBlurPresentationController _animateWithCoordinator:isPresenting:];
-[_UIProgressiveBlurPresentationController _configureSubviews];
-[_UIProgressiveBlurPresentationController _forcesPreferredAnimationControllers];
-[_UIProgressiveBlurPresentationController _preferredAnimationControllerForDismissal];
-[_UIProgressiveBlurPresentationController _preferredAnimationControllerForPresentation];
-[_UIProgressiveBlurPresentationController blurStyle];
-[_UIProgressiveBlurPresentationController setBlurStyle:];
```
