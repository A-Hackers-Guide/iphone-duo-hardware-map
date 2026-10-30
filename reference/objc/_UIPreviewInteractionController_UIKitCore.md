# `_UIPreviewInteractionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIPreviewInteractionDelegate`, `UIViewControllerTransitioningDelegate`, `_UIPreviewActionsControllerDelegate`
- 26 instance variables, 32 properties, 95 instance methods, 0 class methods

## Instance variables

```
B _performingPreviewTransition;
B _hasTransitionedToPreview;
B _dismissingPreview;
B _commitTransitionScheduled;
B _performingCommitTransition;
@"<_UIPreviewInteractionControllerDelegate>" _delegate;
@"UIView" _sourceView;
@"UIViewController" _presentingViewController;
@"UIPreviewInteraction" _previewInteraction;
@"<_UIPreviewInteractionTouchForceProviding>" _presentedViewTouchForceProvider;
@"<_UIPreviewInteractionTouchForceProviding>" _pausingTouchForceProvider;
@"_UIPreviewInteractionGestureRecognizer" _revealGestureRecognizer;
@"_UIPreviewInteractionGestureRecognizer" _previewGestureRecognizer;
@"_UISteadyTouchForceGestureRecognizer" _steadyTouchForceGestureRecognizer;
@"UIViewController" _currentPreviewViewController;
@"_UIPreviewPresentationController2" _currentPresentationController;
@"<_UIPreviewInteractionHighlighting>" _currentHighlighter;
@"_UIPreviewInteractionPresentationTransition" _currentPresentationTransition;
@"_UIPreviewInteractionDismissTransition" _currentDismissTransition;
@"_UIPreviewInteractionCommitTransition" _currentCommitTransition;
@"_UIInteractionEffect_deprecated" _currentInteractionEffect;
@"_UITouchesObservingGestureRecognizer" _gestureRecognizerForPreviewActions;
@"_UIPreviewActionsController" _previewActionsController;
@"<UIViewControllerPreviewing_Internal>" _currentPreviewingContext;
{CGPoint="x"d"y"d} _location;
{CGPoint="x"d"y"d} _initialLocationForPreviewActionsPanning;
```

## Properties

```
@property (T{CGPoint=dd},N,V_location) location;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (T@"UIViewController",W,N,V_presentingViewController) presentingViewController;
@property (T@"UIPreviewInteraction",&,N,V_previewInteraction) previewInteraction;
@property (T@"<_UIPreviewInteractionTouchForceProviding>",&,N,V_presentedViewTouchForceProvider) presentedViewTouchForceProvider;
@property (T@"<_UIPreviewInteractionTouchForceProviding>",&,N,V_pausingTouchForceProvider) pausingTouchForceProvider;
@property (T@"_UIPreviewInteractionGestureRecognizer",&,N,V_revealGestureRecognizer) revealGestureRecognizer;
@property (T@"_UIPreviewInteractionGestureRecognizer",&,N,V_previewGestureRecognizer) previewGestureRecognizer;
@property (T@"_UISteadyTouchForceGestureRecognizer",&,N,V_steadyTouchForceGestureRecognizer) steadyTouchForceGestureRecognizer;
@property (T@"UIViewController",&,N,V_currentPreviewViewController) currentPreviewViewController;
@property (T@"_UIPreviewPresentationController2",&,N,V_currentPresentationController) currentPresentationController;
@property (T@"<_UIPreviewInteractionHighlighting>",&,N,V_currentHighlighter) currentHighlighter;
@property (T@"_UIPreviewInteractionPresentationTransition",&,N,V_currentPresentationTransition) currentPresentationTransition;
@property (T@"_UIPreviewInteractionDismissTransition",&,N,V_currentDismissTransition) currentDismissTransition;
@property (T@"_UIPreviewInteractionCommitTransition",&,N,V_currentCommitTransition) currentCommitTransition;
@property (TB,N,V_performingPreviewTransition) performingPreviewTransition;
@property (TB,N,V_hasTransitionedToPreview) hasTransitionedToPreview;
@property (TB,N,V_dismissingPreview) dismissingPreview;
@property (TB,N,V_commitTransitionScheduled) commitTransitionScheduled;
@property (TB,N,V_performingCommitTransition) performingCommitTransition;
@property (T@"_UIInteractionEffect_deprecated",&,N,V_currentInteractionEffect) currentInteractionEffect;
@property (T@"_UITouchesObservingGestureRecognizer",&,N,V_gestureRecognizerForPreviewActions) gestureRecognizerForPreviewActions;
@property (T@"_UIPreviewActionsController",&,N,V_previewActionsController) previewActionsController;
@property (T{CGPoint=dd},N,V_initialLocationForPreviewActionsPanning) initialLocationForPreviewActionsPanning;
@property (T@"<UIViewControllerPreviewing_Internal>",W,N,V_currentPreviewingContext) currentPreviewingContext;
@property (T@"UIGestureRecognizer",R,N) presentationGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N) beginPreviewGestureRecognizer;
@property (T@"<_UIPreviewInteractionControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionController _gestureRecognizerFailed:];
-[_UIPreviewInteractionController animationControllerForDismissedController:];
-[_UIPreviewInteractionController animationControllerForPresentedController:presentingController:sourceController:];
-[_UIPreviewInteractionController presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIPreviewInteractionController setPresentingViewController:];
-[_UIPreviewInteractionController location];
-[_UIPreviewInteractionController initWithView:];
-[_UIPreviewInteractionController dealloc];
-[_UIPreviewInteractionController currentPreviewViewController];
-[_UIPreviewInteractionController currentPresentationController];
-[_UIPreviewInteractionController presentingViewController];
-[_UIPreviewInteractionController setDelegate:];
-[_UIPreviewInteractionController setLocation:];
-[_UIPreviewInteractionController setCurrentPreviewViewController:];
-[_UIPreviewInteractionController setSourceView:];
-[_UIPreviewInteractionController gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIPreviewInteractionController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIPreviewInteractionController delegate];
-[_UIPreviewInteractionController interactionControllerForPresentation:];
-[_UIPreviewInteractionController sourceView];
-[_UIPreviewInteractionController _handleSteadyTouchForceGesture:];
-[_UIPreviewInteractionController setPerformingPreviewTransition:];
-[_UIPreviewInteractionController presentedViewTouchForceProvider];
-[_UIPreviewInteractionController _dismissPreviewViewControllerIfNeeded];
-[_UIPreviewInteractionController _dismissPreviewViewControllerIfNeededWithCompletion:];
-[_UIPreviewInteractionController _finalizeAfterPreviewViewControllerPresentation];
-[_UIPreviewInteractionController _finalizeHighlighterAfterPreviewViewControllerPresentation];
-[_UIPreviewInteractionController _handlePreviewActionsGesture:];
-[_UIPreviewInteractionController _handlePreviewGesture:];
-[_UIPreviewInteractionController _handleRevealGesture:];
-[_UIPreviewInteractionController _isLongPressGestureRecognizerUsedForDelayingActions:];
-[_UIPreviewInteractionController _newHighlighterForPreviewingContext:];
-[_UIPreviewInteractionController _overrideSourceViewForBinaryCompatibilityIfNeeded:sourceRect:];
-[_UIPreviewInteractionController _preferredNavigationControllerForCommitTransition];
-[_UIPreviewInteractionController _preparePreviewPresentationControllerIfNeeded:];
-[_UIPreviewInteractionController _preparePreviewViewControllerPresentationFromPreviewInteraction:];
-[_UIPreviewInteractionController _preparedInteractionEffect];
-[_UIPreviewInteractionController _previewInteractionShouldEndOnGestureCompletion:];
-[_UIPreviewInteractionController _previewPresentationControllerForViewController:];
-[_UIPreviewInteractionController _previewingIsPossibleForView:];
-[_UIPreviewInteractionController _resetCustomPresentationHooks];
-[_UIPreviewInteractionController _revertInteractionEffectToStartState];
-[_UIPreviewInteractionController _stopCurrentInteractionEffect];
-[_UIPreviewInteractionController _viewControllerIsChildOfTwoColumnSplitViewController:];
-[_UIPreviewInteractionController beginPreviewGestureRecognizer];
-[_UIPreviewInteractionController commitInteractivePreview];
-[_UIPreviewInteractionController commitTransitionScheduled];
-[_UIPreviewInteractionController currentCommitTransition];
-[_UIPreviewInteractionController currentDismissTransition];
-[_UIPreviewInteractionController currentHighlighter];
-[_UIPreviewInteractionController currentInteractionEffect];
-[_UIPreviewInteractionController currentPresentationTransition];
-[_UIPreviewInteractionController currentPreviewingContext];
-[_UIPreviewInteractionController didDismissPreviewActionsController:];
-[_UIPreviewInteractionController dismissingPreview];
-[_UIPreviewInteractionController gestureRecognizerForPreviewActions];
-[_UIPreviewInteractionController hasTransitionedToPreview];
-[_UIPreviewInteractionController initialLocationForPreviewActionsPanning];
-[_UIPreviewInteractionController initialPlatterPositionForPreviewActionsController:];
-[_UIPreviewInteractionController maximumPreviewActionsViewSizeForPreviewActionsController:];
-[_UIPreviewInteractionController pausingTouchForceProvider];
-[_UIPreviewInteractionController performingCommitTransition];
-[_UIPreviewInteractionController performingPreviewTransition];
-[_UIPreviewInteractionController presentationGestureRecognizer];
-[_UIPreviewInteractionController previewActionsController];
-[_UIPreviewInteractionController previewActionsController:didCompleteWithSelectedAction:];
-[_UIPreviewInteractionController previewActionsController:didUpdatePlatterTranslation:withVelocity:];
-[_UIPreviewInteractionController previewGestureRecognizer];
-[_UIPreviewInteractionController previewInteraction];
-[_UIPreviewInteractionController previewInteraction:didUpdateCommitTransition:ended:];
-[_UIPreviewInteractionController previewInteraction:didUpdatePreviewTransition:ended:];
-[_UIPreviewInteractionController previewInteractionDidCancel:];
-[_UIPreviewInteractionController previewInteractionShouldBegin:];
-[_UIPreviewInteractionController revealGestureRecognizer];
-[_UIPreviewInteractionController setCommitTransitionScheduled:];
-[_UIPreviewInteractionController setCurrentCommitTransition:];
-[_UIPreviewInteractionController setCurrentDismissTransition:];
-[_UIPreviewInteractionController setCurrentHighlighter:];
-[_UIPreviewInteractionController setCurrentInteractionEffect:];
-[_UIPreviewInteractionController setCurrentPresentationController:];
-[_UIPreviewInteractionController setCurrentPresentationTransition:];
-[_UIPreviewInteractionController setCurrentPreviewingContext:];
-[_UIPreviewInteractionController setDismissingPreview:];
-[_UIPreviewInteractionController setGestureRecognizerForPreviewActions:];
-[_UIPreviewInteractionController setHasTransitionedToPreview:];
-[_UIPreviewInteractionController setInitialLocationForPreviewActionsPanning:];
-[_UIPreviewInteractionController setPausingTouchForceProvider:];
-[_UIPreviewInteractionController setPerformingCommitTransition:];
-[_UIPreviewInteractionController setPresentedViewTouchForceProvider:];
-[_UIPreviewInteractionController setPreviewActionsController:];
-[_UIPreviewInteractionController setPreviewGestureRecognizer:];
-[_UIPreviewInteractionController setPreviewInteraction:];
-[_UIPreviewInteractionController setRevealGestureRecognizer:];
-[_UIPreviewInteractionController setSteadyTouchForceGestureRecognizer:];
-[_UIPreviewInteractionController steadyTouchForceGestureRecognizer];
```
