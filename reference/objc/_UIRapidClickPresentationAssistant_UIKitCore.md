# `_UIRapidClickPresentationAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitioningDelegate`, `UIViewControllerAnimatedTransitioning`, `_UIClickPresentationAssisting`
- 9 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
i _animationCount;
B _isInteractionInitiatedDismiss;
B _didBeginPresentation;
@"_UIClickPresentation" presentation;
@? lifecycleCompletion;
@? keyboardAssertionInvalidationHandler;
@"UITargetedPreview" _sourcePreview;
@ _keyboardSuppressionAssertion;
@"NSTimer" _animationWatchdogTimer;
```

## Properties

```
@property (T@"UITargetedPreview",&,N,V_sourcePreview) sourcePreview;
@property (T@,&,N,V_keyboardSuppressionAssertion) keyboardSuppressionAssertion;
@property (T@"NSTimer",W,N,V_animationWatchdogTimer) animationWatchdogTimer;
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
-[_UIRapidClickPresentationAssistant _firstResponderDidChange:];
-[_UIRapidClickPresentationAssistant _animateUsingFluidSpringWithType:animations:completion:];
-[_UIRapidClickPresentationAssistant animationControllerForDismissedController:];
-[_UIRapidClickPresentationAssistant setAnimationWatchdogTimer:];
-[_UIRapidClickPresentationAssistant presentation];
-[_UIRapidClickPresentationAssistant setPresentation:];
-[_UIRapidClickPresentationAssistant animateTransition:];
-[_UIRapidClickPresentationAssistant transitionDuration:];
-[_UIRapidClickPresentationAssistant presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIRapidClickPresentationAssistant sourcePreview];
-[_UIRapidClickPresentationAssistant dealloc];
-[_UIRapidClickPresentationAssistant dismissWithReason:alongsideActions:completion:];
-[_UIRapidClickPresentationAssistant keyboardSuppressionAssertion];
-[_UIRapidClickPresentationAssistant _nonAnimatedDismissalWithReason:actions:completion:];
-[_UIRapidClickPresentationAssistant setKeyboardSuppressionAssertion:];
-[_UIRapidClickPresentationAssistant setLifecycleCompletion:];
-[_UIRapidClickPresentationAssistant presentFromSourcePreview:lifecycleCompletion:];
-[_UIRapidClickPresentationAssistant initWithClickPresentation:];
-[_UIRapidClickPresentationAssistant setSourcePreview:];
-[_UIRapidClickPresentationAssistant setKeyboardAssertionInvalidationHandler:];
-[_UIRapidClickPresentationAssistant animationWatchdogTimer];
-[_UIRapidClickPresentationAssistant _performPresentationAnimationsFromViewController:];
-[_UIRapidClickPresentationAssistant _animateDismissalWithReason:actions:completion:];
-[_UIRapidClickPresentationAssistant keyboardAssertionInvalidationHandler];
-[_UIRapidClickPresentationAssistant lifecycleCompletion];
```
