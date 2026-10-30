# `AVMetadataFaceIDReadinessObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _ready;
q _coachingStatus;
q _userEngagementStatus;
```

## Properties

```
@property (TB,R,GisReady) ready;
@property (Tq,R) coachingStatus;
@property (Tq,R) userEngagementStatus;
```

## Class methods

```
+[AVMetadataFaceIDReadinessObject faceIDReadinessObjectWithReady:coachingStatus:userEngagementStatus:input:time:];
```

## Instance methods

```
-[AVMetadataFaceIDReadinessObject isReady];
-[AVMetadataFaceIDReadinessObject description];
-[AVMetadataFaceIDReadinessObject copyWithZone:];
-[AVMetadataFaceIDReadinessObject coachingStatus];
-[AVMetadataFaceIDReadinessObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataFaceIDReadinessObject initWithReady:coachingStatus:userEngagementStatus:time:sourceCaptureInput:];
-[AVMetadataFaceIDReadinessObject userEngagementStatus];
```
