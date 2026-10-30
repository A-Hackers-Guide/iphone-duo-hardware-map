# `_UIViewControllerImmediateAnimationTransitionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitionCoordinator`
- 1 instance variables, 16 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIView" _containerView;
```

## Properties

```
@property (T@"UIView",&,N,V_containerView) containerView;
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
-[_UIViewControllerImmediateAnimationTransitionCoordinator setContainerView:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator completionVelocity];
-[_UIViewControllerImmediateAnimationTransitionCoordinator percentComplete];
-[_UIViewControllerImmediateAnimationTransitionCoordinator animateAlongsideTransitionInView:animation:completion:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator viewControllerForKey:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator animateAlongsideTransition:completion:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator viewForKey:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator isAnimated];
-[_UIViewControllerImmediateAnimationTransitionCoordinator notifyWhenInteractionEndsUsingBlock:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator initiallyInteractive];
-[_UIViewControllerImmediateAnimationTransitionCoordinator notifyWhenInteractionChangesUsingBlock:];
-[_UIViewControllerImmediateAnimationTransitionCoordinator isInteractive];
-[_UIViewControllerImmediateAnimationTransitionCoordinator presentationStyle];
-[_UIViewControllerImmediateAnimationTransitionCoordinator isCancelled];
-[_UIViewControllerImmediateAnimationTransitionCoordinator transitionDuration];
-[_UIViewControllerImmediateAnimationTransitionCoordinator isInterruptible];
-[_UIViewControllerImmediateAnimationTransitionCoordinator containerView];
-[_UIViewControllerImmediateAnimationTransitionCoordinator targetTransform];
-[_UIViewControllerImmediateAnimationTransitionCoordinator completionCurve];
-[_UIViewControllerImmediateAnimationTransitionCoordinator initWithContainerView:];
```
