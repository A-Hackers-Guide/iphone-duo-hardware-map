# `_UIPreviewInteractionPresentationTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`, `UIViewControllerInteractiveTransitioning`
- 6 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerContextTransitioning>" _transitionContext;
@"UIViewPropertyAnimator" _presentationAnimator;
d _interactiveTransitionFraction;
B _shouldPerformAsDismissTransition;
B _didScheduleFinishTransition;
B _didScheduleCancelTransition;
```

## Properties

```
@property (Td,R,D,N) interactiveTransitionFraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,?,R,N) completionSpeed;
@property (Tq,?,R,N) completionCurve;
@property (TB,?,R,N) wantsInteractiveStart;
```

## Instance methods

```
-[_UIPreviewInteractionPresentationTransition updateInteractiveTransition:];
-[_UIPreviewInteractionPresentationTransition animateTransition:];
-[_UIPreviewInteractionPresentationTransition transitionDuration:];
-[_UIPreviewInteractionPresentationTransition init];
-[_UIPreviewInteractionPresentationTransition startInteractiveTransition:];
-[_UIPreviewInteractionPresentationTransition interruptibleAnimatorForTransition:];
-[_UIPreviewInteractionPresentationTransition animationEnded:];
-[_UIPreviewInteractionPresentationTransition finishTransition];
-[_UIPreviewInteractionPresentationTransition wantsInteractiveStart];
-[_UIPreviewInteractionPresentationTransition cancelTransition];
-[_UIPreviewInteractionPresentationTransition _applyPushDecayEffectTransformToView:];
-[_UIPreviewInteractionPresentationTransition _newPushDecayAnimator];
-[_UIPreviewInteractionPresentationTransition _newReducedMotionTimingCurveProviderForPreviewTransition];
-[_UIPreviewInteractionPresentationTransition _newTimingCurveProviderForPreviewTransition];
-[_UIPreviewInteractionPresentationTransition _performCancelTransition];
-[_UIPreviewInteractionPresentationTransition _performFinishTransition];
-[_UIPreviewInteractionPresentationTransition _preparedPresentationAnimator];
-[_UIPreviewInteractionPresentationTransition _previewPresentationControllerForTransitionContext:];
-[_UIPreviewInteractionPresentationTransition _previewPresentationControllerForViewController:];
-[_UIPreviewInteractionPresentationTransition _shouldReduceMotion];
-[_UIPreviewInteractionPresentationTransition interactiveTransitionFraction];
```
