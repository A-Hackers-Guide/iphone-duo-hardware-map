# `_UIViewControllerNullAnimationTransitionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitionCoordinator`
- 4 instance variables, 16 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _transitionIsInFlight;
@"NSMutableArray" _alongsideAnimations;
@"NSMutableArray" _alongsideCompletions;
@"UIView" _containerView;
```

## Properties

```
@property (T@"UIView",N,V_containerView) containerView;
@property (TB,R,N,GisAnimated) animated;
@property (Tq,R,N) presentationStyle;
@property (TB,R,N) initiallyInteractive;
@property (TB,R,N) isInterruptible;
@property (TB,R,N,GisInteractive) interactive;
@property (TB,R,N,GisCancelled) cancelled;
@property (Td,R,N) transitionDuration;
@property (Td,R,N) percentComplete;
@property (Td,R,N) completionVelocity;
@property (Tq,R,N) completionCurve;
@property (T{CGAffineTransform=dddddd},R,N) targetTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIViewControllerNullAnimationTransitionCoordinator _runAlongsideAnimations];
-[_UIViewControllerNullAnimationTransitionCoordinator _runAlongsideCompletions];
-[_UIViewControllerNullAnimationTransitionCoordinator setContainerView:];
-[_UIViewControllerNullAnimationTransitionCoordinator completionVelocity];
-[_UIViewControllerNullAnimationTransitionCoordinator percentComplete];
-[_UIViewControllerNullAnimationTransitionCoordinator animateAlongsideTransitionInView:animation:completion:];
-[_UIViewControllerNullAnimationTransitionCoordinator viewControllerForKey:];
-[_UIViewControllerNullAnimationTransitionCoordinator animateAlongsideTransition:completion:];
-[_UIViewControllerNullAnimationTransitionCoordinator viewForKey:];
-[_UIViewControllerNullAnimationTransitionCoordinator isAnimated];
-[_UIViewControllerNullAnimationTransitionCoordinator notifyWhenInteractionEndsUsingBlock:];
-[_UIViewControllerNullAnimationTransitionCoordinator initiallyInteractive];
-[_UIViewControllerNullAnimationTransitionCoordinator notifyWhenInteractionChangesUsingBlock:];
-[_UIViewControllerNullAnimationTransitionCoordinator isInteractive];
-[_UIViewControllerNullAnimationTransitionCoordinator presentationStyle];
-[_UIViewControllerNullAnimationTransitionCoordinator isCancelled];
-[_UIViewControllerNullAnimationTransitionCoordinator _applyBlocks:releaseBlocks:];
-[_UIViewControllerNullAnimationTransitionCoordinator transitionDuration];
-[_UIViewControllerNullAnimationTransitionCoordinator _runAlongsideCompletionsAndClearAlongsideAnimations];
-[_UIViewControllerNullAnimationTransitionCoordinator isInterruptible];
-[_UIViewControllerNullAnimationTransitionCoordinator containerView];
-[_UIViewControllerNullAnimationTransitionCoordinator targetTransform];
-[_UIViewControllerNullAnimationTransitionCoordinator completionCurve];
-[_UIViewControllerNullAnimationTransitionCoordinator _alongsideCompletions:];
-[_UIViewControllerNullAnimationTransitionCoordinator _animateAlongsideTransitionInView:systemAnimation:systemCompletion:animation:completion:];
-[_UIViewControllerNullAnimationTransitionCoordinator _mainContext];
-[_UIViewControllerNullAnimationTransitionCoordinator isRotating];
-[_UIViewControllerNullAnimationTransitionCoordinator _runAlongsideCompletionsAfterCommit];
-[_UIViewControllerNullAnimationTransitionCoordinator _alongsideAnimations:];
```
