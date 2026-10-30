# `ALSManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ALSClientObserver`, `ALSClientRegistrationProtocol`, `CBHIDServiceProtocol`, `ALSRateManagerDelegate`
- 6 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
queue;
logHandle;
rateManager;
sensorContexts;
clients;
active;
```

## Instance methods

```
-[ALSManager copyStatusInfo];
-[ALSManager handleEvent:];
-[ALSManager addHIDServiceClient:];
-[ALSManager removeHIDServiceClient:];
-[ALSManager init];
-[ALSManager activateWithError:];
-[ALSManager cancel];
-[ALSManager addALSSensor:];
-[ALSManager applyInterval:forSensor:];
-[ALSManager clientReportIntervalUpdate:];
-[ALSManager clientStateUpdate:];
-[ALSManager getClients];
-[ALSManager handleHIDEvent:fromHIDServiceClient:];
-[ALSManager handleSensorEvent:];
-[ALSManager initWithRateManager:];
-[ALSManager newClient:];
-[ALSManager removeALSSensor:];
```
