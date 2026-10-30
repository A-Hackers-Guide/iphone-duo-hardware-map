# `SRPhotoplethysmogramSample`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _startDate;
q _nanosecondsSinceStart;
@"NSArray" _usage;
@"NSArray" _opticalSamples;
@"NSArray" _accelerometerSamples;
@"NSMeasurement" _temperature;
```

## Properties

```
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (Tq,R,N,V_nanosecondsSinceStart) nanosecondsSinceStart;
@property (T@"NSArray",R,C,N,V_usage) usage;
@property (T@"NSArray",R,C,N,V_opticalSamples) opticalSamples;
@property (T@"NSArray",R,C,N,V_accelerometerSamples) accelerometerSamples;
@property (T@"NSMeasurement",R,N,V_temperature) temperature;
```

## Class methods

```
+[SRPhotoplethysmogramSample supportsSecureCoding];
+[SRPhotoplethysmogramSample new];
```

## Instance methods

```
-[SRPhotoplethysmogramSample usage];
-[SRPhotoplethysmogramSample startDate];
-[SRPhotoplethysmogramSample init];
-[SRPhotoplethysmogramSample dealloc];
-[SRPhotoplethysmogramSample encodeWithCoder:];
-[SRPhotoplethysmogramSample hash];
-[SRPhotoplethysmogramSample description];
-[SRPhotoplethysmogramSample initWithCoder:];
-[SRPhotoplethysmogramSample copyWithZone:];
-[SRPhotoplethysmogramSample isEqual:];
-[SRPhotoplethysmogramSample temperature];
-[SRPhotoplethysmogramSample accelerometerSamples];
-[SRPhotoplethysmogramSample initWithHAPPGFrame:];
-[SRPhotoplethysmogramSample initWithStartDate:nsSinceStart:usage:opticalSamples:accelSamples:degrees:];
-[SRPhotoplethysmogramSample isEqualToPPGSample:];
-[SRPhotoplethysmogramSample nanosecondsSinceStart];
-[SRPhotoplethysmogramSample opticalSamples];
```
