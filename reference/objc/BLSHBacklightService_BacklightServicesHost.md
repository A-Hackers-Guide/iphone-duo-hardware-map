# `BLSHBacklightService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _stateMachines;
@"NSArray" _transitionStateMachines;
@"NSArray" _displayWakeTelemetries;
@"BLSHXPCBacklightProxyHostServer" _backlightXPCServer;
@"BLSHDiagnosticsServer" _diagnosticsServer;
@"BLSHWatchdogTester" _watchdogTester;
@"BLSHCriticalAssertTester" _criticalAssertTester;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_displayWakeTelemetries) displayWakeTelemetries;
```

## Class methods

```
+[BLSHBacklightService serviceWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:];
+[BLSHBacklightService serviceWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:localOnly:];
```

## Instance methods

```
-[BLSHBacklightService setFlipbookTelemetryDelegate:];
-[BLSHBacklightService displayWakeTelemetries];
-[BLSHBacklightService initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:];
```
