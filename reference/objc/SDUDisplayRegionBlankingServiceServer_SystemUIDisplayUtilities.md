# `SDUDisplayRegionBlankingServiceServer`

- Image: [`/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`](../userland/System__Library__PrivateFrameworks__SystemUIDisplayUtilities.framework__SystemUIDisplayUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SDUDisplayRegionBlankingClientToServerInterface`, `BSInvalidatable`
- 9 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _isValid;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clientServiceCollectionLock;
@"NSMutableArray" _connections;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnectionListener" _connectionListener;
@"NSMutableDictionary" _regionIdentifierToDisplayRegionBlankingController;
@"NSMutableDictionary" _regionIdentifierToUUIDAssertionMap;
@"NSMutableDictionary" _regionIdentifierToBlankingStateObservingConnections;
@"NSMapTable" _connectionToAssertionUUIDs;
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
-[SDUDisplayRegionBlankingServiceServer listener:didReceiveConnection:withContext:];
-[SDUDisplayRegionBlankingServiceServer init];
-[SDUDisplayRegionBlankingServiceServer invalidate];
-[SDUDisplayRegionBlankingServiceServer acquireDisplayRegionBlankingAssertionWithUniqueIdentifier:forDisplayRegion:reason:restrictingToBundleIDs:];
-[SDUDisplayRegionBlankingServiceServer blankingStateForDisplayRegion:];
-[SDUDisplayRegionBlankingServiceServer displayRegion:blankingStateDidChange:at:];
-[SDUDisplayRegionBlankingServiceServer displayRegion:blankingStateWillChange:at:];
-[SDUDisplayRegionBlankingServiceServer displayRegionBlankingControllerForDisplayRegion:];
-[SDUDisplayRegionBlankingServiceServer invalidateAllAssertionsForConnection:];
-[SDUDisplayRegionBlankingServiceServer invalidateDisplayRegionBlankingAssertionWithUniqueIdentifier:forDisplayRegion:];
-[SDUDisplayRegionBlankingServiceServer removeConnectionFromAllObserverSets:];
-[SDUDisplayRegionBlankingServiceServer setBlankingController:forDisplayRegion:];
-[SDUDisplayRegionBlankingServiceServer setBlankingStateObservationEnabled:forDisplayRegion:];
```
