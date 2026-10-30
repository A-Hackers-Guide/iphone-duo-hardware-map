# `JFXAVMediaVideoTrackReaderSample`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXMediaVideoTrackReaderSample`
- 2 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _sampleBufferRef;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_sampleBufferRef) sampleBufferRef;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (T{?=qiIq},R,N) presentationTimeStamp;
@property (T{?={?=qiIq}{?=qiIq}},R,N) timeRange;
```

## Instance methods

```
-[JFXAVMediaVideoTrackReaderSample timeRange];
-[JFXAVMediaVideoTrackReaderSample dealloc];
-[JFXAVMediaVideoTrackReaderSample initWithSampleBuffer:];
-[JFXAVMediaVideoTrackReaderSample presentationTimeStamp];
-[JFXAVMediaVideoTrackReaderSample duration];
-[JFXAVMediaVideoTrackReaderSample sampleBufferRef];
-[JFXAVMediaVideoTrackReaderSample initWithSampleBuffer:duration:];
```
