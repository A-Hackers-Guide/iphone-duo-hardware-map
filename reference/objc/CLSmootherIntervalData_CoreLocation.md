# `CLSmootherIntervalData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _is1HzData;
B _startsNewSegment;
B _isContinuationOfPriorBatch;
d _startTime;
d _endTime;
@"NSArray" _locationSamples;
@"NSArray" _odometrySamples;
@"NSArray" _altitudeSamples;
Q _workoutActivityType;
```

## Properties

```
@property (Td,R,N,V_startTime) startTime;
@property (Td,R,N,V_endTime) endTime;
@property (T@"NSArray",R,N,V_locationSamples) locationSamples;
@property (T@"NSArray",R,N,V_odometrySamples) odometrySamples;
@property (T@"NSArray",R,N,V_altitudeSamples) altitudeSamples;
@property (TB,R,N,V_is1HzData) is1HzData;
@property (TQ,R,N,V_workoutActivityType) workoutActivityType;
@property (TB,R,N,V_startsNewSegment) startsNewSegment;
@property (TB,R,N,V_isContinuationOfPriorBatch) isContinuationOfPriorBatch;
```

## Class methods

```
+[CLSmootherIntervalData supportsSecureCoding];
```

## Instance methods

```
-[CLSmootherIntervalData endTime];
-[CLSmootherIntervalData startTime];
-[CLSmootherIntervalData dealloc];
-[CLSmootherIntervalData workoutActivityType];
-[CLSmootherIntervalData encodeWithCoder:];
-[CLSmootherIntervalData initWithCoder:];
-[CLSmootherIntervalData copyWithZone:];
-[CLSmootherIntervalData locationSamples];
-[CLSmootherIntervalData odometrySamples];
-[CLSmootherIntervalData altitudeSamples];
-[CLSmootherIntervalData initWithStartTime:endTime:locationSamples:odometrySamples:altitudeSamples:is1HzData:workoutActivityType:startsNewSegment:isContinuationOfPriorBatch:];
-[CLSmootherIntervalData is1HzData];
-[CLSmootherIntervalData isContinuationOfPriorBatch];
-[CLSmootherIntervalData startsNewSegment];
```
