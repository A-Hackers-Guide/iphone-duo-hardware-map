# `FigCaptureVideoPreviewSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkConfiguration`
- 14 instance variables, 14 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _depthDataDeliveryEnabled;
B _filterRenderingEnabled;
@"NSArray" _filters;
f _portraitLightingEffectStrength;
B _semanticStyleRenderingEnabled;
@"FigCaptureSemanticStyle" _semanticStyle;
B _primaryCaptureRectModificationEnabled;
d _primaryCaptureRectAspectRatio;
{CGPoint="x"d"y"d} _primaryCaptureRectCenter;
q _primaryCaptureRectUniqueID;
B _zoomPIPOverlayEnabled;
B _portraitAutoSuggestEnabled;
f _overCaptureGradientPercentInset;
q _primaryDisplayRegion;
```

## Properties

```
@property (TB,N,V_depthDataDeliveryEnabled) depthDataDeliveryEnabled;
@property (TB,N,V_filterRenderingEnabled) filterRenderingEnabled;
@property (T@"NSArray",C,N,V_filters) filters;
@property (Tf,N,V_portraitLightingEffectStrength) portraitLightingEffectStrength;
@property (TB,N,V_semanticStyleRenderingEnabled) semanticStyleRenderingEnabled;
@property (T@"FigCaptureSemanticStyle",&,N,V_semanticStyle) semanticStyle;
@property (TB,N,V_primaryCaptureRectModificationEnabled) primaryCaptureRectModificationEnabled;
@property (Td,N,V_primaryCaptureRectAspectRatio) primaryCaptureRectAspectRatio;
@property (T{CGPoint=dd},N,V_primaryCaptureRectCenter) primaryCaptureRectCenter;
@property (Tq,N,V_primaryCaptureRectUniqueID) primaryCaptureRectUniqueID;
@property (TB,N,V_zoomPIPOverlayEnabled) zoomPIPOverlayEnabled;
@property (TB,N,V_portraitAutoSuggestEnabled) portraitAutoSuggestEnabled;
@property (Tq,N,V_primaryDisplayRegion) primaryDisplayRegion;
@property (Tf,N,V_overCaptureGradientPercentInset) overCaptureGradientPercentInset;
```

## Instance methods

```
-[FigCaptureVideoPreviewSinkConfiguration portraitAutoSuggestEnabled];
-[FigCaptureVideoPreviewSinkConfiguration semanticStyleRenderingEnabled];
-[FigCaptureVideoPreviewSinkConfiguration setPrimaryCaptureRectCenter:];
-[FigCaptureVideoPreviewSinkConfiguration setOverCaptureGradientPercentInset:];
-[FigCaptureVideoPreviewSinkConfiguration overCaptureGradientPercentInset];
-[FigCaptureVideoPreviewSinkConfiguration primaryDisplayRegion];
-[FigCaptureVideoPreviewSinkConfiguration sinkType];
-[FigCaptureVideoPreviewSinkConfiguration primaryCaptureRectUniqueID];
-[FigCaptureVideoPreviewSinkConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureVideoPreviewSinkConfiguration setPrimaryDisplayRegion:];
-[FigCaptureVideoPreviewSinkConfiguration zoomPIPOverlayEnabled];
-[FigCaptureVideoPreviewSinkConfiguration primaryCaptureRectCenter];
-[FigCaptureVideoPreviewSinkConfiguration setSemanticStyle:];
-[FigCaptureVideoPreviewSinkConfiguration primaryCaptureRectAspectRatio];
-[FigCaptureVideoPreviewSinkConfiguration portraitLightingEffectStrength];
-[FigCaptureVideoPreviewSinkConfiguration primaryCaptureRectModificationEnabled];
-[FigCaptureVideoPreviewSinkConfiguration setSemanticStyleRenderingEnabled:];
-[FigCaptureVideoPreviewSinkConfiguration init];
-[FigCaptureVideoPreviewSinkConfiguration setPrimaryCaptureRectUniqueID:];
-[FigCaptureVideoPreviewSinkConfiguration setZoomPIPOverlayEnabled:];
-[FigCaptureVideoPreviewSinkConfiguration dealloc];
-[FigCaptureVideoPreviewSinkConfiguration setFilters:];
-[FigCaptureVideoPreviewSinkConfiguration filters];
-[FigCaptureVideoPreviewSinkConfiguration setPrimaryCaptureRectModificationEnabled:];
-[FigCaptureVideoPreviewSinkConfiguration semanticStyle];
-[FigCaptureVideoPreviewSinkConfiguration copyXPCEncoding];
-[FigCaptureVideoPreviewSinkConfiguration description];
-[FigCaptureVideoPreviewSinkConfiguration setFilterRenderingEnabled:];
-[FigCaptureVideoPreviewSinkConfiguration initWithXPCEncoding:];
-[FigCaptureVideoPreviewSinkConfiguration setPortraitLightingEffectStrength:];
-[FigCaptureVideoPreviewSinkConfiguration setDepthDataDeliveryEnabled:];
-[FigCaptureVideoPreviewSinkConfiguration copyWithZone:];
-[FigCaptureVideoPreviewSinkConfiguration isEqual:];
-[FigCaptureVideoPreviewSinkConfiguration depthDataDeliveryEnabled];
-[FigCaptureVideoPreviewSinkConfiguration setPortraitAutoSuggestEnabled:];
-[FigCaptureVideoPreviewSinkConfiguration setPrimaryCaptureRectAspectRatio:];
-[FigCaptureVideoPreviewSinkConfiguration filterRenderingEnabled];
```
