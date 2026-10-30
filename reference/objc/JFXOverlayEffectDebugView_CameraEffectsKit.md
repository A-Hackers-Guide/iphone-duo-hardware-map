# `JFXOverlayEffectDebugView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 19 instance variables, 19 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"UIView" _rootContainerView;
@"CALayer" _rootLayer;
@"CATransformLayer" _rootTransformLayer;
@"CAShapeLayer" _documentBoundingBoxLayer;
@"CAShapeLayer" _outputROILayer;
@"CAShapeLayer" _objectAlignedBoundingBoxLayer;
@"CALayer" _textBoundingBoxesContainerLayer;
@"CAShapeLayer" _hitAreaBoundingBoxLayer;
@"CAShapeLayer" _hitAreaMinimumSizeBoundingBoxLayer;
@"CAShapeLayer" _midpointLayer;
@"CAShapeLayer" _overlayCenterLayer;
@"CAShapeLayer" _originCrosshairLayer;
@"CAShapeLayer" _cornerPointsLayer;
@"CALayer" _textCornerPointsContainerLayer;
@"CAShapeLayer" _hitAreaPointsLayer;
@"CAShapeLayer" _additionalRectsLayer;
@"CAShapeLayer" _additionalRectsTransformedLayer;
@"JFXOverlayEffectDebugViewOptions" _options;
@"<JFXOverlayEffectDebugViewDelegate>" _delegate;
```

## Properties

```
@property (T@"UIView",&,N,V_rootContainerView) rootContainerView;
@property (T@"CALayer",&,N,V_rootLayer) rootLayer;
@property (T@"CATransformLayer",&,N,V_rootTransformLayer) rootTransformLayer;
@property (T@"CAShapeLayer",&,N,V_documentBoundingBoxLayer) documentBoundingBoxLayer;
@property (T@"CAShapeLayer",&,N,V_outputROILayer) outputROILayer;
@property (T@"CAShapeLayer",&,N,V_objectAlignedBoundingBoxLayer) objectAlignedBoundingBoxLayer;
@property (T@"CALayer",&,N,V_textBoundingBoxesContainerLayer) textBoundingBoxesContainerLayer;
@property (T@"CAShapeLayer",&,N,V_hitAreaBoundingBoxLayer) hitAreaBoundingBoxLayer;
@property (T@"CAShapeLayer",&,N,V_hitAreaMinimumSizeBoundingBoxLayer) hitAreaMinimumSizeBoundingBoxLayer;
@property (T@"CAShapeLayer",&,N,V_midpointLayer) midpointLayer;
@property (T@"CAShapeLayer",&,N,V_overlayCenterLayer) overlayCenterLayer;
@property (T@"CAShapeLayer",&,N,V_originCrosshairLayer) originCrosshairLayer;
@property (T@"CAShapeLayer",&,N,V_cornerPointsLayer) cornerPointsLayer;
@property (T@"CALayer",&,N,V_textCornerPointsContainerLayer) textCornerPointsContainerLayer;
@property (T@"CAShapeLayer",&,N,V_hitAreaPointsLayer) hitAreaPointsLayer;
@property (T@"CAShapeLayer",&,N,V_additionalRectsLayer) additionalRectsLayer;
@property (T@"CAShapeLayer",&,N,V_additionalRectsTransformedLayer) additionalRectsTransformedLayer;
@property (T@"JFXOverlayEffectDebugViewOptions",&,N,V_options) options;
@property (T@"<JFXOverlayEffectDebugViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[JFXOverlayEffectDebugView setupViews];
-[JFXOverlayEffectDebugView setOptions:];
-[JFXOverlayEffectDebugView rootLayer];
-[JFXOverlayEffectDebugView setDelegate:];
-[JFXOverlayEffectDebugView delegate];
-[JFXOverlayEffectDebugView initWithCoder:];
-[JFXOverlayEffectDebugView options];
-[JFXOverlayEffectDebugView initWithFrame:delegate:];
-[JFXOverlayEffectDebugView setRootLayer:];
-[JFXOverlayEffectDebugView rootContainerView];
-[JFXOverlayEffectDebugView setRootContainerView:];
-[JFXOverlayEffectDebugView additionalRectsTransformedLayer];
-[JFXOverlayEffectDebugView textBoundingBoxesContainerLayer];
-[JFXOverlayEffectDebugView additionalRectsLayer];
-[JFXOverlayEffectDebugView additionalRectsToDraw];
-[JFXOverlayEffectDebugView cornerPointsLayer];
-[JFXOverlayEffectDebugView documentBoundingBoxLayer];
-[JFXOverlayEffectDebugView hitAreaBoundingBoxLayer];
-[JFXOverlayEffectDebugView hitAreaMinimumSizeBoundingBoxLayer];
-[JFXOverlayEffectDebugView hitAreaPointsLayer];
-[JFXOverlayEffectDebugView midpointLayer];
-[JFXOverlayEffectDebugView objectAlignedBoundingBoxLayer];
-[JFXOverlayEffectDebugView originCrosshairLayer];
-[JFXOverlayEffectDebugView outputROILayer];
-[JFXOverlayEffectDebugView overlayCenterLayer];
-[JFXOverlayEffectDebugView rootTransformLayer];
-[JFXOverlayEffectDebugView setAdditionalRectsLayer:];
-[JFXOverlayEffectDebugView setAdditionalRectsTransformedLayer:];
-[JFXOverlayEffectDebugView setCornerPointsLayer:];
-[JFXOverlayEffectDebugView setDocumentBoundingBoxLayer:];
-[JFXOverlayEffectDebugView setHitAreaBoundingBoxLayer:];
-[JFXOverlayEffectDebugView setHitAreaMinimumSizeBoundingBoxLayer:];
-[JFXOverlayEffectDebugView setHitAreaPointsLayer:];
-[JFXOverlayEffectDebugView setMidpointLayer:];
-[JFXOverlayEffectDebugView setObjectAlignedBoundingBoxLayer:];
-[JFXOverlayEffectDebugView setOriginCrosshairLayer:];
-[JFXOverlayEffectDebugView setOutputROILayer:];
-[JFXOverlayEffectDebugView setOverlayCenterLayer:];
-[JFXOverlayEffectDebugView setRootTransformLayer:];
-[JFXOverlayEffectDebugView setTextBoundingBoxesContainerLayer:];
-[JFXOverlayEffectDebugView setTextCornerPointsContainerLayer:];
-[JFXOverlayEffectDebugView textCornerPointsContainerLayer];
-[JFXOverlayEffectDebugView updateAdditionalRects:transformedLayer:effectScale:rects:];
-[JFXOverlayEffectDebugView updateBorderedLayer:borderRect:borderWidth:borderColor:];
-[JFXOverlayEffectDebugView updateCrosshairLayer:center:color:size:thickness:];
-[JFXOverlayEffectDebugView updateDottedBorderedLayer:borderRect:borderWidth:borderColor:borderPhase:borderDashPattern:];
-[JFXOverlayEffectDebugView updateFilledCircleLayer:center:radius:fillColor:];
-[JFXOverlayEffectDebugView updateFilledPolygonLayer:path:fillColor:];
-[JFXOverlayEffectDebugView updatePointsLayers:points:colors:size:];
-[JFXOverlayEffectDebugView updatePolygonLayer:points:borderWidth:borderColor:];
-[JFXOverlayEffectDebugView updateWithEffectFrame:];
```
