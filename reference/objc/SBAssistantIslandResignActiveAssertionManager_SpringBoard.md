# `SBAssistantIslandResignActiveAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _resignActiveAssertion;
@"NSHashTable" _observers;
@"BSContinuousMachTimer" _settleTimer;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,R,N,GisResignedActive) resignedActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAssistantIslandResignActiveAssertionManager removeObserver:];
-[SBAssistantIslandResignActiveAssertionManager dealloc];
-[SBAssistantIslandResignActiveAssertionManager initWithWindowScene:];
-[SBAssistantIslandResignActiveAssertionManager addObserver:];
-[SBAssistantIslandResignActiveAssertionManager invalidate];
-[SBAssistantIslandResignActiveAssertionManager windowScene];
-[SBAssistantIslandResignActiveAssertionManager _stateDidChange];
-[SBAssistantIslandResignActiveAssertionManager _cancelSettleTimer];
-[SBAssistantIslandResignActiveAssertionManager _notifyObserversDidChange];
-[SBAssistantIslandResignActiveAssertionManager _notifyObserversDidSettle];
-[SBAssistantIslandResignActiveAssertionManager _settleTimerDidFire];
-[SBAssistantIslandResignActiveAssertionManager _startSettleTimer];
-[SBAssistantIslandResignActiveAssertionManager acquireResignActiveAssertionWithReason:];
-[SBAssistantIslandResignActiveAssertionManager isResignedActive];
```
