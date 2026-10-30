# `CLSmootherBatchInputData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isFinalBatch;
B _shouldReconstructEntireRoute;
B _isWatch;
B _networkAccessAllowed;
B _clientCalledSmootherViaBatchSPI;
Q _schemaVersion;
@"NSUUID" _workoutSessionID;
Q _batchSequenceNumber;
Q _workoutActivityType;
@"NSArray" _intervals;
```

## Properties

```
@property (TQ,R,N,V_schemaVersion) schemaVersion;
@property (T@"NSUUID",R,N,V_workoutSessionID) workoutSessionID;
@property (TQ,R,N,V_batchSequenceNumber) batchSequenceNumber;
@property (TB,R,N,V_isFinalBatch) isFinalBatch;
@property (TQ,R,N,V_workoutActivityType) workoutActivityType;
@property (TB,R,N,V_shouldReconstructEntireRoute) shouldReconstructEntireRoute;
@property (TB,R,N,V_isWatch) isWatch;
@property (TB,R,N,V_networkAccessAllowed) networkAccessAllowed;
@property (TB,R,N,V_clientCalledSmootherViaBatchSPI) clientCalledSmootherViaBatchSPI;
@property (T@"NSArray",R,N,V_intervals) intervals;
```

## Class methods

```
+[CLSmootherBatchInputData supportsSecureCoding];
```

## Instance methods

```
-[CLSmootherBatchInputData isWatch];
-[CLSmootherBatchInputData dealloc];
-[CLSmootherBatchInputData schemaVersion];
-[CLSmootherBatchInputData workoutActivityType];
-[CLSmootherBatchInputData encodeWithCoder:];
-[CLSmootherBatchInputData initWithCoder:];
-[CLSmootherBatchInputData copyWithZone:];
-[CLSmootherBatchInputData networkAccessAllowed];
-[CLSmootherBatchInputData clientCalledSmootherViaBatchSPI];
-[CLSmootherBatchInputData batchSequenceNumber];
-[CLSmootherBatchInputData initWithWorkoutSessionID:batchSequenceNumber:isFinalBatch:workoutActivityType:shouldReconstructEntireRoute:isWatch:networkAccessAllowed:clientCalledSmootherViaBatchSPI:intervals:];
-[CLSmootherBatchInputData intervals];
-[CLSmootherBatchInputData isFinalBatch];
-[CLSmootherBatchInputData shouldReconstructEntireRoute];
-[CLSmootherBatchInputData workoutSessionID];
```
