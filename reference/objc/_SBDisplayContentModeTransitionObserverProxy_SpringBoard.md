# `_SBDisplayContentModeTransitionObserverProxy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`
- 5 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _windowScenesOfInterest;
Q _hash;
@"NSString" _observerClassName;
B _wantsAllTransitions;
@"<SBDisplayContentModeTransitionObserver>" _observer;
```

## Properties

```
@property (T@"<SBDisplayContentModeTransitionObserver>",W,N,V_observer) observer;
@property (TB,N,V_wantsAllTransitions) wantsAllTransitions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBDisplayContentModeTransitionObserverProxy observer];
-[_SBDisplayContentModeTransitionObserverProxy displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[_SBDisplayContentModeTransitionObserverProxy displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[_SBDisplayContentModeTransitionObserverProxy initWithObserver:];
-[_SBDisplayContentModeTransitionObserverProxy setObserver:];
-[_SBDisplayContentModeTransitionObserverProxy addWindowSceneOfInterest:];
-[_SBDisplayContentModeTransitionObserverProxy removeWindowSceneOfInterest:];
-[_SBDisplayContentModeTransitionObserverProxy setWantsAllTransitions:];
-[_SBDisplayContentModeTransitionObserverProxy wantsAllTransitions];
-[_SBDisplayContentModeTransitionObserverProxy windowScenesOfInterest];
```
