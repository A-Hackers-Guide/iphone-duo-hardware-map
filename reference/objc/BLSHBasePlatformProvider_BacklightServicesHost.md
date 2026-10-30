# `BLSHBasePlatformProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightEnvironmentSessionProviding`, `BLSHServicePlatformProvider`, `BLSHBacklightPlatformProvider`
- 13 instance variables, 17 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _lock_observers;
@"<BLSHBacklightEnvironmentSessionProviding>" _lock_sessionProvider;
@? _lock_sessionProviderFactory;
@"BLSHService" _lock_service;
@"BLSHFlipbookSpecification" _lock_flipbookSpecification;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
d _lock_backlightFadeInDuration;
d _lock_backlightFadeOutDuration;
d _lock_backlightDimmingDuration;
f _lock_backlightDimmedFactor;
B _alwaysOnSupportedByHardware;
B _lock_alwaysOnSettingEnabled;
B _suppressionSupported;
```

## Properties

```
@property (Td,N) backlightFadeInDuration;
@property (Td,N) backlightFadeOutDuration;
@property (Td,N) backlightDimmingDuration;
@property (Tf,N) backlightDimmedFactor;
@property (T@"BLSHFlipbookSpecification",N) flipbookSpecification;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,N,GisAlwaysOnSettingEnabled) alwaysOnSettingEnabled;
@property (T@"<BLSHBacklightEnvironmentSessionProviding>",&,N) sessionProvider;
@property (TB,N,V_suppressionSupported) suppressionSupported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BLSHBacklightPlatformProvider>",R,N) backlightPlatformProvider;
@property (T@"<BLSHFlipbookTelemetry>",?,R,N) flipbookTelemetryDelegate;
@property (T@"<BLSHTelemetryServicePlatformDelegate>",?,R,N) telemetryServicePlatformDelegate;
@property (TB,?,R,N,GisUsingAlwaysOnBrightnessCurve) useAlwaysOnBrightnessCurve;
```

## Instance methods

```
-[BLSHBasePlatformProvider isAlwaysOnEnabled];
-[BLSHBasePlatformProvider removeObserver:];
-[BLSHBasePlatformProvider init];
-[BLSHBasePlatformProvider sessionProvider];
-[BLSHBasePlatformProvider createInactiveEnvironmentSession];
-[BLSHBasePlatformProvider addObserver:];
-[BLSHBasePlatformProvider setSessionProvider:];
-[BLSHBasePlatformProvider notifyObserversWithBlock:];
-[BLSHBasePlatformProvider backlightDimmedFactor];
-[BLSHBasePlatformProvider backlightDimmingDuration];
-[BLSHBasePlatformProvider backlightFadeInDuration];
-[BLSHBasePlatformProvider backlightFadeOutDuration];
-[BLSHBasePlatformProvider backlightPlatformProvider];
-[BLSHBasePlatformProvider flipbookSpecification];
-[BLSHBasePlatformProvider serviceInitializing:];
-[BLSHBasePlatformProvider suppressionSupported];
-[BLSHBasePlatformProvider _lock_isAlwaysOnEnabled];
-[BLSHBasePlatformProvider isAlwaysOnSettingEnabled];
-[BLSHBasePlatformProvider platformDidDetectSignificantUserInteraction];
-[BLSHBasePlatformProvider setAlwaysOnSettingEnabled:];
-[BLSHBasePlatformProvider setBacklightDimmedFactor:];
-[BLSHBasePlatformProvider setBacklightDimmingDuration:];
-[BLSHBasePlatformProvider setBacklightFadeInDuration:];
-[BLSHBasePlatformProvider setBacklightFadeOutDuration:];
-[BLSHBasePlatformProvider setFlipbookSpecification:];
-[BLSHBasePlatformProvider setSessionProviderFactory:];
-[BLSHBasePlatformProvider setSuppressionSupported:];
```
