# `CLTripSegmentProcessorManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fQueue;
{CLTripSegmentProcessor="fDistanceCalculator"{CLDistanceCalc="fM"d"fN"d"fRefLatRads"d"fRefLatDegs"d"fCosRefLat"d}"fRecorder"{CLTripSegmentRecorder="fRecordingEnabled"B"fFileNameShouldContainTime"B"fFileNamePrefix"@"NSString""fRecordingDirectory"@"NSString"}} cltsp;
```

## Instance methods

```
-[CLTripSegmentProcessorManager init];
-[CLTripSegmentProcessorManager dealloc];
-[CLTripSegmentProcessorManager cancelMapHelperRoadDataRequest];
-[CLTripSegmentProcessorManager clearMapHelperMemoryAndExitCleanly];
-[CLTripSegmentProcessorManager constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:];
-[CLTripSegmentProcessorManager constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager constructRouteWithID:withOptions:usingRoadData:startRoad:endRoad:modeOfTransport:outputHandler:];
-[CLTripSegmentProcessorManager constructRouteWithID:withOptions:usingRoadData:startRoad:endRoad:modeOfTransport:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager errorObject:description:];
-[CLTripSegmentProcessorManager generateWaypointsOnTheRoute:forRouteID:withOptions:modeOfTransport:outputHandler:];
-[CLTripSegmentProcessorManager generateWaypointsOnTheRoute:forRouteID:withOptions:modeOfTransport:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager getMatchedLocationCandidates:dataID:modeOfTransport:options:outputHandler:];
-[CLTripSegmentProcessorManager getMatchedLocationCandidates:dataID:modeOfTransport:options:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager getWaypointsSubsetFromSnapPointOnRoute:modeOfTransport:snapLocation:snapRoad:waypoints:routeID:withOptions:outputHandler:];
-[CLTripSegmentProcessorManager killProcessingWithID:];
-[CLTripSegmentProcessorManager matchLocations:toRoute:waypoints:withOptions:andRouteID:modeOfTransport:outputHandler:];
-[CLTripSegmentProcessorManager matchLocations:toRoute:waypoints:withOptions:andRouteID:modeOfTransport:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager matchLocations:toRoute:withOptions:andRouteID:modeOfTransport:outputHandler:];
-[CLTripSegmentProcessorManager outputRouteLearningDebuggingDataInCLTSPFile:];
-[CLTripSegmentProcessorManager processTripSegmentData:withOptions:outputHandler:];
-[CLTripSegmentProcessorManager processTripSegmentData:withOptions:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager propagateLocation:route:distance:withOptions:modeOfTransport:outputHandler:];
-[CLTripSegmentProcessorManager propagateLocation:route:distance:withOptions:modeOfTransport:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager simulateLocationOnRouteID:withOptions:usingRoadData:modeOfTransport:constantSpeed:outputHandler:];
-[CLTripSegmentProcessorManager simulateLocationOnRouteID:withOptions:usingRoadData:modeOfTransport:constantSpeed:outputHandler:completionHandler:];
-[CLTripSegmentProcessorManager simulateSparseTrajectoryAndSubmitCoreAnalytics:];
```
