# `CMOdometerSuitabilityManagerProxy`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSObject<OS_dispatch_queue>" fCallbackQueue;
^v fLocationdConnection;
@? fHandler;
@"CMOdometerSuitabilityManager" _odometerSuitabilityManager;
d _startDate;
d _suitableForRunning;
d _suitableForWalking;
```

## Properties

```
@property (T@"CMOdometerSuitabilityManager",N,V_odometerSuitabilityManager) odometerSuitabilityManager;
@property (Td,V_startDate) startDate;
@property (Td,V_suitableForRunning) suitableForRunning;
@property (Td,V_suitableForWalking) suitableForWalking;
```

## Instance methods

```
-[CMOdometerSuitabilityManagerProxy startDate];
-[CMOdometerSuitabilityManagerProxy setStartDate:];
-[CMOdometerSuitabilityManagerProxy dealloc];
-[CMOdometerSuitabilityManagerProxy _teardown];
-[CMOdometerSuitabilityManagerProxy _stopOdometerSuitabilityUpdates];
-[CMOdometerSuitabilityManagerProxy _startDaemonConnection];
-[CMOdometerSuitabilityManagerProxy _startOdometerSuitabilityUpdatesWithHandler:];
-[CMOdometerSuitabilityManagerProxy initWithOdometerSuitability:];
-[CMOdometerSuitabilityManagerProxy odometerSuitabilityManager];
-[CMOdometerSuitabilityManagerProxy setOdometerSuitabilityManager:];
-[CMOdometerSuitabilityManagerProxy setSuitableForRunning:];
-[CMOdometerSuitabilityManagerProxy setSuitableForWalking:];
-[CMOdometerSuitabilityManagerProxy suitableForRunning];
-[CMOdometerSuitabilityManagerProxy suitableForWalking];
```
