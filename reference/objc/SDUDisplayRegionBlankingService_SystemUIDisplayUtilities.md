# `SDUDisplayRegionBlankingService`

- Image: [`/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`](../userland/System__Library__PrivateFrameworks__SystemUIDisplayUtilities.framework__SystemUIDisplayUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SDUDisplayRegionBlankingServerToClientInterface`, `SDUDisplayRegionBlankingObserver`
- 7 instance variables, 4 properties, 18 instance methods, 3 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnection" _connection;
@"NSMutableDictionary" _regionIdentifierToBlankingState;
@"NSMutableDictionary" _regionIdentifierToBlankingStateObservers;
@"NSMutableDictionary" _regionIdentifierToBlankingStateObservationEnabled;
B _observingInProcessCoordinator;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SDUDisplayRegionBlankingService sharedInstance];
+[SDUDisplayRegionBlankingService new];
+[SDUDisplayRegionBlankingService setInProcessCoordinator:];
```

## Instance methods

```
-[SDUDisplayRegionBlankingService init];
-[SDUDisplayRegionBlankingService dealloc];
-[SDUDisplayRegionBlankingService _init];
-[SDUDisplayRegionBlankingService _locked_serverTarget];
-[SDUDisplayRegionBlankingService _unlocked_serverTarget];
-[SDUDisplayRegionBlankingService acquireBlankingAssertionForDisplayRegion:reason:restrictingToBundleIDs:];
-[SDUDisplayRegionBlankingService addBlankingStateObserver:forDisplayRegion:];
-[SDUDisplayRegionBlankingService _locked_blankingStateDidChange:forDisplayRegion:at:];
-[SDUDisplayRegionBlankingService _locked_blankingStateWillChange:forDisplayRegion:at:];
-[SDUDisplayRegionBlankingService _locked_evaluateInProcessCoordinatorBlankingStateObservation];
-[SDUDisplayRegionBlankingService _locked_setBlankingStateObservationEnabled:forDisplayRegion:];
-[SDUDisplayRegionBlankingService _locked_updateObserver:withBlankingState:forDisplayRegion:];
-[SDUDisplayRegionBlankingService _locked_updateServerWithBlankingStateObservationStateForDisplayRegion:];
-[SDUDisplayRegionBlankingService blankingStateDidChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SDUDisplayRegionBlankingService blankingStateForDisplayRegion:];
-[SDUDisplayRegionBlankingService blankingStateWillChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SDUDisplayRegionBlankingService displayRegion:blankingStateDidChange:at:];
-[SDUDisplayRegionBlankingService displayRegion:blankingStateWillChange:at:];
```
