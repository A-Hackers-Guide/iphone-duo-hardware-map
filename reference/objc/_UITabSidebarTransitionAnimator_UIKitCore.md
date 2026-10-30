# `_UITabSidebarTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitionCoordinator`
- 5 instance variables, 16 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _animationBlocks;
@"NSMutableArray" _completionBlocks;
B _completed;
d _transitionDuration;
@"UIView" _containerView;
```

## Properties

```
@property (T@"UIView",R,W,N,V_containerView) containerView;
@property (TB,R,N,GisAnimated) animated;
@property (Tq,R,N) presentationStyle;
@property (TB,R,N) initiallyInteractive;
@property (TB,R,N) isInterruptible;
@property (TB,R,N,GisInteractive) interactive;
@property (TB,R,N,GisCancelled) cancelled;
@property (Td,R,N,V_transitionDuration) transitionDuration;
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
-[_UITabSidebarTransitionAnimator completionVelocity];
-[_UITabSidebarTransitionAnimator percentComplete];
-[_UITabSidebarTransitionAnimator animateAlongsideTransitionInView:animation:completion:];
-[_UITabSidebarTransitionAnimator viewControllerForKey:];
-[_UITabSidebarTransitionAnimator animateAlongsideTransition:completion:];
-[_UITabSidebarTransitionAnimator viewForKey:];
-[_UITabSidebarTransitionAnimator isAnimated];
-[_UITabSidebarTransitionAnimator notifyWhenInteractionEndsUsingBlock:];
-[_UITabSidebarTransitionAnimator initiallyInteractive];
-[_UITabSidebarTransitionAnimator notifyWhenInteractionChangesUsingBlock:];
-[_UITabSidebarTransitionAnimator isInteractive];
-[_UITabSidebarTransitionAnimator presentationStyle];
-[_UITabSidebarTransitionAnimator isCancelled];
-[_UITabSidebarTransitionAnimator transitionDuration];
-[_UITabSidebarTransitionAnimator isInterruptible];
-[_UITabSidebarTransitionAnimator containerView];
-[_UITabSidebarTransitionAnimator targetTransform];
-[_UITabSidebarTransitionAnimator completionCurve];
-[_UITabSidebarTransitionAnimator initWithContainerView:duration:];
-[_UITabSidebarTransitionAnimator runAnimations];
-[_UITabSidebarTransitionAnimator runCompletions];
```
