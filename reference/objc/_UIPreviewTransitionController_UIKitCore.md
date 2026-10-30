# `_UIPreviewTransitionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPercentDrivenInteractiveTransition`
- Protocols: `UIInteractionProgressObserver`, `UIViewControllerAnimatedTransitioning`, `UIForceInteractionController`
- 6 instance variables, 13 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"UIInteractionProgress" _interactionProgress;
Q _targetPresentationPhase;
@"NSDictionary" _viewsParticipatingInCommitTransition;
@"_UIStatesFeedbackGenerator" _feedbackGenerator;
@"NSMutableDictionary" _animationsByPresentationPhase;
@"<UIViewControllerContextTransitioning>" _transitionContext;
```

## Properties

```
@property (T@"UIInteractionProgress",&,N,V_interactionProgress) interactionProgress;
@property (TQ,N,V_targetPresentationPhase) targetPresentationPhase;
@property (T@"NSMutableDictionary",&,N,V_animationsByPresentationPhase) animationsByPresentationPhase;
@property (T@"<UIViewControllerContextTransitioning>",W,N,V_transitionContext) transitionContext;
@property (T@"NSDictionary",&,N,V_viewsParticipatingInCommitTransition) viewsParticipatingInCommitTransition;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,?,R,N) completionSpeed;
@property (Tq,?,R,N) completionCurve;
@property (TB,?,R,N) wantsInteractiveStart;
```

## Class methods

```
+[_UIPreviewTransitionController performCommitTransitionWithDelegate:forViewController:previewViewController:previewInteractionController:completion:];
```

## Instance methods

```
-[_UIPreviewTransitionController interactionProgressDidUpdate:];
-[_UIPreviewTransitionController interactionProgress:didEnd:];
-[_UIPreviewTransitionController updateInteractiveTransition:];
-[_UIPreviewTransitionController setFeedbackGenerator:];
-[_UIPreviewTransitionController feedbackGenerator];
-[_UIPreviewTransitionController animateTransition:];
-[_UIPreviewTransitionController transitionDuration:];
-[_UIPreviewTransitionController transitionContext];
-[_UIPreviewTransitionController init];
-[_UIPreviewTransitionController startInteractiveTransition:];
-[_UIPreviewTransitionController setTransitionContext:];
-[_UIPreviewTransitionController cancelInteractiveTransition];
-[_UIPreviewTransitionController animationEnded:];
-[_UIPreviewTransitionController finishInteractiveTransition];
-[_UIPreviewTransitionController interactionProgress];
-[_UIPreviewTransitionController setInteractionProgress:];
-[_UIPreviewTransitionController _animateCommitTransition:];
-[_UIPreviewTransitionController _animateDismissTransition:];
-[_UIPreviewTransitionController _animatePreviewTransition:];
-[_UIPreviewTransitionController _animateRevealTransition:];
-[_UIPreviewTransitionController _completeAnimationWithPresentationPhase:finished:];
-[_UIPreviewTransitionController _layoutForPresentationPhase:];
-[_UIPreviewTransitionController animationsByPresentationPhase];
-[_UIPreviewTransitionController initWithInteractionProgress:targetPresentationPhase:];
-[_UIPreviewTransitionController setAnimations:completion:forPresentationPhase:];
-[_UIPreviewTransitionController setAnimationsByPresentationPhase:];
-[_UIPreviewTransitionController setTargetPresentationPhase:];
-[_UIPreviewTransitionController setViewsParticipatingInCommitTransition:];
-[_UIPreviewTransitionController targetPresentationPhase];
-[_UIPreviewTransitionController viewsParticipatingInCommitTransition];
```
