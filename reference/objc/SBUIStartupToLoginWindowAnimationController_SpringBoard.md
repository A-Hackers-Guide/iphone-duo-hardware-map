# `SBUIStartupToLoginWindowAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIMainScreenAnimationController`
- Protocols: `SBLoginAppContainerViewControllerObserver`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBWindow" _transitionWindow;
@"NSArray" _persistentSnapshotOverlays;
@"BSTransaction" _waitForLoginAppToFinishLaunchingTransaction;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUIStartupToLoginWindowAnimationController animationSettings];
-[SBUIStartupToLoginWindowAnimationController initWithTransitionContextProvider:];
-[SBUIStartupToLoginWindowAnimationController _cleanupAnimation];
-[SBUIStartupToLoginWindowAnimationController _setHidden:];
-[SBUIStartupToLoginWindowAnimationController _startAnimation];
-[SBUIStartupToLoginWindowAnimationController _getTransitionWindow];
-[SBUIStartupToLoginWindowAnimationController _shouldDismissBanner];
-[SBUIStartupToLoginWindowAnimationController initWithTransitionContextProvider:overlays:];
-[SBUIStartupToLoginWindowAnimationController loginAppDidFinishLaunching:];
```
