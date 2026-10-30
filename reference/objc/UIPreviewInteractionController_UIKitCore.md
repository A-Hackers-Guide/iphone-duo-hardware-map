# `UIPreviewInteractionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteractionProgressObserver`, `_UIForcePresentationControllerDelegate`, `UIPreviewInteractionDelegate`
- 23 instance variables, 28 properties, 85 instance methods, 0 class methods

## Instance variables

```
B _isCommitting;
B _generatorTurnedOn;
B _statusBarWasHidden;
B _didSendDelegateWillDismissViewController;
@"<UIPreviewInteractionControllerDelegate>" _delegate;
@"UIView" _sourceView;
@"UIViewController" _presentingViewController;
@"UIPreviewInteraction" _previewInteraction;
@"UIInteractionProgress" _interactionProgressForCommit;
@"_UIRevealGestureRecognizer" _revealGestureRecognizer;
@"_UIPreviewGestureRecognizer" _previewGestureRecognizer;
@"UIPanGestureRecognizer" _modalPanGestureRecognizer;
@"_UITouchesObservingGestureRecognizer" _touchObservingGestureRecognizer;
@"_UIDeepPressAnalyzer" _deepPressAnalyzer;
@"UIViewController" _currentPreviewViewController;
@"UIPresentationController<UIForcePresentationController>" _currentPresentationController;
@"<UIForceTransitioningDelegate>" _currentTransitionDelegate;
@"UIWindow" _windowForPreviewPresentation;
@ _currentCommitTransition;
@"<UIViewControllerPreviewing_Internal>" _previewingContext;
@"_UIStatesFeedbackGenerator" _feedbackGenerator;
@"UIInteractionProgress" _interactionProgressForPresentation;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (T{CGPoint=dd},N,V_location) location;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (T@"UIViewController",W,N,V_presentingViewController) presentingViewController;
@property (T@"UIPreviewInteraction",&,N,V_previewInteraction) previewInteraction;
@property (T@"UIInteractionProgress",&,N,V_interactionProgressForCommit) interactionProgressForCommit;
@property (T@"_UIRevealGestureRecognizer",&,N,V_revealGestureRecognizer) revealGestureRecognizer;
@property (T@"_UIPreviewGestureRecognizer",&,N,V_previewGestureRecognizer) previewGestureRecognizer;
@property (T@"UIPanGestureRecognizer",&,N,V_modalPanGestureRecognizer) modalPanGestureRecognizer;
@property (T@"_UITouchesObservingGestureRecognizer",&,N,V_touchObservingGestureRecognizer) touchObservingGestureRecognizer;
@property (T@"_UIDeepPressAnalyzer",&,N,V_deepPressAnalyzer) deepPressAnalyzer;
@property (T@"UIViewController",&,N,V_currentPreviewViewController) currentPreviewViewController;
@property (T@"UIPresentationController<UIForcePresentationController>",&,N,V_currentPresentationController) currentPresentationController;
@property (T@"<UIForceTransitioningDelegate>",&,N,V_currentTransitionDelegate) currentTransitionDelegate;
@property (T@"UIWindow",&,N,V_windowForPreviewPresentation) windowForPreviewPresentation;
@property (TB,N,V_statusBarWasHidden) statusBarWasHidden;
@property (T@,&,N,V_currentCommitTransition) currentCommitTransition;
@property (TB,N,V_didSendDelegateWillDismissViewController) didSendDelegateWillDismissViewController;
@property (T@"<UIViewControllerPreviewing_Internal>",W,N,V_previewingContext) previewingContext;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (T@"UIInteractionProgress",&,N,V_interactionProgressForPresentation) interactionProgressForPresentation;
@property (T@"UIGestureRecognizer",R,N) presentationGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N) beginPreviewGestureRecognizer;
@property (T@"<UIPreviewInteractionControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,D,N) gestureRecognizers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPreviewInteractionController interactionProgressDidUpdate:];
-[UIPreviewInteractionController interactionProgress:didEnd:];
-[UIPreviewInteractionController _gestureRecognizerFailed:];
-[UIPreviewInteractionController setFeedbackGenerator:];
-[UIPreviewInteractionController feedbackGenerator];
-[UIPreviewInteractionController gestureRecognizers];
-[UIPreviewInteractionController interactionProgressForPresentation];
-[UIPreviewInteractionController setInteractionProgressForPresentation:];
-[UIPreviewInteractionController init];
-[UIPreviewInteractionController setPresentingViewController:];
-[UIPreviewInteractionController location];
-[UIPreviewInteractionController initWithView:];
-[UIPreviewInteractionController dealloc];
-[UIPreviewInteractionController currentPreviewViewController];
-[UIPreviewInteractionController currentPresentationController];
-[UIPreviewInteractionController presentingViewController];
-[UIPreviewInteractionController setPreviewingContext:];
-[UIPreviewInteractionController setDelegate:];
-[UIPreviewInteractionController setLocation:];
-[UIPreviewInteractionController previewingContext];
-[UIPreviewInteractionController setCurrentPreviewViewController:];
-[UIPreviewInteractionController setSourceView:];
-[UIPreviewInteractionController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIPreviewInteractionController delegate];
-[UIPreviewInteractionController _setStatusBarHidden:];
-[UIPreviewInteractionController sourceView];
-[UIPreviewInteractionController touchObservingGestureRecognizer];
-[UIPreviewInteractionController _activateFeedback];
-[UIPreviewInteractionController _activateFeedbackIfNeeded];
-[UIPreviewInteractionController _configureCommitInteractionProgressForView:];
-[UIPreviewInteractionController _deactivateFeedbackIfNeeded];
-[UIPreviewInteractionController _finalizeInteractivePreview];
-[UIPreviewInteractionController _handleRevealGesture:];
-[UIPreviewInteractionController _handleTouchObservingGesture:];
-[UIPreviewInteractionController _previewPresentationControllerDidScheduleDismiss];
-[UIPreviewInteractionController _previewingIsPossibleForView:];
-[UIPreviewInteractionController _resetCustomPresentationHooks];
-[UIPreviewInteractionController _transitionDelegateForPreviewViewController:atPosition:inView:];
-[UIPreviewInteractionController _turnOffFeedbackGenerator];
-[UIPreviewInteractionController _turnOnFeedbackGenerator];
-[UIPreviewInteractionController _usesPreviewInteraction];
-[UIPreviewInteractionController _usesPreviewPresentationController];
-[UIPreviewInteractionController _viewControllerIsChildOfExpandedSplitViewController:];
-[UIPreviewInteractionController beginPreviewGestureRecognizer];
-[UIPreviewInteractionController cancelInteractivePreview];
-[UIPreviewInteractionController commitInteractivePreview];
-[UIPreviewInteractionController configureRevealTransformSourceViewSnapshotSuppressionFromLocation:inView:];
-[UIPreviewInteractionController configureRevealTransformWithInteractionProgress:forLocation:inView:containerView:];
-[UIPreviewInteractionController currentCommitTransition];
-[UIPreviewInteractionController currentTransitionDelegate];
-[UIPreviewInteractionController deepPressAnalyzer];
-[UIPreviewInteractionController didSendDelegateWillDismissViewController];
-[UIPreviewInteractionController forcePresentationController:didSelectMenuItem:];
-[UIPreviewInteractionController forcePresentationControllerDidDismiss:];
-[UIPreviewInteractionController forcePresentationControllerWantsToCommit:];
-[UIPreviewInteractionController forcePresentationControllerWillDismiss:];
-[UIPreviewInteractionController forcePresentationTransitionWillBegin:];
-[UIPreviewInteractionController initGestureRecognizers];
-[UIPreviewInteractionController interactionProgressForCommit];
-[UIPreviewInteractionController modalPanGestureRecognizer];
-[UIPreviewInteractionController presentationGestureRecognizer];
-[UIPreviewInteractionController previewGestureRecognizer];
-[UIPreviewInteractionController previewInteraction];
-[UIPreviewInteractionController previewInteraction:didUpdateCommitTransition:ended:];
-[UIPreviewInteractionController previewInteraction:didUpdatePreviewTransition:ended:];
-[UIPreviewInteractionController previewInteractionDidCancel:];
-[UIPreviewInteractionController previewInteractionShouldBegin:];
-[UIPreviewInteractionController revealGestureRecognizer];
-[UIPreviewInteractionController setCurrentCommitTransition:];
-[UIPreviewInteractionController setCurrentPresentationController:];
-[UIPreviewInteractionController setCurrentTransitionDelegate:];
-[UIPreviewInteractionController setDeepPressAnalyzer:];
-[UIPreviewInteractionController setDidSendDelegateWillDismissViewController:];
-[UIPreviewInteractionController setInteractionProgressForCommit:];
-[UIPreviewInteractionController setModalPanGestureRecognizer:];
-[UIPreviewInteractionController setPreviewGestureRecognizer:];
-[UIPreviewInteractionController setPreviewInteraction:];
-[UIPreviewInteractionController setRevealGestureRecognizer:];
-[UIPreviewInteractionController setStatusBarWasHidden:];
-[UIPreviewInteractionController setTouchObservingGestureRecognizer:];
-[UIPreviewInteractionController setWindowForPreviewPresentation:];
-[UIPreviewInteractionController startInteractivePreviewAtLocation:inView:];
-[UIPreviewInteractionController startInteractivePreviewWithGestureRecognizer:];
-[UIPreviewInteractionController statusBarWasHidden];
-[UIPreviewInteractionController windowForPreviewPresentation];
```
