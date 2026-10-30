# `SBMainStatusBarStateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBStatusBarStateProvider`
- Protocols: `UIStatusBarStateObserver`
- 10 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBUserSessionController" _userSessionController;
B _killActivity;
[46B] _itemIsDisabled;
[46B] _itemWasDisabled;
[46@"NSCountedSet"] _itemDisabledRequests;
@"NSCountedSet" _dataUpdateAnimationsDisabledRequests;
B _timeCloaked;
B _allButBatteryCloaked;
B _telephonyAndBluetoothCloaked;
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
-[SBMainStatusBarStateProvider dealloc];
-[SBMainStatusBarStateProvider statusBarStateProvider:didPostStatusBarData:withActions:];
-[SBMainStatusBarStateProvider disableStatusBarItem:requestor:];
-[SBMainStatusBarStateProvider setTimeCloaked:];
-[SBMainStatusBarStateProvider _composePostDataFromAggregatorData:];
-[SBMainStatusBarStateProvider _identifierForStateAggregator:];
-[SBMainStatusBarStateProvider _shouldPostForVisitedItem:withUpdates:toAggregatorData:lastPost:];
-[SBMainStatusBarStateProvider _updateDisabledItems];
-[SBMainStatusBarStateProvider disableDataUpdateAnimationsForRequestor:];
-[SBMainStatusBarStateProvider enableStatusBarItem:requestor:];
-[SBMainStatusBarStateProvider initWithStateAggregator:userSessionController:lockScreenCoordinator:];
-[SBMainStatusBarStateProvider setAllItemsExceptBatteryCloaked:];
-[SBMainStatusBarStateProvider setTelephonyAndBluetoothItemsCloaked:];
-[SBMainStatusBarStateProvider statusBarStateAggregatorDidRequestImmediateUpdates:];
-[SBMainStatusBarStateProvider statusBarStateAggregatorDidStopRequestingImmediateUpdates:];
-[SBMainStatusBarStateProvider stopDisablingDataUpdateAnimationsForRequestor:];
```
