# `BWTrackedFace`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@ _trackingID;
f _trackingDistance;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trackingRect;
@ _detectionID;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _detectionRect;
f _sizeToDistanceMultiplier;
f _size;
f _distance;
```

## Properties

```
@property (T@,&,N,V_trackingID) trackingID;
@property (Tf,N) trackingDistance;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_trackingRect) trackingRect;
@property (T@,R,N,V_detectionID) detectionID;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) detectionRect;
@property (Tf,R,N,V_size) size;
@property (Tf,R,N,V_distance) distance;
```

## Instance methods

```
-[BWTrackedFace distance];
-[BWTrackedFace dealloc];
-[BWTrackedFace size];
-[BWTrackedFace trackingID];
-[BWTrackedFace detectionID];
-[BWTrackedFace detectionRect];
-[BWTrackedFace setDetectionRect:];
-[BWTrackedFace setTrackingDistance:];
-[BWTrackedFace setTrackingID:];
-[BWTrackedFace setTrackingRect:];
-[BWTrackedFace trackingDistance];
-[BWTrackedFace trackingRect];
```
