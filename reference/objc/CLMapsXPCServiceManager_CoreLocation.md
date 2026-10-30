# `CLMapsXPCServiceManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSTimer" fInactivityTimer;
d fTimerUpdateMachContTime;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
```

## Class methods

```
+[CLMapsXPCServiceManager sharedInstance];
+[CLMapsXPCServiceManager allocWithZone:];
```

## Instance methods

```
-[CLMapsXPCServiceManager createConnection];
-[CLMapsXPCServiceManager dealloc];
-[CLMapsXPCServiceManager updateTimer];
-[CLMapsXPCServiceManager connection];
-[CLMapsXPCServiceManager setConnection:];
-[CLMapsXPCServiceManager copyWithZone:];
-[CLMapsXPCServiceManager cancelRoadDataRequest];
-[CLMapsXPCServiceManager clearMemoryAndExitHelperProcessCleanly];
-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:includeRoadNames:WithReply:];
-[CLMapsXPCServiceManager constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:];
-[CLMapsXPCServiceManager fetchSimplifiedRoadSegmentsAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:clearTiles:maxSegments:withReply:];
-[CLMapsXPCServiceManager findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:callSynchronously:withReply:];
-[CLMapsXPCServiceManager onTimerFire:];
-[CLMapsXPCServiceManager releaseMapHelperServiceOSTransaction];
-[CLMapsXPCServiceManager sendConfigurationSettings];
-[CLMapsXPCServiceManager stopConstructRouteFromLocation];
```
