# `BLSHBacklightPlatformProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 17 instance methods, 0 class methods

## Properties

```
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

## Instance methods

```
-[BLSHBacklightPlatformProvider removeObserver:];
-[BLSHBacklightPlatformProvider sessionProvider];
-[BLSHBacklightPlatformProvider addObserver:];
-[BLSHBacklightPlatformProvider backlightFadeInDuration];
-[BLSHBacklightPlatformProvider backlightFadeOutDuration];
-[BLSHBacklightPlatformProvider isAlwaysOnEnabled];
-[BLSHBacklightPlatformProvider backlightDimmedFactor];
-[BLSHBacklightPlatformProvider backlightDimmingDuration];
-[BLSHBacklightPlatformProvider flipbookSpecification];
-[BLSHBacklightPlatformProvider flipbookTelemetryDelegate];
-[BLSHBacklightPlatformProvider isEnvironmentTransitionAnimatedToState:fromPreviousState:];
-[BLSHBacklightPlatformProvider isTransitionForcedUnanimatedForSource:];
-[BLSHBacklightPlatformProvider isTransitionForcedUnanimatedToState:fromPreviousState:];
-[BLSHBacklightPlatformProvider isUsingAlwaysOnBrightnessCurve];
-[BLSHBacklightPlatformProvider suppressionSupported];
-[BLSHBacklightPlatformProvider telemetryServicePlatformDelegate];
-[BLSHBacklightPlatformProvider useAlwaysOnBrightnessCurve:withRampDuration:];
```
