# `_UIPreviewPresentationController2`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPreviewPresentationController`
- 10 instance variables, 11 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _hasPerformedInitialLayout;
B _shouldScaleContentViewToAspectFitPlatter;
B _shouldEnableUserInteractionOnPlatter;
@"<UIViewControllerPreviewing_Internal>" _previewingContext;
@"_UIPreviewPresentationPlatterView" _revealPlatterView;
@"<_UIPreviewInteractionHighlighting>" _currentHighlighter;
@"UIViewPropertyAnimator" _currentTransitionAnimator;
d _interactiveTransitionFraction;
@"_UIPreviewPresentationPlatterView" _contentPlatterView;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _preferredContentPlatterTransform;
```

## Properties

```
@property (T@"_UIPreviewPresentationPlatterView",&,N,V_revealPlatterView) revealPlatterView;
@property (TB,N,V_hasPerformedInitialLayout) hasPerformedInitialLayout;
@property (T{CGAffineTransform=dddddd},N,V_preferredContentPlatterTransform) preferredContentPlatterTransform;
@property (T@"<UIViewControllerPreviewing_Internal>",W,N,V_previewingContext) previewingContext;
@property (T@"<_UIPreviewInteractionHighlighting>",W,N,V_currentHighlighter) currentHighlighter;
@property (T@"UIViewPropertyAnimator",W,N,V_currentTransitionAnimator) currentTransitionAnimator;
@property (Td,N,V_interactiveTransitionFraction) interactiveTransitionFraction;
@property (T@"_UIPreviewPresentationPlatterView",&,N,V_contentPlatterView) contentPlatterView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _computedPlatterFrame;
@property (TB,N,V_shouldScaleContentViewToAspectFitPlatter) shouldScaleContentViewToAspectFitPlatter;
@property (TB,N,V_shouldEnableUserInteractionOnPlatter) shouldEnableUserInteractionOnPlatter;
```

## Instance methods

```
-[_UIPreviewPresentationController2 setCurrentTransitionAnimator:];
-[_UIPreviewPresentationController2 currentTransitionAnimator];
-[_UIPreviewPresentationController2 presentationTransitionDidEnd:];
-[_UIPreviewPresentationController2 preferredContentSizeDidChangeForChildContentContainer:];
-[_UIPreviewPresentationController2 contentPlatterView];
-[_UIPreviewPresentationController2 setPreviewingContext:];
-[_UIPreviewPresentationController2 previewingContext];
-[_UIPreviewPresentationController2 systemLayoutFittingSizeDidChangeForChildContentContainer:];
-[_UIPreviewPresentationController2 _shouldDisableInteractionDuringTransitions];
-[_UIPreviewPresentationController2 dismissalTransitionWillBegin];
-[_UIPreviewPresentationController2 dismissalTransitionDidEnd:];
-[_UIPreviewPresentationController2 presentationTransitionWillBegin];
-[_UIPreviewPresentationController2 _computedPlatterFrame];
-[_UIPreviewPresentationController2 _layoutContentViews];
-[_UIPreviewPresentationController2 _performDismissAnimationsWithTransitionContext:];
-[_UIPreviewPresentationController2 _performPresentationAnimationsWithTransitionContext:];
-[_UIPreviewPresentationController2 _performReducedMotionDismissAnimationsWithTransitionContext:];
-[_UIPreviewPresentationController2 _performReducedMotionPresentationAnimationsWithTransitionContext:];
-[_UIPreviewPresentationController2 _performTransitionAnimations:];
-[_UIPreviewPresentationController2 _preferredContentPlatterRectForContainerRect:];
-[_UIPreviewPresentationController2 _prepareContentPlatterViewForPresentationTransitionIfNeeded:];
-[_UIPreviewPresentationController2 _prepareContentViewsForPresentationAnimationsIfNeeded];
-[_UIPreviewPresentationController2 _preparePresentationAnimationsForTransitionCoordinator:];
-[_UIPreviewPresentationController2 _prepareRevealPlatterViewForPresentationTransitionIfNeeded:];
-[_UIPreviewPresentationController2 _presentationTransitionWillBeginForContainerEffectView:];
-[_UIPreviewPresentationController2 _shouldReduceMotion];
-[_UIPreviewPresentationController2 _updateFromInteractionEffect:];
-[_UIPreviewPresentationController2 containerViewDidLayoutSubviews];
-[_UIPreviewPresentationController2 currentHighlighter];
-[_UIPreviewPresentationController2 hasPerformedInitialLayout];
-[_UIPreviewPresentationController2 initWithPresentedViewController:presentingViewController:previewingContext:];
-[_UIPreviewPresentationController2 interactiveTransitionFraction];
-[_UIPreviewPresentationController2 preferredContentPlatterTransform];
-[_UIPreviewPresentationController2 revealPlatterView];
-[_UIPreviewPresentationController2 setContentPlatterView:];
-[_UIPreviewPresentationController2 setCurrentHighlighter:];
-[_UIPreviewPresentationController2 setHasPerformedInitialLayout:];
-[_UIPreviewPresentationController2 setInteractiveTransitionFraction:];
-[_UIPreviewPresentationController2 setPreferredContentPlatterTransform:];
-[_UIPreviewPresentationController2 setRevealPlatterView:];
-[_UIPreviewPresentationController2 setShouldEnableUserInteractionOnPlatter:];
-[_UIPreviewPresentationController2 setShouldScaleContentViewToAspectFitPlatter:];
-[_UIPreviewPresentationController2 shouldEnableUserInteractionOnPlatter];
-[_UIPreviewPresentationController2 shouldScaleContentViewToAspectFitPlatter];
```
