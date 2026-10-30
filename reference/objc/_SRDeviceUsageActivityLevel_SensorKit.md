# `_SRDeviceUsageActivityLevel`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`
- 2 instance variables, 6 properties, 9 instance methods, 2 class methods

## Instance variables

```
q _activityLevel;
d _duration;
```

## Properties

```
@property (Tq,V_activityLevel) activityLevel;
@property (Td,V_duration) duration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SRDeviceUsageActivityLevel supportsSecureCoding];
+[_SRDeviceUsageActivityLevel activityLevelWithLevel:duration:];
```

## Instance methods

```
-[_SRDeviceUsageActivityLevel duration];
-[_SRDeviceUsageActivityLevel encodeWithCoder:];
-[_SRDeviceUsageActivityLevel description];
-[_SRDeviceUsageActivityLevel initWithCoder:];
-[_SRDeviceUsageActivityLevel setDuration:];
-[_SRDeviceUsageActivityLevel isEqual:];
-[_SRDeviceUsageActivityLevel activityLevel];
-[_SRDeviceUsageActivityLevel sr_dictionaryRepresentation];
-[_SRDeviceUsageActivityLevel setActivityLevel:];
```
