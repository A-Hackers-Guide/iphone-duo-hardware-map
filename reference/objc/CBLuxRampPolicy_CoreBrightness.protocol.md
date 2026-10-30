# `CBLuxRampPolicy` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (Tf,R) rampUpDuration;
@property (Tf,R) rampDownDuration;
```

## Instance methods

```
-[CBLuxRampPolicy rampUpDuration];
-[CBLuxRampPolicy cappedRampStartLux:];
-[CBLuxRampPolicy cappedRampTargetLux:];
-[CBLuxRampPolicy rampDownDuration];
-[CBLuxRampPolicy rampDownLuxDeltaThresholdFor:];
-[CBLuxRampPolicy rampUpLuxDeltaThresholdFor:];
```
