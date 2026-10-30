# `SBHardwareDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 6 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TB,D,N) hasSeenACaseLatchCoverOnce;
@property (TB,R,D,N) disableHomeButton;
@property (TB,R,D,N) disableProximitySensor;
@property (TB,R,D,N) disableHomeButtonDoublePress;
@property (Tq,D,N) homeButtonHapticType;
@property (TB,D,N) disableNaturalVolumeButtonOrientation;
```

## Instance methods

```
-[SBHardwareDefaults _bindAndRegisterDefaults];
-[SBHardwareDefaults _deviceRequiresNaturalVolumeButtonArrangement];
-[SBHardwareDefaults isNaturalVolumeButtonOrientationEnabled];
```
