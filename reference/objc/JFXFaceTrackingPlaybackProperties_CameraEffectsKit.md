# `JFXFaceTrackingPlaybackProperties`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _canTrackFace;
@"JFXFaceTrackedEffectTransform" _faceTrackingTransform;
@"JFXARMetadata" _arMetadata;
q _mediaInterfaceOrientationForDisplay;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _mediaTimeRange;
```

## Properties

```
@property (TB,R,N,V_canTrackFace) canTrackFace;
@property (T@"JFXFaceTrackedEffectTransform",R,N,V_faceTrackingTransform) faceTrackingTransform;
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_mediaTimeRange) mediaTimeRange;
@property (T@"JFXARMetadata",R,N,V_arMetadata) arMetadata;
@property (Tq,R,N,V_mediaInterfaceOrientationForDisplay) mediaInterfaceOrientationForDisplay;
```

## Instance methods

```
-[JFXFaceTrackingPlaybackProperties mediaTimeRange];
-[JFXFaceTrackingPlaybackProperties arMetadata];
-[JFXFaceTrackingPlaybackProperties canTrackFace];
-[JFXFaceTrackingPlaybackProperties containsMediaTime:forDisplayingMediaAtInterfaceOrientation:];
-[JFXFaceTrackingPlaybackProperties faceTrackingTransform];
-[JFXFaceTrackingPlaybackProperties initWithFaceTrackableMediaTimeRange:forDisplayingMediaAtInterfaceOrientation:faceTrackingTransform:arMetadata:];
-[JFXFaceTrackingPlaybackProperties initWithNonFaceTrackableMediaTimeRange:];
-[JFXFaceTrackingPlaybackProperties mediaInterfaceOrientationForDisplay];
```
