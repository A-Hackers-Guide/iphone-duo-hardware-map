# `SRPhotoplethysmogramAccelerometerSample`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
d _rawFrequency;
d _rawX;
d _rawY;
d _rawZ;
q _nanosecondsSinceStart;
```

## Properties

```
@property (Tq,R,N,V_nanosecondsSinceStart) nanosecondsSinceStart;
@property (T@"NSMeasurement",R,N) samplingFrequency;
@property (T@"NSMeasurement",R,N) x;
@property (T@"NSMeasurement",R,N) y;
@property (T@"NSMeasurement",R,N) z;
```

## Class methods

```
+[SRPhotoplethysmogramAccelerometerSample supportsSecureCoding];
```

## Instance methods

```
-[SRPhotoplethysmogramAccelerometerSample y];
-[SRPhotoplethysmogramAccelerometerSample x];
-[SRPhotoplethysmogramAccelerometerSample encodeWithCoder:];
-[SRPhotoplethysmogramAccelerometerSample hash];
-[SRPhotoplethysmogramAccelerometerSample description];
-[SRPhotoplethysmogramAccelerometerSample initWithCoder:];
-[SRPhotoplethysmogramAccelerometerSample copyWithZone:];
-[SRPhotoplethysmogramAccelerometerSample isEqual:];
-[SRPhotoplethysmogramAccelerometerSample z];
-[SRPhotoplethysmogramAccelerometerSample samplingFrequency];
-[SRPhotoplethysmogramAccelerometerSample initWithHAPPGAccelSample:];
-[SRPhotoplethysmogramAccelerometerSample initWithTimestamp:frequency:x:y:z:];
-[SRPhotoplethysmogramAccelerometerSample isEqualToAccelSample:];
-[SRPhotoplethysmogramAccelerometerSample nanosecondsSinceStart];
```
