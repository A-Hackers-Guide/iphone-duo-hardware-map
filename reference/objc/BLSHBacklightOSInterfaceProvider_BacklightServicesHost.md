# `BLSHBacklightOSInterfaceProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHBacklightOSTimerProvider`
- Protocols: `BLSHBacklightOSInterfaceProviding`, `BLSHWatchdogProviderDelegate`, `BLSHBacklightPlatformProviderObserver`
- 18 instance variables, 14 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"<BLSHBacklightPlatformProvider>" _platformProvider;
@"BLSHWatchdogProvider" _watchdogProvider;
@"BLSHCriticalAssertProvider" _criticalAssertProvider;
@"NSMutableDictionary" _lock_sceneObservers;
@"NSMutableSet" _lock_sceneWorkspaces;
@"CBDisplayStateClient" _displayStateClient;
@"CADisplayStateControl" _displayStateControl;
@"BSContinuousMachTimer" _setCBDisplayModeTimer;
@"<BLSHResourceArbitrating>" _flipbookArbiter;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_flipbookTransparent;
B _deviceSupportsAlwaysOn;
B _deviceSupportsAlwaysOnFlipbook;
B _deviceSupportsAlwaysOnFlipbookWatchdog;
@"NSArray" _displayInterfaces;
@"NSArray" _displayReferences;
Q _flipbookDiagnosticHistoryFrameLimit;
Q _flipbookDiagnosticHistoryMemoryLimit;
```

## Properties

```
@property (T@"<BLSHResourceArbitrating>",R,N) flipbookArbiter;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (TB,R,N) deviceSupportsAlwaysOnFlipbook;
@property (TB,R,N) deviceSupportsAlwaysOnFlipbookWatchdog;
@property (TQ,R,N,V_flipbookDiagnosticHistoryFrameLimit) flipbookDiagnosticHistoryFrameLimit;
@property (TQ,R,N,V_flipbookDiagnosticHistoryMemoryLimit) flipbookDiagnosticHistoryMemoryLimit;
@property (TQ,R,N) mach_continuous_time;
@property (Td,R,N) bsContinuousMachTimeNow;
@property (T@"NSDate",R,N) now;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,R,N,GisTesting) testing;
```

## Class methods

```
+[BLSHBacklightOSInterfaceProvider sharedProvider];
+[BLSHBacklightOSInterfaceProvider setSharedProvider:];
```

## Instance methods

```
-[BLSHBacklightOSInterfaceProvider deregisterSceneWorkspace:];
-[BLSHBacklightOSInterfaceProvider registerHandlersForService:];
-[BLSHBacklightOSInterfaceProvider deviceSupportsAlwaysOn];
-[BLSHBacklightOSInterfaceProvider displayReferences];
-[BLSHBacklightOSInterfaceProvider systemSleepMonitor];
-[BLSHBacklightOSInterfaceProvider platformProvider:didChangeAlwaysOnSetting:];
-[BLSHBacklightOSInterfaceProvider deviceSupportsAlwaysOnFlipbook];
-[BLSHBacklightOSInterfaceProvider removeSceneObserver:forSceneIdentityToken:];
-[BLSHBacklightOSInterfaceProvider abortForWatchdog:payload:payloadSize:explanation:];
-[BLSHBacklightOSInterfaceProvider addSceneObserver:forSceneIdentityToken:];
-[BLSHBacklightOSInterfaceProvider createSystemActivityAssertionWithIdentifier:configurator:];
-[BLSHBacklightOSInterfaceProvider flipbookDiagnosticHistoryMemoryLimit];
-[BLSHBacklightOSInterfaceProvider displayInterfaces];
-[BLSHBacklightOSInterfaceProvider isTailspinAvailable];
-[BLSHBacklightOSInterfaceProvider registerSceneWorkspace:];
-[BLSHBacklightOSInterfaceProvider deviceSupportsAlwaysOnFlipbookWatchdog];
-[BLSHBacklightOSInterfaceProvider sceneWithIdentityToken:];
-[BLSHBacklightOSInterfaceProvider observeSignificantTimeChangeWithIdentifier:handler:];
-[BLSHBacklightOSInterfaceProvider flipbookArbiter];
-[BLSHBacklightOSInterfaceProvider createPowerAssertionWithIdentifier:];
-[BLSHBacklightOSInterfaceProvider platformProviderDidDetectSignificantUserInteraction:];
-[BLSHBacklightOSInterfaceProvider writeTailspinForWatchdog:completion:];
-[BLSHBacklightOSInterfaceProvider scheduleWatchdogWithDelegate:explanation:timeout:];
-[BLSHBacklightOSInterfaceProvider initWithPlatformProvider:];
-[BLSHBacklightOSInterfaceProvider panicForWatchdog:withDelay:completion:];
-[BLSHBacklightOSInterfaceProvider dispatchToMainQueueAfterSecondsDelay:identifier:block:];
-[BLSHBacklightOSInterfaceProvider flipbookDiagnosticHistoryFrameLimit];
```
