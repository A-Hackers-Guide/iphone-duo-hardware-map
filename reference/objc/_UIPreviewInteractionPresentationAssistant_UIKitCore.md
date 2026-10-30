# `_UIPreviewInteractionPresentationAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitioningDelegate`, `UIViewControllerAnimatedTransitioning`
- 10 instance variables, 13 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerContextTransitioning>" _currentContext;
B _isAppearing;
@"UIViewPropertyAnimator" _presentationAnimator;
@"_UIPreviewInteractionHighlighter" _highlighter;
@"_UIPreviewInteractionViewControllerPresentation" _presentation;
@"_UIPortalView" _presentationSourcePortalView;
@"UITargetedPreview" _sourcePreview;
@"UIViewController" _stashedParentViewController;
@"UIView" _stashedSuperView;
@? _dismissalCompletion;
```

## Properties

```
@property (T@"_UIPreviewInteractionViewControllerPresentation",&,N,V_presentation) presentation;
@property (T@"_UIPortalView",&,N,V_presentationSourcePortalView) presentationSourcePortalView;
@property (T@"UITargetedPreview",&,N,V_sourcePreview) sourcePreview;
@property (T@"UIViewController",&,N,V_stashedParentViewController) stashedParentViewController;
@property (T@"UIView",&,N,V_stashedSuperView) stashedSuperView;
@property (T@?,C,N,V_dismissalCompletion) dismissalCompletion;
@property (TB,N,V_isAppearing) isAppearing;
@property (T@"UIViewPropertyAnimator",R,N,V_presentationAnimator) presentationAnimator;
@property (T@"_UIPreviewInteractionHighlighter",&,N,V_highlighter) highlighter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionPresentationAssistant animationControllerForDismissedController:];
-[_UIPreviewInteractionPresentationAssistant presentation];
-[_UIPreviewInteractionPresentationAssistant setPresentation:];
-[_UIPreviewInteractionPresentationAssistant animateTransition:];
-[_UIPreviewInteractionPresentationAssistant animationControllerForPresentedController:presentingController:sourceController:];
-[_UIPreviewInteractionPresentationAssistant transitionDuration:];
-[_UIPreviewInteractionPresentationAssistant presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIPreviewInteractionPresentationAssistant sourcePreview];
-[_UIPreviewInteractionPresentationAssistant setIsAppearing:];
-[_UIPreviewInteractionPresentationAssistant isAppearing];
-[_UIPreviewInteractionPresentationAssistant setSourcePreview:];
-[_UIPreviewInteractionPresentationAssistant setHighlighter:];
-[_UIPreviewInteractionPresentationAssistant setStashedParentViewController:];
-[_UIPreviewInteractionPresentationAssistant _applyStashedParentViewControllerIfNecessary];
-[_UIPreviewInteractionPresentationAssistant _createpresentationAnimatorIfNecessary:];
-[_UIPreviewInteractionPresentationAssistant _postInteractionCleanup];
-[_UIPreviewInteractionPresentationAssistant _sourcePreviewPortal];
-[_UIPreviewInteractionPresentationAssistant _stashParentViewControllerIfNecessary];
-[_UIPreviewInteractionPresentationAssistant dismissViewController];
-[_UIPreviewInteractionPresentationAssistant dismissalCompletion];
-[_UIPreviewInteractionPresentationAssistant highlighter];
-[_UIPreviewInteractionPresentationAssistant initWithViewControllerPresentation:];
-[_UIPreviewInteractionPresentationAssistant presentFromViewController:sourcePreview:dismissalCompletion:];
-[_UIPreviewInteractionPresentationAssistant presentationAnimator];
-[_UIPreviewInteractionPresentationAssistant presentationSourcePortalView];
-[_UIPreviewInteractionPresentationAssistant setDismissalCompletion:];
-[_UIPreviewInteractionPresentationAssistant setPresentationSourcePortalView:];
-[_UIPreviewInteractionPresentationAssistant setStashedSuperView:];
-[_UIPreviewInteractionPresentationAssistant stashedParentViewController];
-[_UIPreviewInteractionPresentationAssistant stashedSuperView];
```
