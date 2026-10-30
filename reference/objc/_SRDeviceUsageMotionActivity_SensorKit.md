# `_SRDeviceUsageMotionActivity`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`
- 2 instance variables, 6 properties, 9 instance methods, 2 class methods

## Instance variables

```
q _motionActivityType;
d _duration;
```

## Properties

```
@property (Tq,V_motionActivityType) motionActivityType;
@property (Td,V_duration) duration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SRDeviceUsageMotionActivity supportsSecureCoding];
+[_SRDeviceUsageMotionActivity motionActivityWithActivityType:duration:];
```

## Instance methods

```
-[_SRDeviceUsageMotionActivity duration];
-[_SRDeviceUsageMotionActivity encodeWithCoder:];
-[_SRDeviceUsageMotionActivity description];
-[_SRDeviceUsageMotionActivity initWithCoder:];
-[_SRDeviceUsageMotionActivity setDuration:];
-[_SRDeviceUsageMotionActivity isEqual:];
-[_SRDeviceUsageMotionActivity sr_dictionaryRepresentation];
-[_SRDeviceUsageMotionActivity motionActivityType];
-[_SRDeviceUsageMotionActivity setMotionActivityType:];
```
