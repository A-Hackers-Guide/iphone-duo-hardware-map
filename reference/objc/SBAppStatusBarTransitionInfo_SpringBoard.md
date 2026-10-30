# `SBAppStatusBarTransitionInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIStatusBarStyleRequest" _startStyleRequest;
q _startOrientation;
@"UIStatusBarStyleRequest" _endStyleRequest;
q _endOrientation;
i _transition;
B _zoomOther;
```

## Properties

```
@property (T@"UIStatusBarStyleRequest",C,N,V_startStyleRequest) startStyleRequest;
@property (Tq,N,V_startOrientation) startOrientation;
@property (T@"UIStatusBarStyleRequest",C,N,V_endStyleRequest) endStyleRequest;
@property (Tq,N,V_endOrientation) endOrientation;
@property (Ti,N,V_transition) transition;
@property (TB,N,V_zoomOther) zoomOther;
```

## Instance methods

```
-[SBAppStatusBarTransitionInfo transition];
-[SBAppStatusBarTransitionInfo description];
-[SBAppStatusBarTransitionInfo setTransition:];
-[SBAppStatusBarTransitionInfo endStyleRequest];
-[SBAppStatusBarTransitionInfo endOrientation];
-[SBAppStatusBarTransitionInfo setEndOrientation:];
-[SBAppStatusBarTransitionInfo setEndStyleRequest:];
-[SBAppStatusBarTransitionInfo setStartOrientation:];
-[SBAppStatusBarTransitionInfo setStartStyleRequest:];
-[SBAppStatusBarTransitionInfo setZoomOther:];
-[SBAppStatusBarTransitionInfo startOrientation];
-[SBAppStatusBarTransitionInfo startStyleRequest];
-[SBAppStatusBarTransitionInfo zoomOther];
```
