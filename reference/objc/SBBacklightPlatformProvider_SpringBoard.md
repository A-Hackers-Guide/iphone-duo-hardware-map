# `SBBacklightPlatformProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlwaysOnUserPreferenceProvider`, `SBBacklightSignificantUserInteractionMonitorObserver`, `BLSHFlipbookTelemetry`, `BLSHBacklightPlatformProvider`, `SBWindowSceneAttachmentObserving`
- 12 instance variables, 17 properties, 31 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"SBFWakeAnimationSettings" _wakeAnimationSettings;
@"SBBacklightEnvironmentSessionProvider" _sessionProvider;
@"SBAlwaysOnDefaults" _alwaysOnDefaults;
@"SBAveragePixelLuminanceLimitController" _aplLimitController;
@"BLSHFlipbookSpecification" _flipbookSpecification;
@"<BLSHFlipbookTelemetry>" _telemetryEmitter;
@"SBAlwaysOnPolicyCoordinator" _alwaysOnPolicyCoordinator;
@"NSHashTable" _signficantUserInteractionMonitors;
B _lock_alwaysOnEnabled;
B _lock_forceAlwaysOnUserPreferenceEnabled;
@"NSHashTable" _lock_alwaysOnObservers;
```

## Properties

```
@property (T@"SBAlwaysOnPolicyCoordinator",R,N,V_alwaysOnPolicyCoordinator) alwaysOnPolicyCoordinator;
@property (TB,N,V_lock_forceAlwaysOnUserPreferenceEnabled) forceAlwaysOnUserPreferenceEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N) backlightFadeInDuration;
@property (Td,R,N) backlightFadeOutDuration;
@property (T@"<BLSHBacklightEnvironmentSessionProviding>",R,N) sessionProvider;
@property (TB,?,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (T@"BLSHFlipbookSpecification",?,R,N) flipbookSpecification;
@property (T@"<BLSHFlipbookTelemetry>",?,R,N) flipbookTelemetryDelegate;
@property (T@"<BLSHTelemetryServicePlatformDelegate>",?,R,N) telemetryServicePlatformDelegate;
@property (TB,?,R,N,GisUsingAlwaysOnBrightnessCurve) useAlwaysOnBrightnessCurve;
@property (Tf,?,R,N) backlightDimmedFactor;
@property (Td,?,R,N) backlightDimmingDuration;
@property (TB,?,R,N) suppressionSupported;
```

## Class methods

```
+[SBBacklightPlatformProvider deviceSupportsAlwaysOn];
```

## Instance methods

```
-[SBBacklightPlatformProvider alwaysOnPolicyCoordinator];
-[SBBacklightPlatformProvider isAlwaysOnEnabled];
-[SBBacklightPlatformProvider removeObserver:];
-[SBBacklightPlatformProvider init];
-[SBBacklightPlatformProvider windowSceneDidDisconnect:];
-[SBBacklightPlatformProvider sessionProvider];
-[SBBacklightPlatformProvider logTelemetryForRenderSession:];
-[SBBacklightPlatformProvider addObserver:];
-[SBBacklightPlatformProvider initWithBacklightEnvironmentSessionProvider:];
-[SBBacklightPlatformProvider logTelemetryForRequestDates:];
-[SBBacklightPlatformProvider logTelemetryForInvalidation:];
-[SBBacklightPlatformProvider windowSceneDidConnect:];
-[SBBacklightPlatformProvider _notifyObserversOfSignificantUserInteraction];
-[SBBacklightPlatformProvider _registerHandlersForService:];
-[SBBacklightPlatformProvider _updateAlwaysOnEnabled];
-[SBBacklightPlatformProvider addSignificantUserInteractionMonitor:];
-[SBBacklightPlatformProvider backlightDimmedFactor];
-[SBBacklightPlatformProvider backlightDimmingDuration];
-[SBBacklightPlatformProvider backlightFadeInDuration];
-[SBBacklightPlatformProvider backlightFadeOutDuration];
-[SBBacklightPlatformProvider completeInitializationAfterBLSStartup];
-[SBBacklightPlatformProvider criticalAssertDidFail:resetFailure:];
-[SBBacklightPlatformProvider flipbookSpecification];
-[SBBacklightPlatformProvider flipbookTelemetryDelegate];
-[SBBacklightPlatformProvider forceAlwaysOnUserPreferenceEnabled];
-[SBBacklightPlatformProvider noteSignificantEvent];
-[SBBacklightPlatformProvider removeSignificantUserInteractionMonitor:];
-[SBBacklightPlatformProvider setForceAlwaysOnUserPreferenceEnabled:];
-[SBBacklightPlatformProvider significantUserInteractionMonitorDetectedSignificantUserInteraction:];
-[SBBacklightPlatformProvider suppressionSupported];
-[SBBacklightPlatformProvider telemetryServicePlatformDelegate];
```
