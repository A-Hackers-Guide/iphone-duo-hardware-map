# `SRWristTemperatureSession`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `SRSampling`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 20 properties, 21 instance methods, 3 class methods

## Instance variables

```
@"HAWristTemperatureSession" _healthwristTemperatureSession;
@"NSData" _dataRepresentation;
```

## Properties

```
@property (Tf,R,N) a0CorrectionCoefficient;
@property (Tf,R,N) c0CorrectionCoefficient;
@property (Tf,R,N) c0UserDeviceCorrectionCoefficient;
@property (T@"NSMeasurement",R,N) meanQuiescentPower;
@property (T@"NSMeasurement",R,N) standardDeviationQuiescentPower;
@property (TB,R,N,GisPublishable) publishable;
@property (Tf,R,N) a0CorrectionCoefficient;
@property (Tf,R,N) c0CorrectionCoefficient;
@property (Tf,R,N) c0UserDeviceCorrectionCoefficient;
@property (T@"NSMeasurement",R,N) meanQuiescentPower;
@property (T@"NSMeasurement",R,N) standardDeviationQuiescentPower;
@property (TB,R,N,GisPublishable) publishable;
@property (T@"NSDate",R,N) startDate;
@property (Td,R,N) duration;
@property (T@"NSString",R,C,N) version;
@property (T@"NSEnumerator",R,C,N) temperatures;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRWristTemperatureSession supportsSecureCoding];
+[SRWristTemperatureSession initialize];
+[SRWristTemperatureSession new];
```

## Instance methods

```
-[SRWristTemperatureSession startDate];
-[SRWristTemperatureSession init];
-[SRWristTemperatureSession dealloc];
-[SRWristTemperatureSession version];
-[SRWristTemperatureSession duration];
-[SRWristTemperatureSession encodeWithCoder:];
-[SRWristTemperatureSession hash];
-[SRWristTemperatureSession description];
-[SRWristTemperatureSession initWithCoder:];
-[SRWristTemperatureSession initWithSession:];
-[SRWristTemperatureSession copyWithZone:];
-[SRWristTemperatureSession isEqual:];
-[SRWristTemperatureSession temperatures];
-[SRWristTemperatureSession initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRWristTemperatureSession sr_dictionaryRepresentation];
-[SRWristTemperatureSession standardDeviationQuiescentPower];
-[SRWristTemperatureSession a0CorrectionCoefficient];
-[SRWristTemperatureSession c0CorrectionCoefficient];
-[SRWristTemperatureSession c0UserDeviceCorrectionCoefficient];
-[SRWristTemperatureSession isPublishable];
-[SRWristTemperatureSession meanQuiescentPower];
```
