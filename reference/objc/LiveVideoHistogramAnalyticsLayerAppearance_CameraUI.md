# `LiveVideoHistogramAnalyticsLayerAppearance`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
+[LiveVideoHistogramAnalyticsLayerAppearance _getLuminanceMatricesWithLineColors:fillStartColors:fillEndColors:];
+[LiveVideoHistogramAnalyticsLayerAppearance _getRGBMatricesWithLineColors:fillStartColors:fillEndColors:];
+[LiveVideoHistogramAnalyticsLayerAppearance _matrixFromDefault:disablingChannels:];
+[LiveVideoHistogramAnalyticsLayerAppearance defaultLuminanceAppearance];
+[LiveVideoHistogramAnalyticsLayerAppearance defaultRGBCompositeAppearance];
+[LiveVideoHistogramAnalyticsLayerAppearance defaultRGBParadeAppearance];
```

## Instance methods

```
-[LiveVideoHistogramAnalyticsLayerAppearance smoothness];
-[LiveVideoHistogramAnalyticsLayerAppearance setSmoothness:];
-[LiveVideoHistogramAnalyticsLayerAppearance init];
-[LiveVideoHistogramAnalyticsLayerAppearance copyWithZone:];
-[LiveVideoHistogramAnalyticsLayerAppearance numberOfBars];
-[LiveVideoHistogramAnalyticsLayerAppearance setNumberOfBars:];
-[LiveVideoHistogramAnalyticsLayerAppearance channelBlendMode];
-[LiveVideoHistogramAnalyticsLayerAppearance channelFillColorEnd];
-[LiveVideoHistogramAnalyticsLayerAppearance channelFillColorStart];
-[LiveVideoHistogramAnalyticsLayerAppearance channelFillGradientAngle];
-[LiveVideoHistogramAnalyticsLayerAppearance channelLineColor];
-[LiveVideoHistogramAnalyticsLayerAppearance channelLineThickness];
-[LiveVideoHistogramAnalyticsLayerAppearance initWithSubstrateColor:channelFillColorStart:channelFillColorEnd:channelLineColor:channelFillGradientAngle:channelLineThickness:channelBlendMode:isParade:numberOfBars:smoothness:];
-[LiveVideoHistogramAnalyticsLayerAppearance isParade];
-[LiveVideoHistogramAnalyticsLayerAppearance setChannelBlendMode:];
-[LiveVideoHistogramAnalyticsLayerAppearance setChannelFillColorEnd:];
-[LiveVideoHistogramAnalyticsLayerAppearance setChannelFillColorStart:];
-[LiveVideoHistogramAnalyticsLayerAppearance setChannelFillGradientAngle:];
-[LiveVideoHistogramAnalyticsLayerAppearance setChannelLineColor:];
-[LiveVideoHistogramAnalyticsLayerAppearance setChannelLineThickness:];
-[LiveVideoHistogramAnalyticsLayerAppearance setIsParade:];
-[LiveVideoHistogramAnalyticsLayerAppearance setSubstrateColor:];
-[LiveVideoHistogramAnalyticsLayerAppearance substrateColor];
```
