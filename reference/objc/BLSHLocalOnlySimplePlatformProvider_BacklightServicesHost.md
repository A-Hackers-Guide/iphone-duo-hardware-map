# `BLSHLocalOnlySimplePlatformProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightPlatformProvider`, `BLSHBacklightEnvironmentSessionProviding`, `BLSHServicePlatformProvider`
- 4 instance variables, 16 properties, 10 instance methods, 0 class methods

## Instance variables

```
f _backlightDimmedFactor;
d _backlightFadeInDuration;
d _backlightFadeOutDuration;
d _backlightDimmingDuration;
```

## Properties

```
@property (Td,R,N,V_backlightFadeInDuration) backlightFadeInDuration;
@property (Td,R,N,V_backlightFadeOutDuration) backlightFadeOutDuration;
@property (T@"<BLSHBacklightEnvironmentSessionProviding>",R,N) sessionProvider;
@property (TB,?,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (T@"BLSHFlipbookSpecification",?,R,N) flipbookSpecification;
@property (T@"<BLSHFlipbookTelemetry>",?,R,N) flipbookTelemetryDelegate;
@property (T@"<BLSHTelemetryServicePlatformDelegate>",?,R,N) telemetryServicePlatformDelegate;
@property (TB,?,R,N,GisUsingAlwaysOnBrightnessCurve) useAlwaysOnBrightnessCurve;
@property (Tf,?,R,N,V_backlightDimmedFactor) backlightDimmedFactor;
@property (Td,?,R,N,V_backlightDimmingDuration) backlightDimmingDuration;
@property (TB,?,R,N) suppressionSupported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BLSHBacklightPlatformProvider>",R,N) backlightPlatformProvider;
```

## Instance methods

```
-[BLSHLocalOnlySimplePlatformProvider removeObserver:];
-[BLSHLocalOnlySimplePlatformProvider sessionProvider];
-[BLSHLocalOnlySimplePlatformProvider createInactiveEnvironmentSession];
-[BLSHLocalOnlySimplePlatformProvider initWithConfiguration:];
-[BLSHLocalOnlySimplePlatformProvider addObserver:];
-[BLSHLocalOnlySimplePlatformProvider backlightDimmedFactor];
-[BLSHLocalOnlySimplePlatformProvider backlightDimmingDuration];
-[BLSHLocalOnlySimplePlatformProvider backlightFadeInDuration];
-[BLSHLocalOnlySimplePlatformProvider backlightFadeOutDuration];
-[BLSHLocalOnlySimplePlatformProvider backlightPlatformProvider];
```
