# `FigHumanBodyObservation`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"VNHumanObservation" _humanObservation;
@"VNTrackObjectRequest" _humanTrackingRequest;
Q _humanBodyID;
Q _lastUpdatedTime;
```

## Properties

```
@property (T@"VNHumanObservation",R,V_humanObservation) humanObservation;
@property (T@"VNTrackObjectRequest",R,V_humanTrackingRequest) humanTrackingRequest;
@property (TQ,R,V_humanBodyID) humanBodyID;
@property (TQ,R,V_lastUpdatedTime) lastUpdatedTime;
```

## Instance methods

```
-[FigHumanBodyObservation dealloc];
-[FigHumanBodyObservation lastUpdatedTime];
-[FigHumanBodyObservation isEqual:];
-[FigHumanBodyObservation humanBodyID];
-[FigHumanBodyObservation humanObservation];
-[FigHumanBodyObservation humanTrackingRequest];
-[FigHumanBodyObservation initWithHumanObservation:humanBodyID:time:];
```
