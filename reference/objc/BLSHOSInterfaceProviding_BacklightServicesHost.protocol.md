# `BLSHOSInterfaceProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSHOSTimerProviding`
- 0 instance variables, 5 properties, 12 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (TB,R,N) deviceSupportsAlwaysOnFlipbook;
@property (TB,R,N) deviceSupportsAlwaysOnFlipbookWatchdog;
@property (TQ,R,N) flipbookDiagnosticHistoryFrameLimit;
@property (TQ,R,N) flipbookDiagnosticHistoryMemoryLimit;
```

## Instance methods

```
-[BLSHOSInterfaceProviding deviceSupportsAlwaysOn];
-[BLSHOSInterfaceProviding systemSleepMonitor];
-[BLSHOSInterfaceProviding deviceSupportsAlwaysOnFlipbook];
-[BLSHOSInterfaceProviding removeSceneObserver:forSceneIdentityToken:];
-[BLSHOSInterfaceProviding addSceneObserver:forSceneIdentityToken:];
-[BLSHOSInterfaceProviding createSystemActivityAssertionWithIdentifier:configurator:];
-[BLSHOSInterfaceProviding flipbookDiagnosticHistoryMemoryLimit];
-[BLSHOSInterfaceProviding deviceSupportsAlwaysOnFlipbookWatchdog];
-[BLSHOSInterfaceProviding observeSignificantTimeChangeWithIdentifier:handler:];
-[BLSHOSInterfaceProviding createPowerAssertionWithIdentifier:];
-[BLSHOSInterfaceProviding scheduleWatchdogWithDelegate:explanation:timeout:];
-[BLSHOSInterfaceProviding flipbookDiagnosticHistoryFrameLimit];
```
