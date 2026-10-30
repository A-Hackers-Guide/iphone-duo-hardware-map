# `NIDeviceCapabilities`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NIInternalDeviceCapability`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _supportsPreciseDistanceMeasurement;
B _supportsDirectionMeasurement;
B _supportsCameraAssistance;
B _supportsCoarseDistanceMeasurement;
B _supportsExtendedDistanceMeasurement;
B _supportsDLTDOAMeasurement;
B _supportsBluetoothChannelSounding;
```

## Properties

```
@property (TB,R,N,V_supportsCoarseDistanceMeasurement) supportsCoarseDistanceMeasurement;
@property (TB,R,N,V_supportsPreciseDistanceMeasurement) supportsPreciseDistanceMeasurement;
@property (TB,R,N,V_supportsDirectionMeasurement) supportsDirectionMeasurement;
@property (TB,R,N,V_supportsCameraAssistance) supportsCameraAssistance;
@property (TB,R,N,V_supportsExtendedDistanceMeasurement) supportsExtendedDistanceMeasurement;
@property (TB,R,N,V_supportsDLTDOAMeasurement) supportsDLTDOAMeasurement;
@property (TB,R,N,V_supportsBluetoothChannelSounding) supportsBluetoothChannelSounding;
```

## Class methods

```
+[NIDeviceCapabilities new];
```

## Instance methods

```
-[NIDeviceCapabilities init];
-[NIDeviceCapabilities initWithBitmap:];
-[NIDeviceCapabilities initWithFineRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:btcsSupport:];
-[NIDeviceCapabilities initWithFineRangingSupport:coarseRangingSupport:aoaSupport:extendedDistanceMeasurementSupport:syntheticApertureSupport:dltdoaSupport:btcsSupport:];
-[NIDeviceCapabilities supportsBluetoothChannelSounding];
-[NIDeviceCapabilities supportsCameraAssistance];
-[NIDeviceCapabilities supportsCoarseDistanceMeasurement];
-[NIDeviceCapabilities supportsDLTDOAMeasurement];
-[NIDeviceCapabilities supportsDirectionMeasurement];
-[NIDeviceCapabilities supportsExtendedDistanceMeasurement];
-[NIDeviceCapabilities supportsPreciseDistanceMeasurement];
-[NIDeviceCapabilities toBitmap];
```
