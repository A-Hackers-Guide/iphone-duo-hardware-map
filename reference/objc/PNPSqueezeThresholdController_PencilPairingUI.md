# `PNPSqueezeThresholdController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 3 properties, 14 instance methods, 2 class methods

## Properties

```
@property (TB,N) autoCalibrationInProgress;
@property (TB,N) squeezeOnboardingModeEnabled;
@property (T@"NSNumber",&,N) squeezeThreshold;
```

## Class methods

```
+[PNPSqueezeThresholdController sharedController];
+[PNPSqueezeThresholdController defaultThreshold];
```

## Instance methods

```
-[PNPSqueezeThresholdController squeezeThreshold];
-[PNPSqueezeThresholdController startAutoCalibrationIfNecessary];
-[PNPSqueezeThresholdController autoCalibrationInProgress];
-[PNPSqueezeThresholdController disableAutoCalibrationIfNecessary];
-[PNPSqueezeThresholdController disableSqueezeOnboardingMode];
-[PNPSqueezeThresholdController initializeToDefaultThreshold];
-[PNPSqueezeThresholdController initializeToDefaultThresholdIfUninitialized];
-[PNPSqueezeThresholdController opaqueTouchSenderDescriptor];
-[PNPSqueezeThresholdController resetAutoCalibration];
-[PNPSqueezeThresholdController setAutoCalibrationInProgress:];
-[PNPSqueezeThresholdController setSqueezeOnboardingModeEnabled:];
-[PNPSqueezeThresholdController setSqueezeThreshold:];
-[PNPSqueezeThresholdController squeezeOnboardingModeEnabled];
-[PNPSqueezeThresholdController synchronizeSqueezeThresholdToBackboard];
```
