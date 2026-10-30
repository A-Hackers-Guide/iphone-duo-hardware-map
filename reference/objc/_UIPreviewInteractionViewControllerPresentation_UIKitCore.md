# `_UIPreviewInteractionViewControllerPresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _shouldUseCATransitions;
B _shouldFlipFromAndToViewsForDisappearanceTransition;
B _shouldUpdateFromViewBeforePresentation;
B _shouldPresentAutomatically;
@"UIViewController" _viewController;
@"UIView" _customContainerView;
@"UIPreviewPresentationController" _presentationController;
@"<_UIPreviewInteractionViewControllerTransition>" _appearanceTransition;
@"<_UIPreviewInteractionViewControllerTransition>" _disappearanceTransition;
@? _privatePresentationBlock;
@? _privatePresentationCompletionBlock;
@"UIView" _customViewForTouchContinuation;
```

## Properties

```
@property (T@"UIViewController",&,N,V_viewController) viewController;
@property (TB,N,V_shouldUseCATransitions) shouldUseCATransitions;
@property (TB,N,V_shouldFlipFromAndToViewsForDisappearanceTransition) shouldFlipFromAndToViewsForDisappearanceTransition;
@property (T@?,C,N,V_privatePresentationBlock) privatePresentationBlock;
@property (T@?,C,N,V_privatePresentationCompletionBlock) privatePresentationCompletionBlock;
@property (TB,N,V_shouldUpdateFromViewBeforePresentation) shouldUpdateFromViewBeforePresentation;
@property (T@"UIView",W,N,V_customViewForTouchContinuation) customViewForTouchContinuation;
@property (TB,N,V_shouldPresentAutomatically) shouldPresentAutomatically;
@property (T@"UIView",&,N,V_customContainerView) customContainerView;
@property (T@"UIPreviewPresentationController",&,N,V_presentationController) presentationController;
@property (T@"<_UIPreviewInteractionViewControllerTransition>",&,N,V_appearanceTransition) appearanceTransition;
@property (T@"<_UIPreviewInteractionViewControllerTransition>",&,N,V_disappearanceTransition) disappearanceTransition;
```

## Instance methods

```
-[_UIPreviewInteractionViewControllerPresentation setViewController:];
-[_UIPreviewInteractionViewControllerPresentation initWithViewController:];
-[_UIPreviewInteractionViewControllerPresentation presentViewController];
-[_UIPreviewInteractionViewControllerPresentation viewController];
-[_UIPreviewInteractionViewControllerPresentation presentationController];
-[_UIPreviewInteractionViewControllerPresentation setPresentationController:];
-[_UIPreviewInteractionViewControllerPresentation _completeViewControllerPresentationImmediately];
-[_UIPreviewInteractionViewControllerPresentation appearanceTransition];
-[_UIPreviewInteractionViewControllerPresentation customContainerView];
-[_UIPreviewInteractionViewControllerPresentation customViewForTouchContinuation];
-[_UIPreviewInteractionViewControllerPresentation disappearanceTransition];
-[_UIPreviewInteractionViewControllerPresentation privatePresentationBlock];
-[_UIPreviewInteractionViewControllerPresentation privatePresentationCompletionBlock];
-[_UIPreviewInteractionViewControllerPresentation setAppearanceTransition:];
-[_UIPreviewInteractionViewControllerPresentation setCustomContainerView:];
-[_UIPreviewInteractionViewControllerPresentation setCustomViewForTouchContinuation:];
-[_UIPreviewInteractionViewControllerPresentation setDisappearanceTransition:];
-[_UIPreviewInteractionViewControllerPresentation setPrivatePresentationBlock:];
-[_UIPreviewInteractionViewControllerPresentation setPrivatePresentationCompletionBlock:];
-[_UIPreviewInteractionViewControllerPresentation setShouldFlipFromAndToViewsForDisappearanceTransition:];
-[_UIPreviewInteractionViewControllerPresentation setShouldPresentAutomatically:];
-[_UIPreviewInteractionViewControllerPresentation setShouldUpdateFromViewBeforePresentation:];
-[_UIPreviewInteractionViewControllerPresentation setShouldUseCATransitions:];
-[_UIPreviewInteractionViewControllerPresentation shouldFlipFromAndToViewsForDisappearanceTransition];
-[_UIPreviewInteractionViewControllerPresentation shouldPresentAutomatically];
-[_UIPreviewInteractionViewControllerPresentation shouldUpdateFromViewBeforePresentation];
-[_UIPreviewInteractionViewControllerPresentation shouldUseCATransitions];
```
