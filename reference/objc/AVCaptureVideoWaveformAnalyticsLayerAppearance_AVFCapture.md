# `AVCaptureVideoWaveformAnalyticsLayerAppearance`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 13 instance methods, 9 class methods

## Instance variables

```
B _isParade;
i _channelBlendMode;
f _smoothness;
_substrateColor;
{?="columns"[4]} _channelFillColor;
```

## Properties

```
@property (T,N,V_substrateColor) substrateColor;
@property (T{?=[4]},N,V_channelFillColor) channelFillColor;
@property (Ti,N,V_channelBlendMode) channelBlendMode;
@property (TB,N,V_isParade) isParade;
@property (Tf,N,V_smoothness) smoothness;
```

## Class methods

```
+[AVCaptureVideoWaveformAnalyticsLayerAppearance _getLuminanceFillColors];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance _getRGBFillColors];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance _getYUVFillColors];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance _matrixFromDefault:disablingChannels:];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultLuminanceAppearance];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultRGBCompositeAppearance];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultRGBParadeAppearance];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultYUVCompositeAppearance];
+[AVCaptureVideoWaveformAnalyticsLayerAppearance defaultYUVParadeAppearance];
```

## Instance methods

```
-[AVCaptureVideoWaveformAnalyticsLayerAppearance smoothness];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance setSmoothness:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance init];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance copyWithZone:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance channelBlendMode];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance channelFillColor];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance initWithSubstrateColor:channelFillColor:channelBlendMode:isParade:smoothness:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance isParade];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance setChannelBlendMode:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance setChannelFillColor:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance setIsParade:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance setSubstrateColor:];
-[AVCaptureVideoWaveformAnalyticsLayerAppearance substrateColor];
```
