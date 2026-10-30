# `CFXFrame`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _pixelBuffer;
@"PVFrameSet" _pvFrameSet;
@"ARFrame" _arFrame;
{?="value"q"timescale"i"flags"I"epoch"q} _latency;
{?="value"q"timescale"i"flags"I"epoch"q} _timestamp;
{?="value"q"timescale"i"flags"I"epoch"q} _requestTime;
```

## Properties

```
@property (T@"PVFrameSet",&,N,V_pvFrameSet) pvFrameSet;
@property (T@"ARFrame",&,N,V_arFrame) arFrame;
@property (T{?=qiIq},N,V_latency) latency;
@property (T^{__CVBuffer=},N,V_pixelBuffer) pixelBuffer;
@property (T{?=qiIq},N,V_timestamp) timestamp;
@property (T{?=qiIq},N,V_requestTime) requestTime;
```

## Instance methods

```
-[CFXFrame setLatency:];
-[CFXFrame setRequestTime:];
-[CFXFrame pixelBuffer];
-[CFXFrame latency];
-[CFXFrame setTimestamp:];
-[CFXFrame requestTime];
-[CFXFrame dealloc];
-[CFXFrame timestamp];
-[CFXFrame encodeWithCoder:];
-[CFXFrame setPixelBuffer:];
-[CFXFrame isEqual:];
-[CFXFrame initWithPixelBuffer:timestamp:];
-[CFXFrame arFrame];
-[CFXFrame isEqualToFrame:];
-[CFXFrame initWithARFrame:];
-[CFXFrame initWithFrameSet:];
-[CFXFrame pvFrameSet];
-[CFXFrame setArFrame:];
-[CFXFrame setPvFrameSet:];
```
