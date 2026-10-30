# `CAMPanoramaConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
i _ringBufferSize;
q _sampleBufferWidth;
q _sampleBufferHeight;
q _maxWidth;
@"NSDictionary" __maxWidthPerDevice;
{?="value"q"timescale"i"flags"I"epoch"q} _minimumFramerate;
{?="value"q"timescale"i"flags"I"epoch"q} _maximumFramerate;
```

## Properties

```
@property (T@"NSDictionary",&,N,V__maxWidthPerDevice) _maxWidthPerDevice;
@property (Tq,R,N,V_sampleBufferWidth) sampleBufferWidth;
@property (Tq,R,N,V_sampleBufferHeight) sampleBufferHeight;
@property (T{?=qiIq},R,N,V_minimumFramerate) minimumFramerate;
@property (T{?=qiIq},R,N,V_maximumFramerate) maximumFramerate;
@property (Ti,R,N,V_ringBufferSize) ringBufferSize;
@property (Tq,R,N,V_maxWidth) maxWidth;
```

## Class methods

```
+[CAMPanoramaConfiguration sharedInstance];
```

## Instance methods

```
-[CAMPanoramaConfiguration maxWidth];
-[CAMPanoramaConfiguration maximumFramerate];
-[CAMPanoramaConfiguration minimumFramerate];
-[CAMPanoramaConfiguration _maxWidthPerDevice];
-[CAMPanoramaConfiguration initWithACTConfiguration:];
-[CAMPanoramaConfiguration maxWidthForDevice:];
-[CAMPanoramaConfiguration ringBufferSize];
-[CAMPanoramaConfiguration sampleBufferHeight];
-[CAMPanoramaConfiguration sampleBufferWidth];
-[CAMPanoramaConfiguration set_maxWidthPerDevice:];
```
