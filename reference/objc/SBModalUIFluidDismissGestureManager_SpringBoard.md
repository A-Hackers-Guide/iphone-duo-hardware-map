# `SBModalUIFluidDismissGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHomeGesturePanGestureRecognizerContextDelegate`, `BSTransactionObserver`, `PTSettingsKeyObserver`, `SBHomeGestureInteractionDelegate`
- 6 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"SBSystemGestureManager" _systemGestureManager;
@"SBWindowScene" _windowScene;
@"SBHomeGestureSettings" _homeGestureSettings;
@"SBHomeGestureInteraction" _homeGestureInteraction;
@"SBModalUIFluidDismissGestureWorkspaceTransaction" _currentTransaction;
@"BSCompoundAssertion" _observers;
```

## Properties

```
@property (T@"SBSystemGestureManager",R,N,V_systemGestureManager) systemGestureManager;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"SBHomeGestureSettings",&,N,V_homeGestureSettings) homeGestureSettings;
@property (T@"SBHomeGestureInteraction",&,N,V_homeGestureInteraction) homeGestureInteraction;
@property (T@"SBModalUIFluidDismissGestureWorkspaceTransaction",&,N,V_currentTransaction) currentTransaction;
@property (T@"BSCompoundAssertion",&,N,V_observers) observers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBModalUIFluidDismissGestureManager currentTransaction];
-[SBModalUIFluidDismissGestureManager transactionDidComplete:];
-[SBModalUIFluidDismissGestureManager homeGestureSettings];
-[SBModalUIFluidDismissGestureManager homeGestureInteraction:shouldReceiveTouch:];
-[SBModalUIFluidDismissGestureManager dealloc];
-[SBModalUIFluidDismissGestureManager homeGestureInteraction];
-[SBModalUIFluidDismissGestureManager setHomeGestureInteraction:];
-[SBModalUIFluidDismissGestureManager homeGestureInteractionBegan:];
-[SBModalUIFluidDismissGestureManager settings:changedValueForKey:];
-[SBModalUIFluidDismissGestureManager viewForSystemGestureRecognizer:];
-[SBModalUIFluidDismissGestureManager setHomeGestureSettings:];
-[SBModalUIFluidDismissGestureManager homeGestureInteractionChanged:];
-[SBModalUIFluidDismissGestureManager systemGestureManager];
-[SBModalUIFluidDismissGestureManager _addOrRemoveGestureForCurrentSettings];
-[SBModalUIFluidDismissGestureManager homeGestureInteractionEnded:];
-[SBModalUIFluidDismissGestureManager homeGestureInteraction:systemGestureTypeForType:];
-[SBModalUIFluidDismissGestureManager touchInterfaceOrientationForHomeGesturePanGestureRecognizer:];
-[SBModalUIFluidDismissGestureManager setObservers:];
-[SBModalUIFluidDismissGestureManager setCurrentTransaction:];
-[SBModalUIFluidDismissGestureManager customScreenEdgePanGestureRecognizerForHomeGestureInteraction:];
-[SBModalUIFluidDismissGestureManager observers];
-[SBModalUIFluidDismissGestureManager homeGestureInteractionCancelled:];
-[SBModalUIFluidDismissGestureManager windowScene];
-[SBModalUIFluidDismissGestureManager addObserver:forReason:];
-[SBModalUIFluidDismissGestureManager _dismissalTypeForCurrentContext];
-[SBModalUIFluidDismissGestureManager _notifyObserversDismissalEnded];
-[SBModalUIFluidDismissGestureManager handleGestureBegan:initiatedFromBottomEdge:];
-[SBModalUIFluidDismissGestureManager handleGestureBegan:initiatedFromBottomEdge:dismissalThreshold:initiatedFromIndirectEdge:];
-[SBModalUIFluidDismissGestureManager handleGestureChanged:];
-[SBModalUIFluidDismissGestureManager handleGestureEnded:];
-[SBModalUIFluidDismissGestureManager initWithWindowScene:systemGestureManager:];
```
