# `BLSHService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 9 instance methods, 5 class methods

## Instance variables

```
@"BLSHAssertionService" _assertionService;
@"BLSHBacklightOSInterfaceProvider" _osInterfaceProvider;
@"BLSHBacklightService" _backlightService;
@"BLSHDefaultsObserver" _defaultsObserver;
@"BLSHSystemWakeTelemetry" _systemWakeTelemetry;
Q _stateHandler;
@"<BLSHServicePlatformProvider>" _platformProvider;
@"<BLSHInactiveBudgetPolicing>" _inactiveBudgetPolicy;
```

## Properties

```
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (T@"<BLSHServicePlatformProvider>",R,N,V_platformProvider) platformProvider;
@property (T@"BLSHLocalAssertionService",R,N) localAssertionService;
@property (T@"<BLSHInactiveBudgetPolicing>",R,N,V_inactiveBudgetPolicy) inactiveBudgetPolicy;
```

## Class methods

```
+[BLSHService sharedService];
+[BLSHService earlyInitialization];
+[BLSHService startServiceWithPlatformProvider:];
+[BLSHService startLocalOnlyServiceWithConfiguration:];
+[BLSHService startServiceWithPlatformProvider:localOnly:];
```

## Instance methods

```
-[BLSHService deregisterSceneWorkspace:];
-[BLSHService deviceSupportsAlwaysOn];
-[BLSHService platformProvider];
-[BLSHService dealloc];
-[BLSHService registerSceneWorkspace:];
-[BLSHService localAssertionService];
-[BLSHService beginSpecialManagementForHostEnvironment:];
-[BLSHService inactiveBudgetPolicy];
-[BLSHService initWithPlatformProvider:localOnly:];
```
