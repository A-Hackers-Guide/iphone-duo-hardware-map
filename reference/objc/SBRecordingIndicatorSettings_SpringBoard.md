# `SBRecordingIndicatorSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 37 instance variables, 37 properties, 75 instance methods, 1 class methods

## Instance variables

```
B _requiresIntersensorRegion;
B _prefersCornerCircleAssociation;
B _rateLimitForceMicro;
B _usesSecureIndicatorLayer;
B _debugBackgroundColorEnabled;
B _debugHighLevelDotBorderEnabled;
B _useOverlappingCrossfade;
B _alwaysSuppressBacklightChanges;
B _observesProximityForBacklightChanges;
B _secureDisplayDeviceStatePollEnabled;
B _secureDisplayContinuousDeviceStatePoll;
B _secureDisplayAlwaysPowerAllDisplays;
q _sensorType;
d _cornerCircleRotationRateLimitPeriod;
Q _cornerCircleRotationRateLimitNumber;
Q _rateLimitForceMicroTolerance;
q _steadinessOverride;
d _delayBeforeFadeOut90;
d _fadeOutDuration90;
d _delayBeforeFadeIn90;
d _fadeInDuration90;
d _delayBeforeFadeOut180;
d _fadeOutDuration180;
d _delayBeforeFadeIn180;
d _fadeInDuration180;
d _delayBeforeFadeOut90WhenOverlapping;
d _fadeOutDuration90WhenOverlapping;
d _delayBeforeFadeIn90WhenOverlapping;
d _fadeInDuration90WhenOverlapping;
d _delayBeforeFadeOut180WhenOverlapping;
d _fadeOutDuration180WhenOverlapping;
d _delayBeforeFadeIn180WhenOverlapping;
d _fadeInDuration180WhenOverlapping;
d _rateLimitPeriod;
Q _rateLimitNumber;
d _secureDisplayPoseThrottleInterval;
d _secureDisplayDeviceStatePollInterval;
```

## Properties

```
@property (Tq,V_sensorType) sensorType;
@property (TB,V_requiresIntersensorRegion) requiresIntersensorRegion;
@property (TB,V_prefersCornerCircleAssociation) prefersCornerCircleAssociation;
@property (Td,V_cornerCircleRotationRateLimitPeriod) cornerCircleRotationRateLimitPeriod;
@property (TQ,V_cornerCircleRotationRateLimitNumber) cornerCircleRotationRateLimitNumber;
@property (TB,V_rateLimitForceMicro) rateLimitForceMicro;
@property (TQ,V_rateLimitForceMicroTolerance) rateLimitForceMicroTolerance;
@property (TB,V_usesSecureIndicatorLayer) usesSecureIndicatorLayer;
@property (Tq,V_steadinessOverride) steadinessOverride;
@property (TB,V_debugBackgroundColorEnabled) debugBackgroundColorEnabled;
@property (TB,V_debugHighLevelDotBorderEnabled) debugHighLevelDotBorderEnabled;
@property (Td,V_delayBeforeFadeOut90) delayBeforeFadeOut90;
@property (Td,V_fadeOutDuration90) fadeOutDuration90;
@property (Td,V_delayBeforeFadeIn90) delayBeforeFadeIn90;
@property (Td,V_fadeInDuration90) fadeInDuration90;
@property (Td,V_delayBeforeFadeOut180) delayBeforeFadeOut180;
@property (Td,V_fadeOutDuration180) fadeOutDuration180;
@property (Td,V_delayBeforeFadeIn180) delayBeforeFadeIn180;
@property (Td,V_fadeInDuration180) fadeInDuration180;
@property (TB,V_useOverlappingCrossfade) useOverlappingCrossfade;
@property (Td,V_delayBeforeFadeOut90WhenOverlapping) delayBeforeFadeOut90WhenOverlapping;
@property (Td,V_fadeOutDuration90WhenOverlapping) fadeOutDuration90WhenOverlapping;
@property (Td,V_delayBeforeFadeIn90WhenOverlapping) delayBeforeFadeIn90WhenOverlapping;
@property (Td,V_fadeInDuration90WhenOverlapping) fadeInDuration90WhenOverlapping;
@property (Td,V_delayBeforeFadeOut180WhenOverlapping) delayBeforeFadeOut180WhenOverlapping;
@property (Td,V_fadeOutDuration180WhenOverlapping) fadeOutDuration180WhenOverlapping;
@property (Td,V_delayBeforeFadeIn180WhenOverlapping) delayBeforeFadeIn180WhenOverlapping;
@property (Td,V_fadeInDuration180WhenOverlapping) fadeInDuration180WhenOverlapping;
@property (Td,V_rateLimitPeriod) rateLimitPeriod;
@property (TQ,V_rateLimitNumber) rateLimitNumber;
@property (TB,V_alwaysSuppressBacklightChanges) alwaysSuppressBacklightChanges;
@property (TB,V_observesProximityForBacklightChanges) observesProximityForBacklightChanges;
@property (Td,V_secureDisplayPoseThrottleInterval) secureDisplayPoseThrottleInterval;
@property (TB,V_secureDisplayDeviceStatePollEnabled) secureDisplayDeviceStatePollEnabled;
@property (TB,V_secureDisplayContinuousDeviceStatePoll) secureDisplayContinuousDeviceStatePoll;
@property (Td,V_secureDisplayDeviceStatePollInterval) secureDisplayDeviceStatePollInterval;
@property (TB,V_secureDisplayAlwaysPowerAllDisplays) secureDisplayAlwaysPowerAllDisplays;
```

## Class methods

```
+[SBRecordingIndicatorSettings settingsControllerModule];
```

## Instance methods

```
-[SBRecordingIndicatorSettings setFadeOutDuration180:];
-[SBRecordingIndicatorSettings alwaysSuppressBacklightChanges];
-[SBRecordingIndicatorSettings useOverlappingCrossfade];
-[SBRecordingIndicatorSettings setFadeInDuration90WhenOverlapping:];
-[SBRecordingIndicatorSettings setUsesSecureIndicatorLayer:];
-[SBRecordingIndicatorSettings sensorType];
-[SBRecordingIndicatorSettings debugBackgroundColorEnabled];
-[SBRecordingIndicatorSettings setPrefersCornerCircleAssociation:];
-[SBRecordingIndicatorSettings setObservesProximityForBacklightChanges:];
-[SBRecordingIndicatorSettings delayBeforeFadeIn180];
-[SBRecordingIndicatorSettings fadeInDuration90];
-[SBRecordingIndicatorSettings setRateLimitForceMicroTolerance:];
-[SBRecordingIndicatorSettings setSecureDisplayDeviceStatePollInterval:];
-[SBRecordingIndicatorSettings setFadeInDuration180:];
-[SBRecordingIndicatorSettings setAlwaysSuppressBacklightChanges:];
-[SBRecordingIndicatorSettings steadinessOverride];
-[SBRecordingIndicatorSettings fadeInDuration180WhenOverlapping];
-[SBRecordingIndicatorSettings rateLimitNumber];
-[SBRecordingIndicatorSettings rateLimitForceMicro];
-[SBRecordingIndicatorSettings fadeOutDuration180];
-[SBRecordingIndicatorSettings setRateLimitPeriod:];
-[SBRecordingIndicatorSettings setFadeInDuration90:];
-[SBRecordingIndicatorSettings secureDisplayDeviceStatePollInterval];
-[SBRecordingIndicatorSettings setRateLimitNumber:];
-[SBRecordingIndicatorSettings setDebugHighLevelDotBorderEnabled:];
-[SBRecordingIndicatorSettings setFadeOutDuration180WhenOverlapping:];
-[SBRecordingIndicatorSettings fadeInDuration90WhenOverlapping];
-[SBRecordingIndicatorSettings fadeInDuration180];
-[SBRecordingIndicatorSettings fadeOutDuration90];
-[SBRecordingIndicatorSettings setUseOverlappingCrossfade:];
-[SBRecordingIndicatorSettings delayBeforeFadeIn180WhenOverlapping];
-[SBRecordingIndicatorSettings setDefaultValues];
-[SBRecordingIndicatorSettings secureDisplayPoseThrottleInterval];
-[SBRecordingIndicatorSettings setDelayBeforeFadeIn90WhenOverlapping:];
-[SBRecordingIndicatorSettings debugHighLevelDotBorderEnabled];
-[SBRecordingIndicatorSettings setSecureDisplayPoseThrottleInterval:];
-[SBRecordingIndicatorSettings setCornerCircleRotationRateLimitNumber:];
-[SBRecordingIndicatorSettings delayBeforeFadeOut180WhenOverlapping];
-[SBRecordingIndicatorSettings setDelayBeforeFadeOut90:];
-[SBRecordingIndicatorSettings requiresIntersensorRegion];
-[SBRecordingIndicatorSettings delayBeforeFadeIn90WhenOverlapping];
-[SBRecordingIndicatorSettings setDelayBeforeFadeOut90WhenOverlapping:];
-[SBRecordingIndicatorSettings setFadeOutDuration90WhenOverlapping:];
-[SBRecordingIndicatorSettings rateLimitForceMicroTolerance];
-[SBRecordingIndicatorSettings setCornerCircleRotationRateLimitPeriod:];
-[SBRecordingIndicatorSettings fadeOutDuration180WhenOverlapping];
-[SBRecordingIndicatorSettings secureDisplayDeviceStatePollEnabled];
-[SBRecordingIndicatorSettings setDelayBeforeFadeOut180WhenOverlapping:];
-[SBRecordingIndicatorSettings rateLimitPeriod];
-[SBRecordingIndicatorSettings cornerCircleRotationRateLimitNumber];
-[SBRecordingIndicatorSettings setRateLimitForceMicro:];
-[SBRecordingIndicatorSettings setDelayBeforeFadeOut180:];
-[SBRecordingIndicatorSettings delayBeforeFadeOut180];
-[SBRecordingIndicatorSettings delayBeforeFadeIn90];
-[SBRecordingIndicatorSettings secureDisplayAlwaysPowerAllDisplays];
-[SBRecordingIndicatorSettings setDelayBeforeFadeIn90:];
-[SBRecordingIndicatorSettings setSecureDisplayContinuousDeviceStatePoll:];
-[SBRecordingIndicatorSettings setSensorType:];
-[SBRecordingIndicatorSettings setSecureDisplayDeviceStatePollEnabled:];
-[SBRecordingIndicatorSettings setFadeOutDuration90:];
-[SBRecordingIndicatorSettings delayBeforeFadeOut90];
-[SBRecordingIndicatorSettings setDebugBackgroundColorEnabled:];
-[SBRecordingIndicatorSettings setRequiresIntersensorRegion:];
-[SBRecordingIndicatorSettings fadeOutDuration90WhenOverlapping];
-[SBRecordingIndicatorSettings setSecureDisplayAlwaysPowerAllDisplays:];
-[SBRecordingIndicatorSettings setFadeInDuration180WhenOverlapping:];
-[SBRecordingIndicatorSettings observesProximityForBacklightChanges];
-[SBRecordingIndicatorSettings setDelayBeforeFadeIn180:];
-[SBRecordingIndicatorSettings secureDisplayContinuousDeviceStatePoll];
-[SBRecordingIndicatorSettings cornerCircleRotationRateLimitPeriod];
-[SBRecordingIndicatorSettings setSteadinessOverride:];
-[SBRecordingIndicatorSettings setDelayBeforeFadeIn180WhenOverlapping:];
-[SBRecordingIndicatorSettings prefersCornerCircleAssociation];
-[SBRecordingIndicatorSettings usesSecureIndicatorLayer];
-[SBRecordingIndicatorSettings delayBeforeFadeOut90WhenOverlapping];
```
