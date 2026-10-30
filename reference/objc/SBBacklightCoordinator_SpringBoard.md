# `SBBacklightCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`
- 9 instance variables, 15 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _backlightControllers;
q _aggregateBacklightState;
q _pendingAggregateBacklightState;
@"<SBSleepWakePolicyProviding>" _sleepWakePolicy;
q _lastBacklightChangeSource;
@"NSMapTable" _pendingBacklightStates;
@"NSHashTable" _observers;
@"FBSystemService" _systemService;
d _idleSleepPreventionInterval;
```

## Properties

```
@property (Tq,N,S_setAggregateBacklightState:,V_aggregateBacklightState) aggregateBacklightState;
@property (Tq,N,S_setPendingAggregateBacklightState:,V_pendingAggregateBacklightState) pendingAggregateBacklightState;
@property (T@"NSMapTable",&,N,V_pendingBacklightStates) pendingBacklightStates;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"FBSystemService",W,N,V_systemService) systemService;
@property (Td,N,V_idleSleepPreventionInterval) idleSleepPreventionInterval;
@property (T@"<SBSleepWakePolicyProviding>",&,N,V_sleepWakePolicy) sleepWakePolicy;
@property (TB,R,N,GisAnyBacklightOn) anyBacklightOn;
@property (Tq,R,N) aggregateBacklightStateExcludingPrewarms;
@property (Tq,R,N) pendingAggregateBacklightStateExcludingPrewarms;
@property (Tq,R,N,V_lastBacklightChangeSource) lastBacklightChangeSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBacklightCoordinator backlightController:didTransitionToBacklightState:source:];
-[SBBacklightCoordinator setSystemService:];
-[SBBacklightCoordinator sleepWakePolicy];
-[SBBacklightCoordinator backlightController:willTransitionToBacklightState:source:];
-[SBBacklightCoordinator actionForBacklightChangeSource:];
-[SBBacklightCoordinator aggregateBacklightStateExcludingPrewarms];
-[SBBacklightCoordinator aggregateBacklightState];
-[SBBacklightCoordinator pendingAggregateBacklightStateExcludingPrewarms];
-[SBBacklightCoordinator removeObserver:];
-[SBBacklightCoordinator addBacklightController:];
-[SBBacklightCoordinator init];
-[SBBacklightCoordinator _preventIdleSleep];
-[SBBacklightCoordinator lastBacklightChangeSource];
-[SBBacklightCoordinator setPendingBacklightStates:];
-[SBBacklightCoordinator _mostActivePendingBacklightState];
-[SBBacklightCoordinator targetBacklightControllersForAction:];
-[SBBacklightCoordinator idleSleepPreventionInterval];
-[SBBacklightCoordinator systemService];
-[SBBacklightCoordinator _mostActiveBacklightState];
-[SBBacklightCoordinator addObserver:];
-[SBBacklightCoordinator _setPendingAggregateBacklightState:];
-[SBBacklightCoordinator _updateAggregateBacklightStates];
-[SBBacklightCoordinator targetBacklightControllersForActiveDim];
-[SBBacklightCoordinator _controllersExcludingPrewarms];
-[SBBacklightCoordinator _allowIdleSleep];
-[SBBacklightCoordinator pendingBacklightStates];
-[SBBacklightCoordinator isAnyBacklightOn];
-[SBBacklightCoordinator removeBacklightController:];
-[SBBacklightCoordinator initWithSystemService:idleSleepPreventionInterval:];
-[SBBacklightCoordinator _preventIdleSleepForNumberOfSeconds:];
-[SBBacklightCoordinator setObservers:];
-[SBBacklightCoordinator setIdleSleepPreventionInterval:];
-[SBBacklightCoordinator observers];
-[SBBacklightCoordinator _mostActiveBacklightStateForControllers:includingPendingStates:];
-[SBBacklightCoordinator noteBacklightControllerState:willUpdateFromState:toState:forSource:];
-[SBBacklightCoordinator _notifyObserversOfAggregateBacklightStateChangeFromSource:];
-[SBBacklightCoordinator _setAggregateBacklightState:];
-[SBBacklightCoordinator pendingAggregateBacklightState];
-[SBBacklightCoordinator setSleepWakePolicy:];
```
