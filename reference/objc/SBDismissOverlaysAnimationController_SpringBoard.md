# `SBDismissOverlaysAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIAnimationController`
- 2 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
Q _dismissOptions;
@"SBWorkspaceTransitionRequest" _transitionRequest;
```

## Properties

```
@property (TQ,R,N,V_dismissOptions) dismissOptions;
```

## Class methods

```
+[SBDismissOverlaysAnimationController _overlaysToDismissForOptions:windowScene:];
+[SBDismissOverlaysAnimationController willDismissOverlaysForDismissOptions:windowScene:];
```

## Instance methods

```
-[SBDismissOverlaysAnimationController animationSettings];
-[SBDismissOverlaysAnimationController _canBeInterrupted];
-[SBDismissOverlaysAnimationController initWithTransitionContextProvider:];
-[SBDismissOverlaysAnimationController _startAnimation];
-[SBDismissOverlaysAnimationController initWithTransitionContextProvider:options:];
-[SBDismissOverlaysAnimationController dismissOptions];
```
