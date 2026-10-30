# `FigFaceObservation`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"VNFaceObservation" _faceObservation;
@"VNTrackObjectRequest" _faceTrackingRequest;
Q _faceID;
Q _lastUpdatedTime;
```

## Properties

```
@property (T@"VNFaceObservation",R,V_faceObservation) faceObservation;
@property (T@"VNTrackObjectRequest",R,V_faceTrackingRequest) faceTrackingRequest;
@property (TQ,R,V_faceID) faceID;
@property (TQ,V_lastUpdatedTime) lastUpdatedTime;
```

## Instance methods

```
-[FigFaceObservation dealloc];
-[FigFaceObservation setLastUpdatedTime:];
-[FigFaceObservation lastUpdatedTime];
-[FigFaceObservation faceID];
-[FigFaceObservation isEqual:];
-[FigFaceObservation faceObservation];
-[FigFaceObservation faceTrackingRequest];
-[FigFaceObservation initWithFaceObservation:faceID:time:];
```
