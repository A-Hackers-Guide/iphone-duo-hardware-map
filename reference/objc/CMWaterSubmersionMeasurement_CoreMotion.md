# `CMWaterSubmersionMeasurement`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _date;
@"NSMeasurement" _depth;
@"NSMeasurement" _pressure;
@"NSMeasurement" _surfacePressure;
q _submersionState;
```

## Properties

```
@property (T@"NSDate",R,N,V_date) date;
@property (T@"NSMeasurement",R,N,V_depth) depth;
@property (T@"NSMeasurement",R,N,V_pressure) pressure;
@property (T@"NSMeasurement",R,N,V_surfacePressure) surfacePressure;
@property (Tq,R,N,V_submersionState) submersionState;
```

## Class methods

```
+[CMWaterSubmersionMeasurement supportsSecureCoding];
```

## Instance methods

```
-[CMWaterSubmersionMeasurement depth];
-[CMWaterSubmersionMeasurement dealloc];
-[CMWaterSubmersionMeasurement date];
-[CMWaterSubmersionMeasurement pressure];
-[CMWaterSubmersionMeasurement encodeWithCoder:];
-[CMWaterSubmersionMeasurement description];
-[CMWaterSubmersionMeasurement initWithCoder:];
-[CMWaterSubmersionMeasurement copyWithZone:];
-[CMWaterSubmersionMeasurement submersionState];
-[CMWaterSubmersionMeasurement surfacePressure];
-[CMWaterSubmersionMeasurement initWithDepth:andPressure:andSurfacePressure:andState:andDate:];
```
