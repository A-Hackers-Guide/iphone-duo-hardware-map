# `CUIVectorGlyphLayer`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 26 properties, 53 instance methods, 33 class methods

## Instance variables

```
@"NSArray" _sublayers;
^{CGPath=} _clipPathFromSublayers;
B _alwaysPulses;
B _alwaysRotates;
B _alwaysBreathes;
B _isEraserLayer;
B _gradientAlignsToLayer;
B _isPassthrough;
B _supportsVariableDraw;
i _lineCap;
i _lineJoin;
@"NSString" _name;
Q _index;
@"NSArray" _tags;
Q _motionGroup;
d _opacity;
d _valueThreshold;
d _variableDrawOffset;
d _variableDrawLength;
@"CUIVectorGlyphLayerDrawAttachmentStore" _drawAttachments;
d _strokeWidth;
q _gradientType;
@"CUIVectorGlyphPath" _referencePath;
@"<CUIVectorGlyhLayerDelegate>" _delegate;
```

## Properties

```
@property (T@"<CUIVectorGlyhLayerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) needsWideGamut;
@property (TB,R,N,V_supportsVariableDraw) supportsVariableDraw;
@property (T@"NSString",R,&,N,V_name) name;
@property (TQ,R,N,V_index) index;
@property (T@"NSArray",R,&,N,V_tags) tags;
@property (TQ,R,N,V_motionGroup) motionGroup;
@property (TB,R,N,V_alwaysPulses) alwaysPulses;
@property (TB,R,N,V_alwaysRotates) alwaysRotates;
@property (TB,R,N,V_alwaysBreathes) alwaysBreathes;
@property (Td,R,N,V_opacity) opacity;
@property (Td,R,N,V_valueThreshold) valueThreshold;
@property (TB,R,N) participatesInVariableDraw;
@property (Td,R,N,V_variableDrawOffset) variableDrawOffset;
@property (Td,R,N,V_variableDrawLength) variableDrawLength;
@property (TB,R,N,V_isEraserLayer) isEraserLayer;
@property (T@"CUIVectorGlyphLayerDrawAttachmentStore",R,&,N,V_drawAttachments) drawAttachments;
@property (Td,R,N,V_strokeWidth) strokeWidth;
@property (Ti,R,N,V_lineCap) lineCap;
@property (Ti,R,N,V_lineJoin) lineJoin;
@property (Tq,R,N,V_gradientType) gradientType;
@property (TB,R,N,V_gradientAlignsToLayer) gradientAlignsToLayer;
@property (T@,R,&,N) referenceShape;
@property (T@"CUIVectorGlyphPath",R,&,N,V_referencePath) referencePath;
@property (T@"NSArray",R,&,N) sublayers;
@property (TB,R,N,V_isPassthrough) isPassthrough;
```

## Class methods

```
+[CUIVectorGlyphLayer createLayerGroupWithLayerTree:layerNames:shapes:delegate:];
+[CUIVectorGlyphLayer _subpathClipStrokeIndicesAtom];
+[CUIVectorGlyphLayer _lineCapFromStyle:];
+[CUIVectorGlyphLayer _alwaysRotatesAtom];
+[CUIVectorGlyphLayer _suffixForNamedStyleWithPrefix:styles:];
+[CUIVectorGlyphLayer _createPathFromStyle:subpaths:];
+[CUIVectorGlyphLayer _motionGroupAtom];
+[CUIVectorGlyphLayer _clearBehindAtom];
+[CUIVectorGlyphLayer _fillColorFromStyle:];
+[CUIVectorGlyphLayer _createShapeLayerWithLayerTreeNode:layerName:index:shapes:delegate:];
+[CUIVectorGlyphLayer _drawAttachmentsAtom];
+[CUIVectorGlyphLayer _classesContainRenderModeClass:];
+[CUIVectorGlyphLayer createLayerGroupWithLayerNames:delegate:];
+[CUIVectorGlyphLayer _gradientTypeAtom];
+[CUIVectorGlyphLayer createLayerGroupWithLayerTree:modePrefix:shapes:delegate:];
+[CUIVectorGlyphLayer _createLayerWithLayerTreeNode:layerName:index:subpaths:delegate:];
+[CUIVectorGlyphLayer _indexFromStyleSuffix:integer:];
+[CUIVectorGlyphLayer _alwaysPulsesAtom];
+[CUIVectorGlyphLayer _alwaysBreathesAtom];
+[CUIVectorGlyphLayer _createSimpleLayerWithLayerTreeNode:layerName:index:subpaths:delegate:];
+[CUIVectorGlyphLayer _strokeWidthFromStyle:];
+[CUIVectorGlyphLayer _lineJoinFromStyle:];
+[CUIVectorGlyphLayer _layerHierarchyStyleNames];
+[CUIVectorGlyphLayer _createTreeWithLayerTreeNode:modePrefix:layerName:index:subpaths:delegate:];
+[CUIVectorGlyphLayer _layerTagsAtom];
+[CUIVectorGlyphLayer _gradientSizeToLayerAtom];
+[CUIVectorGlyphLayer _variableDrawAtom];
+[CUIVectorGlyphLayer _strokeWidthForNode:];
+[CUIVectorGlyphLayer _strokeColorFromStyle:];
+[CUIVectorGlyphLayer _colorNameForRenderingStyle:];
+[CUIVectorGlyphLayer _fillActionAtom];
+[CUIVectorGlyphLayer _variableThresholdAtom];
+[CUIVectorGlyphLayer _subpathIndicesAtom];
```

## Instance methods

```
-[CUIVectorGlyphLayer _visibleCompoundShape:];
-[CUIVectorGlyphLayer _setAlwaysRotates:];
-[CUIVectorGlyphLayer _initWithName:index:shape:strokeWidth:attributes:style:delegate:];
-[CUIVectorGlyphLayer __initTreeWithName:index:sublayers:attributes:style:delegate:];
-[CUIVectorGlyphLayer anyLayerNeedsWideGamutColor];
-[CUIVectorGlyphLayer _setAlwaysPulses:];
-[CUIVectorGlyphLayer _anyLayerAlwaysRotates];
-[CUIVectorGlyphLayer drawInContext:scaleFactor:targetSize:variableMinValue:variableMaxValue:onFillColor:offFillColor:];
-[CUIVectorGlyphLayer supportsVariableDraw];
-[CUIVectorGlyphLayer isEraserLayer];
-[CUIVectorGlyphLayer debugDescriptionWithIndentLevel:];
-[CUIVectorGlyphLayer gradientAlignsToLayer];
-[CUIVectorGlyphLayer _setAllLayersAlwaysPulse:];
-[CUIVectorGlyphLayer lineCap];
-[CUIVectorGlyphLayer referencePath];
-[CUIVectorGlyphLayer drawAttachments];
-[CUIVectorGlyphLayer _setAllLayersAlwaysRotate:];
-[CUIVectorGlyphLayer alwaysPulses];
-[CUIVectorGlyphLayer _initWithName:index:sublayers:attributes:style:delegate:];
-[CUIVectorGlyphLayer alwaysRotates];
-[CUIVectorGlyphLayer createSublayerMaskUsingScaleFactor:targetSize:maskColor:];
-[CUIVectorGlyphLayer _anyLayerAlwaysPulses];
-[CUIVectorGlyphLayer __initGroupWithName:index:sublayers:attributes:style:passthrough:delegate:];
-[CUIVectorGlyphLayer gradientType];
-[CUIVectorGlyphLayer variableDrawOffset];
-[CUIVectorGlyphLayer isPassthrough];
-[CUIVectorGlyphLayer motionGroup];
-[CUIVectorGlyphLayer copyClipShapeWithStartProgress:endProgress:];
-[CUIVectorGlyphLayer lineJoin];
-[CUIVectorGlyphLayer alwaysBreathes];
-[CUIVectorGlyphLayer valueThreshold];
-[CUIVectorGlyphLayer variableDrawLength];
-[CUIVectorGlyphLayer _colorForVariableThreshold:variableMinValue:variableMaxValue:onFillColor:offFillColor:];
-[CUIVectorGlyphLayer referenceShape];
-[CUIVectorGlyphLayer shapeAtScale:];
-[CUIVectorGlyphLayer copyClipShape];
-[CUIVectorGlyphLayer participatesInVariableDraw];
-[CUIVectorGlyphLayer pathAtScale:];
-[CUIVectorGlyphLayer needsWideGamut];
-[CUIVectorGlyphLayer _readCSSAttributes:styleAttributes:];
-[CUIVectorGlyphLayer tags];
-[CUIVectorGlyphLayer sublayers];
-[CUIVectorGlyphLayer debugDescription];
-[CUIVectorGlyphLayer createImageUsingScaleFactor:targetSize:variableMinValue:variableMaxValue:onFillColor:offFillColor:];
-[CUIVectorGlyphLayer shape];
-[CUIVectorGlyphLayer strokeWidth];
-[CUIVectorGlyphLayer dealloc];
-[CUIVectorGlyphLayer index];
-[CUIVectorGlyphLayer opacity];
-[CUIVectorGlyphLayer setDelegate:];
-[CUIVectorGlyphLayer delegate];
-[CUIVectorGlyphLayer name];
-[CUIVectorGlyphLayer path];
```
