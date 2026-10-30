# `TURouteController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 14 properties, 36 instance methods, 0 class methods

## Instance variables

```
f _volume;
@"NSObject<OS_dispatch_queue>" _queue;
@"<TURouteControllerActions>" _actionsDelegate;
@"NSHashTable" _delegates;
@"NSDictionary" _routesByUniqueIdentifier;
@"NSDictionary" _disabledRoutesByUniqueIdentifier;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T^v,R,N) queueContext;
@property (T@"<TURouteControllerActions>",R,W,N,V_actionsDelegate) actionsDelegate;
@property (T@"NSHashTable",R,N,V_delegates) delegates;
@property (T@"NSDictionary",C,N,V_routesByUniqueIdentifier) routesByUniqueIdentifier;
@property (T@"NSDictionary",C,N,V_disabledRoutesByUniqueIdentifier) disabledRoutesByUniqueIdentifier;
@property (T@"NSArray",R,C,N) routes;
@property (T@"NSArray",R,C,N) disabledRoutes;
@property (T@"TURoute",R,C,N) pickedRoute;
@property (T@"TURoute",R,C,N) receiverRoute;
@property (T@"TURoute",R,C,N) speakerRoute;
@property (TB,R,N) areAuxiliaryRoutesAvailable;
@property (TB,R,N) hasOnlyBuiltInRoutes;
@property (Tf,N,V_volume) volume;
```

## Instance methods

```
-[TURouteController performBlockOnQueue:];
-[TURouteController queueContext];
-[TURouteController handleServerDisconnect];
-[TURouteController removeDelegate:];
-[TURouteController actionsDelegate];
-[TURouteController routes];
-[TURouteController delegates];
-[TURouteController handleServerReconnect];
-[TURouteController addDelegate:];
-[TURouteController volume];
-[TURouteController dealloc];
-[TURouteController setVolume:];
-[TURouteController queue];
-[TURouteController pickedRoute];
-[TURouteController pickRoute:];
-[TURouteController disabledRoutes];
-[TURouteController areAuxiliaryRoutesAvailable];
-[TURouteController disabledRoutesByUniqueIdentifier];
-[TURouteController fetchRoutesSynchronously];
-[TURouteController handleDisabledRoutesByUniqueIdentifierUpdated:];
-[TURouteController handleRoutesByUniqueIdentifierUpdated:];
-[TURouteController handleVolumeUpdateFromHost:];
-[TURouteController hasOnlyBuiltInRoutes];
-[TURouteController initWithActionsDelegate:serialQueue:];
-[TURouteController pickRoute:routeSelectionProvenance:];
-[TURouteController pickRouteWhenAvailableWithUniqueIdentifier:];
-[TURouteController pickRouteWhenAvailableWithUniqueIdentifier:routeSelectionProvenance:];
-[TURouteController pickRouteWithUniqueIdentifier:];
-[TURouteController pickRouteWithUniqueIdentifier:routeSelectionProvenance:];
-[TURouteController receiverRoute];
-[TURouteController requeryRoutes];
-[TURouteController routeWithSourceIdentifier:];
-[TURouteController routesByUniqueIdentifier];
-[TURouteController setDisabledRoutesByUniqueIdentifier:];
-[TURouteController setRoutesByUniqueIdentifier:];
-[TURouteController speakerRoute];
```
