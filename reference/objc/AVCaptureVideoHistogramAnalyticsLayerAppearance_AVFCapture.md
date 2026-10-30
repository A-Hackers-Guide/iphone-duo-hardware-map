# `AVCaptureVideoHistogramAnalyticsLayerAppearance`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 23 instance methods, 6 class methods

## Instance variables

```
B _isParade;
f _channelFillGradientAngle;
f _channelLineThickness;
i _channelBlendMode;
I _numberOfBars;
f _smoothness;
_substrateColor;
{?="columns"[4]} _channelFillColorStart;
{?="columns"[4]} _channelFillColorEnd;
{?="columns"[4]} _channelLineColor;
```

## Properties

```
@property (T,N,V_substrateColor) substrateColor;
@property (T{?=[4]},N,V_channelFillColorStart) channelFillColorStart;
@property (T{?=[4]},N,V_channelFillColorEnd) channelFillColorEnd;
@property (T{?=[4]},N,V_channelLineColor) channelLineColor;
@property (Tf,N,V_channelFillGradientAngle) channelFillGradientAngle;
@property (Tf,N,V_channelLineThickness) channelLineThickness;
@property (Ti,N,V_channelBlendMode) channelBlendMode;
@property (TB,N,V_isParade) isParade;
@property (TI,N,V_numberOfBars) numberOfBars;
@property (Tf,N,V_smoothness) smoothness;
```

## Class methods

```
+[AVCaptureVideoHistogramAnalyticsLayerAppearance _getLuminanceMatricesWithLineColors:fillStartColors:fillEndColors:];
+[AVCaptureVideoHistogramAnalyticsLayerAppearance _getRGBMatricesWithLineColors:fillStartColors:fillEndColors:];
+[AVCaptureVideoHistogramAnalyticsLayerAppearance _matrixFromDefault:disablingChannels:];
+[AVCaptureVideoHistogramAnalyticsLayerAppearance defaultLuminanceAppearance];
+[AVCaptureVideoHistogramAnalyticsLayerAppearance defaultRGBCompositeAppearance];
+[AVCaptureVideoHistogramAnalyticsLayerAppearance defaultRGBParadeAppearance];
```

## Instance methods

```
-[AVCaptureVideoHistogramAnalyticsLayerAppearance smoothness];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setSmoothness:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance init];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance copyWithZone:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance numberOfBars];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setNumberOfBars:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance channelBlendMode];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance channelFillColorEnd];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance channelFillColorStart];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance channelFillGradientAngle];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance channelLineColor];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance channelLineThickness];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance initWithSubstrateColor:channelFillColorStart:channelFillColorEnd:channelLineColor:channelFillGradientAngle:channelLineThickness:channelBlendMode:isParade:numberOfBars:smoothness:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance isParade];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelBlendMode:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelFillColorEnd:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelFillColorStart:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelFillGradientAngle:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelLineColor:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setChannelLineThickness:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setIsParade:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance setSubstrateColor:];
-[AVCaptureVideoHistogramAnalyticsLayerAppearance substrateColor];
```
