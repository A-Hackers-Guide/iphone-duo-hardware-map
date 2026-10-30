# `CAMVideoStabilizationCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
B __enabled;
B __frontRearSimultaneousVideoEnabled;
B __configureSecondaryDevice;
q __strength;
```

## Properties

```
@property (TB,R,N,G_isEnabled,V__enabled) _enabled;
@property (Tq,R,N,V__strength) _strength;
@property (TB,R,N,V__frontRearSimultaneousVideoEnabled) _frontRearSimultaneousVideoEnabled;
@property (TB,R,N,V__configureSecondaryDevice) _configureSecondaryDevice;
```

## Instance methods

```
-[CAMVideoStabilizationCommand _configureSecondaryDevice];
-[CAMVideoStabilizationCommand _isEnabled];
-[CAMVideoStabilizationCommand executeWithContext:];
-[CAMVideoStabilizationCommand copyWithZone:];
-[CAMVideoStabilizationCommand _frontRearSimultaneousVideoEnabled];
-[CAMVideoStabilizationCommand _strength];
-[CAMVideoStabilizationCommand initWithAutomaticVideoStabilizationEnabled:strength:frontRearSimultaneousVideoEnabled:configureSecondaryDevice:];
```
