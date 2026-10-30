# `FBWatchdogTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _watchdogBehavior;
@"<FBProcessWatchdogProviding>" _watchdogProvider;
B _runIndependently;
```

## Properties

```
@property (TB,N,V_runIndependently) runIndependently;
@property (Tq,N,V_watchdogBehavior) watchdogBehavior;
@property (T@"<FBProcessWatchdogProviding>",&,N,V_watchdogProvider) watchdogProvider;
```

## Instance methods

```
-[FBWatchdogTransitionContext mutableCopyWithZone:];
-[FBWatchdogTransitionContext setWatchdogProvider:];
-[FBWatchdogTransitionContext watchdogProvider];
-[FBWatchdogTransitionContext copyWithZone:];
-[FBWatchdogTransitionContext runIndependently];
-[FBWatchdogTransitionContext setRunIndependently:];
-[FBWatchdogTransitionContext setWatchdogBehavior:];
-[FBWatchdogTransitionContext watchdogBehavior];
```
