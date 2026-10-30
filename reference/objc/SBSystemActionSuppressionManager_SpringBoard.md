# `SBSystemActionSuppressionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMPocketStateDelegate`, `BLSBacklightStateObserving`, `SBSystemActionDataSourceObserver`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CMSuppressionManager" _suppressionManager;
@"CMPocketStateManager" _pocketStateManager;
@"SBSystemActionSuppressionManagerStateReducer" _stateReducer;
@"SBSystemActionSuppressionManagerState" _state;
B _subscribedToViewObstructionEvents;
@"NSHashTable" _observers;
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
-[SBSystemActionSuppressionManager _unsubscribeFromViewObstructionEvents];
-[SBSystemActionSuppressionManager backlight:didCompleteUpdateToState:forEvent:];
-[SBSystemActionSuppressionManager _subscribeToViewObstructionEvents];
-[SBSystemActionSuppressionManager _queryPocketStateWithTimeout:];
-[SBSystemActionSuppressionManager pocketStateManager:didUpdateState:];
-[SBSystemActionSuppressionManager systemActionDataSource:didUpdateSelectedAction:];
-[SBSystemActionSuppressionManager _updateViewObstructionSubscription];
-[SBSystemActionSuppressionManager backlight:didChangeAlwaysOnEnabled:];
-[SBSystemActionSuppressionManager _didReduceState:];
```
