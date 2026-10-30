# `JFXOverlayEffectDebugViewOptions`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 46 instance methods, 1 class methods

## Instance variables

```
B _showDocumentBoundingBox;
B _showObjectAlignedBoundingBox;
B _showTextBoundingBoxes;
B _showHitAreaBoundingBox;
B _showFaceRect;
B _showTapPoints;
B _showMidpoint;
B _showCornerPoints;
B _showTextCornerPoints;
B _showHitAreaPoints;
B _showAdditionalRects;
@"UIColor" _documentBoundingBoxColor;
@"UIColor" _outputROIColor;
@"UIColor" _objectAlignedBoundingBoxColor;
@"NSArray" _textBoundingBoxColors;
@"UIColor" _hitAreaBoundingBoxColor;
@"UIColor" _midpointColor;
@"UIColor" _overlayCenterColor;
@"UIColor" _originCrosshairColor;
@"NSArray" _cornerPointColors;
@"NSArray" _textCornerPointColors;
@"NSArray" _hitAreaPointColors;
```

## Properties

```
@property (TB,N,V_showDocumentBoundingBox) showDocumentBoundingBox;
@property (TB,N,V_showObjectAlignedBoundingBox) showObjectAlignedBoundingBox;
@property (TB,N,V_showTextBoundingBoxes) showTextBoundingBoxes;
@property (TB,N,V_showHitAreaBoundingBox) showHitAreaBoundingBox;
@property (TB,N,V_showFaceRect) showFaceRect;
@property (TB,N,V_showTapPoints) showTapPoints;
@property (TB,N,V_showMidpoint) showMidpoint;
@property (TB,N,V_showCornerPoints) showCornerPoints;
@property (TB,N,V_showTextCornerPoints) showTextCornerPoints;
@property (TB,N,V_showHitAreaPoints) showHitAreaPoints;
@property (TB,N,V_showAdditionalRects) showAdditionalRects;
@property (T@"UIColor",&,N,V_documentBoundingBoxColor) documentBoundingBoxColor;
@property (T@"UIColor",&,N,V_outputROIColor) outputROIColor;
@property (T@"UIColor",&,N,V_objectAlignedBoundingBoxColor) objectAlignedBoundingBoxColor;
@property (T@"NSArray",&,N,V_textBoundingBoxColors) textBoundingBoxColors;
@property (T@"UIColor",&,N,V_hitAreaBoundingBoxColor) hitAreaBoundingBoxColor;
@property (T@"UIColor",&,N,V_midpointColor) midpointColor;
@property (T@"UIColor",&,N,V_overlayCenterColor) overlayCenterColor;
@property (T@"UIColor",&,N,V_originCrosshairColor) originCrosshairColor;
@property (T@"NSArray",&,N,V_cornerPointColors) cornerPointColors;
@property (T@"NSArray",&,N,V_textCornerPointColors) textCornerPointColors;
@property (T@"NSArray",&,N,V_hitAreaPointColors) hitAreaPointColors;
```

## Class methods

```
+[JFXOverlayEffectDebugViewOptions debugViewOptionsWithDictionary:];
```

## Instance methods

```
-[JFXOverlayEffectDebugViewOptions init];
-[JFXOverlayEffectDebugViewOptions description];
-[JFXOverlayEffectDebugViewOptions midpointColor];
-[JFXOverlayEffectDebugViewOptions cornerPointColors];
-[JFXOverlayEffectDebugViewOptions documentBoundingBoxColor];
-[JFXOverlayEffectDebugViewOptions hitAreaBoundingBoxColor];
-[JFXOverlayEffectDebugViewOptions hitAreaPointColors];
-[JFXOverlayEffectDebugViewOptions objectAlignedBoundingBoxColor];
-[JFXOverlayEffectDebugViewOptions originCrosshairColor];
-[JFXOverlayEffectDebugViewOptions outputROIColor];
-[JFXOverlayEffectDebugViewOptions overlayCenterColor];
-[JFXOverlayEffectDebugViewOptions setCornerPointColors:];
-[JFXOverlayEffectDebugViewOptions setDocumentBoundingBoxColor:];
-[JFXOverlayEffectDebugViewOptions setHitAreaBoundingBoxColor:];
-[JFXOverlayEffectDebugViewOptions setHitAreaPointColors:];
-[JFXOverlayEffectDebugViewOptions setMidpointColor:];
-[JFXOverlayEffectDebugViewOptions setObjectAlignedBoundingBoxColor:];
-[JFXOverlayEffectDebugViewOptions setOriginCrosshairColor:];
-[JFXOverlayEffectDebugViewOptions setOutputROIColor:];
-[JFXOverlayEffectDebugViewOptions setOverlayCenterColor:];
-[JFXOverlayEffectDebugViewOptions setShowAdditionalRects:];
-[JFXOverlayEffectDebugViewOptions setShowCornerPoints:];
-[JFXOverlayEffectDebugViewOptions setShowDocumentBoundingBox:];
-[JFXOverlayEffectDebugViewOptions setShowFaceRect:];
-[JFXOverlayEffectDebugViewOptions setShowHitAreaBoundingBox:];
-[JFXOverlayEffectDebugViewOptions setShowHitAreaPoints:];
-[JFXOverlayEffectDebugViewOptions setShowMidpoint:];
-[JFXOverlayEffectDebugViewOptions setShowObjectAlignedBoundingBox:];
-[JFXOverlayEffectDebugViewOptions setShowTapPoints:];
-[JFXOverlayEffectDebugViewOptions setShowTextBoundingBoxes:];
-[JFXOverlayEffectDebugViewOptions setShowTextCornerPoints:];
-[JFXOverlayEffectDebugViewOptions setTextBoundingBoxColors:];
-[JFXOverlayEffectDebugViewOptions setTextCornerPointColors:];
-[JFXOverlayEffectDebugViewOptions showAdditionalRects];
-[JFXOverlayEffectDebugViewOptions showCornerPoints];
-[JFXOverlayEffectDebugViewOptions showDocumentBoundingBox];
-[JFXOverlayEffectDebugViewOptions showFaceRect];
-[JFXOverlayEffectDebugViewOptions showHitAreaBoundingBox];
-[JFXOverlayEffectDebugViewOptions showHitAreaPoints];
-[JFXOverlayEffectDebugViewOptions showMidpoint];
-[JFXOverlayEffectDebugViewOptions showObjectAlignedBoundingBox];
-[JFXOverlayEffectDebugViewOptions showTapPoints];
-[JFXOverlayEffectDebugViewOptions showTextBoundingBoxes];
-[JFXOverlayEffectDebugViewOptions showTextCornerPoints];
-[JFXOverlayEffectDebugViewOptions textBoundingBoxColors];
-[JFXOverlayEffectDebugViewOptions textCornerPointColors];
```
