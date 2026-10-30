# `_UIPreviewInteractionViewControllerHelper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitioningDelegate`, `UIViewControllerAnimatedTransitioning`, `UIPreviewPresentationControllerDelegate`
- 10 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_UIPreviewInteractionHighlighter" _highlighter;
@"_UIPreviewInteractionViewControllerPresentation" _viewControllerPresentation;
@"UIWindow" _presentingWindow;
@? _presentationCompletion;
@? _dismissalCompletion;
B _shouldActAsAppearanceAnimationController;
B _shouldUseDefaultPresentationController;
@"UIViewController" _previousParentViewController;
@"UIView" _previousSuperview;
@"<UIViewControllerContextTransitioning>" _currentTransitionContext;
```

## Properties

```
@property (T@"_UIPreviewInteractionViewControllerPresentation",R,N,V_viewControllerPresentation) viewControllerPresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionViewControllerHelper animationControllerForDismissedController:];
-[_UIPreviewInteractionViewControllerHelper animateTransition:];
-[_UIPreviewInteractionViewControllerHelper animationControllerForPresentedController:presentingController:sourceController:];
-[_UIPreviewInteractionViewControllerHelper transitionDuration:];
-[_UIPreviewInteractionViewControllerHelper presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIPreviewInteractionViewControllerHelper _finalizeAfterViewControllerPresentation];
-[_UIPreviewInteractionViewControllerHelper _performDismissalCompletionIfNeeded];
-[_UIPreviewInteractionViewControllerHelper _performPresentViewControllerFromViewController:];
-[_UIPreviewInteractionViewControllerHelper customPresentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIPreviewInteractionViewControllerHelper defaultPresentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIPreviewInteractionViewControllerHelper dismissViewController];
-[_UIPreviewInteractionViewControllerHelper initWithViewControllerPresentation:];
-[_UIPreviewInteractionViewControllerHelper presentViewControllerFromViewController:highlighter:presentationCompletion:dismissalCompletion:];
-[_UIPreviewInteractionViewControllerHelper previewPresentationController:shouldDismissViewController:];
-[_UIPreviewInteractionViewControllerHelper viewControllerPresentation];
```
