# `UIViewControllerTransitionCoordinatorContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 14 instance methods, 0 class methods

## Properties

```
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
@property (T@"UIView",R,N) containerView;
@property (T{CGAffineTransform=dddddd},R,N) targetTransform;
```

## Instance methods

```
-[UIViewControllerTransitionCoordinatorContext completionVelocity];
-[UIViewControllerTransitionCoordinatorContext percentComplete];
-[UIViewControllerTransitionCoordinatorContext viewControllerForKey:];
-[UIViewControllerTransitionCoordinatorContext viewForKey:];
-[UIViewControllerTransitionCoordinatorContext isAnimated];
-[UIViewControllerTransitionCoordinatorContext initiallyInteractive];
-[UIViewControllerTransitionCoordinatorContext isInteractive];
-[UIViewControllerTransitionCoordinatorContext presentationStyle];
-[UIViewControllerTransitionCoordinatorContext isCancelled];
-[UIViewControllerTransitionCoordinatorContext transitionDuration];
-[UIViewControllerTransitionCoordinatorContext isInterruptible];
-[UIViewControllerTransitionCoordinatorContext containerView];
-[UIViewControllerTransitionCoordinatorContext targetTransform];
-[UIViewControllerTransitionCoordinatorContext completionCurve];
```
