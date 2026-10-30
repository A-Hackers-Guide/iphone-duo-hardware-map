# `JFXAnimojiPlaybackPreprocessedData`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"ARFrame" _arFrame;
@"AVDepthData" _avDepthData;
@"NSDictionary" _animojiBlendShapes;
{?="value"q"timescale"i"flags"I"epoch"q} _time;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _mediaTimeRangeForData;
```

## Properties

```
@property (T{?=qiIq},R,N,V_time) time;
@property (T@"ARFrame",R,N,V_arFrame) arFrame;
@property (T@"AVDepthData",R,N,V_avDepthData) avDepthData;
@property (T@"NSDictionary",R,N,V_animojiBlendShapes) animojiBlendShapes;
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_mediaTimeRangeForData) mediaTimeRangeForData;
```

## Instance methods

```
-[JFXAnimojiPlaybackPreprocessedData time];
-[JFXAnimojiPlaybackPreprocessedData avDepthData];
-[JFXAnimojiPlaybackPreprocessedData arFrame];
-[JFXAnimojiPlaybackPreprocessedData animojiBlendShapes];
-[JFXAnimojiPlaybackPreprocessedData initForRenderTime:usingDataFromMediaTimeRange:arFrame:avDepthData:animojiBlendShapes:];
-[JFXAnimojiPlaybackPreprocessedData mediaTimeRangeForData];
```
