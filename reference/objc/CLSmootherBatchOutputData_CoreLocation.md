# `CLSmootherBatchOutputData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _isFinalBatch;
@"NSUUID" _workoutSessionID;
Q _batchSequenceNumber;
@"NSArray" _smoothedLocationSamples;
```

## Properties

```
@property (T@"NSUUID",R,N,V_workoutSessionID) workoutSessionID;
@property (TQ,R,N,V_batchSequenceNumber) batchSequenceNumber;
@property (TB,R,N,V_isFinalBatch) isFinalBatch;
@property (T@"NSArray",R,N,V_smoothedLocationSamples) smoothedLocationSamples;
```

## Class methods

```
+[CLSmootherBatchOutputData supportsSecureCoding];
```

## Instance methods

```
-[CLSmootherBatchOutputData dealloc];
-[CLSmootherBatchOutputData encodeWithCoder:];
-[CLSmootherBatchOutputData initWithCoder:];
-[CLSmootherBatchOutputData copyWithZone:];
-[CLSmootherBatchOutputData batchSequenceNumber];
-[CLSmootherBatchOutputData initWithWorkoutSessionID:batchSequenceNumber:isFinalBatch:smoothedLocationSamples:];
-[CLSmootherBatchOutputData isFinalBatch];
-[CLSmootherBatchOutputData smoothedLocationSamples];
-[CLSmootherBatchOutputData workoutSessionID];
```
