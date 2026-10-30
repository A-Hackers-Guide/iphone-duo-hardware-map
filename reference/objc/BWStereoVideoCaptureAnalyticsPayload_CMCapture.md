# `BWStereoVideoCaptureAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 7 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _videoOrientation;
i _cameraPosture;
B _stereoVideoCaptureEnabled;
i _stereoVideoCaptureStatus;
f _stereoVideoCaptureDuration;
f _percentageOfFramesWithAggressiveLuxLevel;
f _percentageOfFramesWithAggressiveFocusDistance;
```

## Properties

```
@property (TB,N,V_stereoVideoCaptureEnabled) stereoVideoCaptureEnabled;
@property (Ti,N,V_stereoVideoCaptureStatus) stereoVideoCaptureStatus;
@property (Tf,N,V_stereoVideoCaptureDuration) stereoVideoCaptureDuration;
@property (Tf,N,V_percentageOfFramesWithAggressiveLuxLevel) percentageOfFramesWithAggressiveLuxLevel;
@property (Tf,N,V_percentageOfFramesWithAggressiveFocusDistance) percentageOfFramesWithAggressiveFocusDistance;
@property (Ti,N,V_videoOrientation) videoOrientation;
@property (Ti,N,V_cameraPosture) cameraPosture;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWStereoVideoCaptureAnalyticsPayload eventDictionary];
-[BWStereoVideoCaptureAnalyticsPayload init];
-[BWStereoVideoCaptureAnalyticsPayload setStereoVideoCaptureEnabled:];
-[BWStereoVideoCaptureAnalyticsPayload videoOrientation];
-[BWStereoVideoCaptureAnalyticsPayload stereoVideoCaptureStatus];
-[BWStereoVideoCaptureAnalyticsPayload reset];
-[BWStereoVideoCaptureAnalyticsPayload cameraPosture];
-[BWStereoVideoCaptureAnalyticsPayload eventName];
-[BWStereoVideoCaptureAnalyticsPayload setStereoVideoCaptureStatus:];
-[BWStereoVideoCaptureAnalyticsPayload setVideoOrientation:];
-[BWStereoVideoCaptureAnalyticsPayload stereoVideoCaptureEnabled];
-[BWStereoVideoCaptureAnalyticsPayload setCameraPosture:];
-[BWStereoVideoCaptureAnalyticsPayload percentageOfFramesWithAggressiveFocusDistance];
-[BWStereoVideoCaptureAnalyticsPayload percentageOfFramesWithAggressiveLuxLevel];
-[BWStereoVideoCaptureAnalyticsPayload setPercentageOfFramesWithAggressiveFocusDistance:];
-[BWStereoVideoCaptureAnalyticsPayload setPercentageOfFramesWithAggressiveLuxLevel:];
-[BWStereoVideoCaptureAnalyticsPayload setStereoVideoCaptureDuration:];
-[BWStereoVideoCaptureAnalyticsPayload stereoVideoCaptureDuration];
```
