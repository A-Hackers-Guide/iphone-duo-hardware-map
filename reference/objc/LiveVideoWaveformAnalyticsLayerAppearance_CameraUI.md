# `LiveVideoWaveformAnalyticsLayerAppearance`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 13 instance methods, 6 class methods

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
+[LiveVideoWaveformAnalyticsLayerAppearance _getLuminanceFillColors];
+[LiveVideoWaveformAnalyticsLayerAppearance _getRGBFillColors];
+[LiveVideoWaveformAnalyticsLayerAppearance _matrixFromDefault:disablingChannels:];
+[LiveVideoWaveformAnalyticsLayerAppearance defaultLuminanceAppearance];
+[LiveVideoWaveformAnalyticsLayerAppearance defaultRGBCompositeAppearance];
+[LiveVideoWaveformAnalyticsLayerAppearance defaultRGBParadeAppearance];
```

## Instance methods

```
-[LiveVideoWaveformAnalyticsLayerAppearance smoothness];
-[LiveVideoWaveformAnalyticsLayerAppearance setSmoothness:];
-[LiveVideoWaveformAnalyticsLayerAppearance init];
-[LiveVideoWaveformAnalyticsLayerAppearance copyWithZone:];
-[LiveVideoWaveformAnalyticsLayerAppearance channelBlendMode];
-[LiveVideoWaveformAnalyticsLayerAppearance channelFillColor];
-[LiveVideoWaveformAnalyticsLayerAppearance initWithSubstrateColor:channelFillColor:channelBlendMode:isParade:smoothness:];
-[LiveVideoWaveformAnalyticsLayerAppearance isParade];
-[LiveVideoWaveformAnalyticsLayerAppearance setChannelBlendMode:];
-[LiveVideoWaveformAnalyticsLayerAppearance setChannelFillColor:];
-[LiveVideoWaveformAnalyticsLayerAppearance setIsParade:];
-[LiveVideoWaveformAnalyticsLayerAppearance setSubstrateColor:];
-[LiveVideoWaveformAnalyticsLayerAppearance substrateColor];
```
