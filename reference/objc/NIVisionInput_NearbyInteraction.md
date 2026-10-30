# `NIVisionInput`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _majorRelocalization;
B _minorRelocalization;
d _timestamp;
q _trackingState;
d _lightEstimate;
{?="columns"[4]} _devicePose;
```

## Properties

```
@property (Td,R,V_timestamp) timestamp;
@property (T{?=[4]},R,V_devicePose) devicePose;
@property (Tq,R,V_trackingState) trackingState;
@property (Td,R,V_lightEstimate) lightEstimate;
@property (TB,R,V_majorRelocalization) majorRelocalization;
@property (TB,R,V_minorRelocalization) minorRelocalization;
```

## Class methods

```
+[NIVisionInput supportsSecureCoding];
```

## Instance methods

```
-[NIVisionInput timestamp];
-[NIVisionInput encodeWithCoder:];
-[NIVisionInput hash];
-[NIVisionInput initWithCoder:];
-[NIVisionInput copyWithZone:];
-[NIVisionInput isEqual:];
-[NIVisionInput trackingState];
-[NIVisionInput devicePose];
-[NIVisionInput lightEstimate];
-[NIVisionInput initWithTimestamp:devicePose:trackingState:lightEstimate:majorRelocalization:minorRelocalization:];
-[NIVisionInput majorRelocalization];
-[NIVisionInput minorRelocalization];
-[NIVisionInput overrideTimestamp:];
```
