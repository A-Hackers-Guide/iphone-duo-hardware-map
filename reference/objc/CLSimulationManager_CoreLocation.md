# `CLSimulationManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 43 instance methods, 0 class methods

## Instance variables

```
d _locationDistance;
d _locationInterval;
d _locationSpeed;
C _locationRepeatBehavior;
C _locationDeliveryBehavior;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"<CLSimulationXPCServerInterface>",R) daemonProxy;
@property (TC,N,V_locationDeliveryBehavior) locationDeliveryBehavior;
@property (Td,N,V_locationDistance) locationDistance;
@property (Td,N,V_locationInterval) locationInterval;
@property (Td,N,V_locationSpeed) locationSpeed;
@property (TC,N,V_locationRepeatBehavior) locationRepeatBehavior;
```

## Instance methods

```
-[CLSimulationManager init];
-[CLSimulationManager flush];
-[CLSimulationManager connection];
-[CLSimulationManager setConnection:];
-[CLSimulationManager flushWithReply:];
-[CLSimulationManager selectScenario:];
-[CLSimulationManager appendSimulatedLocation:];
-[CLSimulationManager availableScenarios];
-[CLSimulationManager cl_waitOnRunningReplyWithTimeout:isSimulationRunning:block:];
-[CLSimulationManager clearSimulatedCells];
-[CLSimulationManager clearSimulatedLocations];
-[CLSimulationManager daemonProxy];
-[CLSimulationManager flushSynchronouslyWithTimeout:isSimulationRunning:];
-[CLSimulationManager getFencesForBundleID:withHandler:];
-[CLSimulationManager isSimulationRunningSynchronouslyWithTimeout:isSimulationRunning:];
-[CLSimulationManager isSimulationRunningWithReply:];
-[CLSimulationManager loadScenarioFromURL:];
-[CLSimulationManager localizedNameForScenario:];
-[CLSimulationManager locationDeliveryBehavior];
-[CLSimulationManager locationDistance];
-[CLSimulationManager locationInterval];
-[CLSimulationManager locationRepeatBehavior];
-[CLSimulationManager locationSpeed];
-[CLSimulationManager scenariosPath];
-[CLSimulationManager setLocationDeliveryBehavior:];
-[CLSimulationManager setLocationDistance:];
-[CLSimulationManager setLocationInterval:];
-[CLSimulationManager setLocationRepeatBehavior:];
-[CLSimulationManager setLocationSpeed:];
-[CLSimulationManager setSimulatedCell:];
-[CLSimulationManager setSimulatedCellRegistrationStatus:];
-[CLSimulationManager setSimulatedWifiPower:];
-[CLSimulationManager setWifiScanResults:];
-[CLSimulationManager simulateBeaconWithProximityUUID:major:minor:eventType:];
-[CLSimulationManager simulateFenceWithBundleID:andFenceID:eventType:atLocation:];
-[CLSimulationManager simulateSignificantLocationChange:];
-[CLSimulationManager simulateVisit:];
-[CLSimulationManager startCellSimulation];
-[CLSimulationManager startLocationSimulation];
-[CLSimulationManager startWifiSimulation];
-[CLSimulationManager stopCellSimulation];
-[CLSimulationManager stopLocationSimulation];
-[CLSimulationManager stopWifiSimulation];
```
