# `SBLockStateAggregator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLockStateObserving`
- 3 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _lockState;
@"<SBLockStateProviding>" _uiLockStateProvider;
@"SBFAnalyticsClient" _analyticsClient;
```

## Properties

```
@property (T@"SBFAnalyticsClient",W,N,V_analyticsClient) analyticsClient;
@property (T@"<SBLockStateProviding>",&,N,SsetUILockStateProvider:,V_uiLockStateProvider) uiLockStateProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockStateAggregator lockState];
-[SBLockStateAggregator uiLockStateProvider];
-[SBLockStateAggregator init];
-[SBLockStateAggregator dealloc];
-[SBLockStateAggregator invalidate];
-[SBLockStateAggregator lockStateProvider:didUpdateIsUILocked:];
-[SBLockStateAggregator setUILockStateProvider:];
-[SBLockStateAggregator description];
-[SBLockStateAggregator analyticsClient];
-[SBLockStateAggregator _updateLockState];
-[SBLockStateAggregator hasAnyLockState];
-[SBLockStateAggregator _descriptionForLockState:];
-[SBLockStateAggregator _initWithAnalyticsClient:];
-[SBLockStateAggregator setAnalyticsClient:];
```
