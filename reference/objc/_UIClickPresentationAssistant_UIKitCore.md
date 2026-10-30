# `_UIClickPresentationAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitioningDelegate`, `UIViewControllerAnimatedTransitioning`, `_UIClickPresentationAssisting`
- 11 instance variables, 13 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerContextTransitioning>" _currentContext;
Q _currentState;
@"UIViewPropertyAnimator" _presentationAnimator;
@"_UIClickPresentation" presentation;
@? lifecycleCompletion;
@? keyboardAssertionInvalidationHandler;
@"_UIPortalView" _presentationSourcePortalView;
@"UITargetedPreview" _sourcePreview;
@"UIViewController" _stashedParentViewController;
@"UIView" _stashedSuperView;
@? _transitionCompletion;
```

## Properties

```
@property (T@"_UIPortalView",&,N,V_presentationSourcePortalView) presentationSourcePortalView;
@property (T@"UITargetedPreview",&,N,V_sourcePreview) sourcePreview;
@property (T@"UIViewController",&,N,V_stashedParentViewController) stashedParentViewController;
@property (T@"UIView",&,N,V_stashedSuperView) stashedSuperView;
@property (T@?,C,N,V_transitionCompletion) transitionCompletion;
@property (T@"UIViewPropertyAnimator",R,N,V_presentationAnimator) presentationAnimator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIClickPresentation",&,N,Vpresentation) presentation;
@property (T@?,C,N,VlifecycleCompletion) lifecycleCompletion;
@property (T@?,C,N,VkeyboardAssertionInvalidationHandler) keyboardAssertionInvalidationHandler;
```

## Instance methods

```
-[_UIClickPresentationAssistant animationControllerForDismissedController:];
-[_UIClickPresentationAssistant presentation];
-[_UIClickPresentationAssistant setPresentation:];
-[_UIClickPresentationAssistant animateTransition:];
-[_UIClickPresentationAssistant animationControllerForPresentedController:presentingController:sourceController:];
-[_UIClickPresentationAssistant transitionDuration:];
-[_UIClickPresentationAssistant presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIClickPresentationAssistant sourcePreview];
-[_UIClickPresentationAssistant dismissWithReason:alongsideActions:completion:];
-[_UIClickPresentationAssistant setLifecycleCompletion:];
-[_UIClickPresentationAssistant presentFromSourcePreview:lifecycleCompletion:];
-[_UIClickPresentationAssistant initWithClickPresentation:];
-[_UIClickPresentationAssistant setSourcePreview:];
-[_UIClickPresentationAssistant setKeyboardAssertionInvalidationHandler:];
-[_UIClickPresentationAssistant keyboardAssertionInvalidationHandler];
-[_UIClickPresentationAssistant lifecycleCompletion];
-[_UIClickPresentationAssistant setStashedParentViewController:];
-[_UIClickPresentationAssistant _animateDismissalIsInterruption:];
-[_UIClickPresentationAssistant _animatePresentation];
-[_UIClickPresentationAssistant _applyStashedParentViewControllerIfNecessary];
-[_UIClickPresentationAssistant _createPropertyAnimatorIfNecessaryForTransition:isAppearing:];
-[_UIClickPresentationAssistant _didTransitionToDismissingFromState:];
-[_UIClickPresentationAssistant _didTransitionToPossibleEndingTransition:];
-[_UIClickPresentationAssistant _didTransitionToPresented];
-[_UIClickPresentationAssistant _didTransitionToPresenting];
-[_UIClickPresentationAssistant _postInteractionCleanup];
-[_UIClickPresentationAssistant _sourcePreviewPortal];
-[_UIClickPresentationAssistant _stashParentViewControllerIfNecessary];
-[_UIClickPresentationAssistant presentationAnimator];
-[_UIClickPresentationAssistant presentationSourcePortalView];
-[_UIClickPresentationAssistant setPresentationSourcePortalView:];
-[_UIClickPresentationAssistant setStashedSuperView:];
-[_UIClickPresentationAssistant setTransitionCompletion:];
-[_UIClickPresentationAssistant stashedParentViewController];
-[_UIClickPresentationAssistant stashedSuperView];
-[_UIClickPresentationAssistant transitionCompletion];
```
