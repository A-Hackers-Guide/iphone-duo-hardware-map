# `NIDeviceCapability` (protocol)

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 6 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) supportsPreciseDistanceMeasurement;
@property (TB,R,N) supportsDirectionMeasurement;
@property (TB,R,N) supportsCameraAssistance;
@property (TB,R,N) supportsExtendedDistanceMeasurement;
@property (TB,R,N) supportsDLTDOAMeasurement;
@property (TB,R,N) supportsBluetoothChannelSounding;
```

## Instance methods

```
-[NIDeviceCapability supportsBluetoothChannelSounding];
-[NIDeviceCapability supportsCameraAssistance];
-[NIDeviceCapability supportsDLTDOAMeasurement];
-[NIDeviceCapability supportsDirectionMeasurement];
-[NIDeviceCapability supportsExtendedDistanceMeasurement];
-[NIDeviceCapability supportsPreciseDistanceMeasurement];
```
