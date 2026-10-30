# `CLMapHelperService`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLMapHelperServiceProtocol`
- 9 instance variables, 0 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"GEOMapFeatureAccess" fGEOMapFeatureAccess;
@"<GEOMapFeatureAccessRequest>" fGeoMapFeatureRoadRequest;
B fHasEntitlementForRoadData;
B fHasEntitlementForBuildingData;
@"NSObject<OS_os_transaction>" fTransaction;
B fRoadDataRequestInProgress;
B fExternalSignalReceivedToStopConstructVehicularRouteProcessing;
B fEnableDebugLogging;
```

## Instance methods

```
-[CLMapHelperService init];
-[CLMapHelperService releaseOSTransaction];
-[CLMapHelperService cancelRoadDataRequest];
-[CLMapHelperService clearMemoryAndExitCleanly];
-[CLMapHelperService configureWithSettings:];
-[CLMapHelperService constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:];
-[CLMapHelperService convertCLMapRoadVectorToRoadDictionaryArray:];
-[CLMapHelperService fetchGEOBuildingDataAroundCoordinate:inRadius:tileSetStyle:allowNetwork:preferCachedTiles:clearTiles:withReply:];
-[CLMapHelperService fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:useStartOfRoad:returnRoads:];
-[CLMapHelperService fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:includeRoadNames:withReply:];
-[CLMapHelperService fetchGEORoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:ignoreUTurns:returnRoads:];
-[CLMapHelperService fetchSimplifiedRoadSegmentsAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:clearTiles:maxSegments:withReply:];
-[CLMapHelperService findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:withReply:];
-[CLMapHelperService getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:gmfRoad:];
-[CLMapHelperService getGEOMapFeatureRoadDataAroundLatitude:longitude:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:];
-[CLMapHelperService internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:];
-[CLMapHelperService makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:useStartOfRoad:returnRoads:];
-[CLMapHelperService scanTunnelWalkingBackward:fromRoad:gmf:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:];
-[CLMapHelperService setEnableDebugLogging:];
-[CLMapHelperService setEntitlementsForBuilding:];
-[CLMapHelperService setEntitlementsForRoad:];
-[CLMapHelperService stopConstructRouteFromLocation];
-[CLMapHelperService takeOSTransaction];
```
