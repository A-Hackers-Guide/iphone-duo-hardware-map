# `AVMetadataDeviceProximityDetectionObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
f _confidence;
{?="columns"[4]} _pose;
q _deviceType;
q _deviceID;
```

## Properties

```
@property (Tf,R,V_confidence) confidence;
@property (T{?=[4]},R,V_pose) pose;
@property (Tq,R,V_deviceType) deviceType;
@property (Tq,R,V_deviceID) deviceID;
```

## Class methods

```
+[AVMetadataDeviceProximityDetectionObject deviceProximityDetectionWithDeviceDictionary:input:time:];
```

## Instance methods

```
-[AVMetadataDeviceProximityDetectionObject deviceID];
-[AVMetadataDeviceProximityDetectionObject deviceType];
-[AVMetadataDeviceProximityDetectionObject description];
-[AVMetadataDeviceProximityDetectionObject copyWithZone:];
-[AVMetadataDeviceProximityDetectionObject confidence];
-[AVMetadataDeviceProximityDetectionObject pose];
-[AVMetadataDeviceProximityDetectionObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataDeviceProximityDetectionObject initWithDeviceDictionary:sourceCaptureInput:time:];
```
