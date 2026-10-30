# `SRWristDetection`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `SRSampling`, `NSCopying`
- 5 instance variables, 11 properties, 24 instance methods, 2 class methods

## Instance variables

```
B _onWrist;
q _wristLocation;
q _crownOrientation;
d _cfOnWristDate;
d _cfOffWristDate;
```

## Properties

```
@property (TB,V_onWrist) onWrist;
@property (Tq,V_wristLocation) wristLocation;
@property (Tq,V_crownOrientation) crownOrientation;
@property (Td,V_cfOnWristDate) cfOnWristDate;
@property (Td,V_cfOffWristDate) cfOffWristDate;
@property (T@"NSDate",R) onWristDate;
@property (T@"NSDate",R) offWristDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRWristDetection supportsSecureCoding];
+[SRWristDetection initialize];
```

## Instance methods

```
-[SRWristDetection encodeWithCoder:];
-[SRWristDetection description];
-[SRWristDetection initWithCoder:];
-[SRWristDetection copyWithZone:];
-[SRWristDetection isEqual:];
-[SRWristDetection binarySampleRepresentation];
-[SRWristDetection initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRWristDetection sr_dictionaryRepresentation];
-[SRWristDetection onWrist];
-[SRWristDetection _offWristDate];
-[SRWristDetection _onWristDate];
-[SRWristDetection cfOffWristDate];
-[SRWristDetection cfOnWristDate];
-[SRWristDetection crownOrientation];
-[SRWristDetection initWithCFOnWristDate:CFOffWristDate:onWrist:wristLocation:crownOrientation:];
-[SRWristDetection initWithOnWristDate:offWristDate:onWrist:wristLocation:crownOrientation:];
-[SRWristDetection offWristDate];
-[SRWristDetection onWristDate];
-[SRWristDetection setCfOffWristDate:];
-[SRWristDetection setCfOnWristDate:];
-[SRWristDetection setCrownOrientation:];
-[SRWristDetection setOnWrist:];
-[SRWristDetection setWristLocation:];
-[SRWristDetection wristLocation];
```
