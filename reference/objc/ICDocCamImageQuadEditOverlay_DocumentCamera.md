# `ICDocCamImageQuadEditOverlay`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `ICDocCamImageQuadEditPanGestureRecognizerDelegate`
- 23 instance variables, 32 properties, 69 instance methods, 0 class methods

## Instance variables

```
B _isTempOverlay;
B _tempOverlayQuadIsValid;
B _isDisplayingValidQuad;
@"<ICDocCamImageQuadEditOverlayDelegate>" _delegate;
@"ICDocCamImageQuad" _quad;
@"UIImage" _image;
q _orientation;
d _knobHeight;
@"UIColor" _knobColor;
@"NSArray" _knobs;
@"NSArray" _knobAccessibilityElements;
@"UIColor" _validRectColor;
@"UIColor" _invalidRectColor;
@"CALayer" _selectedKnob;
@"ICDocCamImageQuadEditPanGestureRecognizer" _panGR;
@"CALayer" _knobLayer;
@"CAShapeLayer" _outlineLayer;
@"CALayer" _loupeLayer;
@"CALayer" _loupeContentsLayer;
d _tempOverlayMagnification;
@"NSMutableArray" _panHistory;
Q _panHistoryIdx;
{CGPoint="x"d"y"d} _lastGestureTranslation;
```

## Properties

```
@property (T@"NSArray",&,N,V_knobs) knobs;
@property (T@"NSArray",C,N,V_knobAccessibilityElements) knobAccessibilityElements;
@property (T@"UIColor",R,N,V_validRectColor) validRectColor;
@property (T@"UIColor",R,N,V_invalidRectColor) invalidRectColor;
@property (TB,N,V_isDisplayingValidQuad) isDisplayingValidQuad;
@property (T@"CALayer",&,N,V_selectedKnob) selectedKnob;
@property (T@"ICDocCamImageQuadEditPanGestureRecognizer",&,N,V_panGR) panGR;
@property (T@"CALayer",&,N,V_knobLayer) knobLayer;
@property (T@"CAShapeLayer",&,N,V_outlineLayer) outlineLayer;
@property (T@"UIBezierPath",R,N) outlinePath;
@property (T@"UIImage",&,N,V_image) image;
@property (Tq,N,V_orientation) orientation;
@property (T@"CALayer",&,N,V_loupeLayer) loupeLayer;
@property (T@"CALayer",&,N,V_loupeContentsLayer) loupeContentsLayer;
@property (Td,N,V_tempOverlayMagnification) tempOverlayMagnification;
@property (Td,N,V_knobHeight) knobHeight;
@property (T@"UIColor",&,N,V_knobColor) knobColor;
@property (T{CGPoint=dd},N,V_lastGestureTranslation) lastGestureTranslation;
@property (T@"NSMutableArray",&,N,V_panHistory) panHistory;
@property (TQ,N,V_panHistoryIdx) panHistoryIdx;
@property (TB,N,V_isTempOverlay) isTempOverlay;
@property (TB,N,V_tempOverlayQuadIsValid) tempOverlayQuadIsValid;
@property (T@"<ICDocCamImageQuadEditOverlayDelegate>",W,N,V_delegate) delegate;
@property (T@"ICDocCamImageQuad",&,N,V_quad) quad;
@property (T@"ICDocCamImageQuad",R,N) adjustedQuad;
@property (TB,R,N) isDraggingKnob;
@property (TB,R,N) isQuadValid;
@property (TB,R,N) containsPointOutsideOfOverlayBounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamImageQuadEditOverlay commonInit];
-[ICDocCamImageQuadEditOverlay setOrientation:];
-[ICDocCamImageQuadEditOverlay accessibilityElements];
-[ICDocCamImageQuadEditOverlay accessibilityIgnoresInvertColors];
-[ICDocCamImageQuadEditOverlay orientation];
-[ICDocCamImageQuadEditOverlay layoutSubviews];
-[ICDocCamImageQuadEditOverlay setDelegate:];
-[ICDocCamImageQuadEditOverlay delegate];
-[ICDocCamImageQuadEditOverlay initWithCoder:];
-[ICDocCamImageQuadEditOverlay image];
-[ICDocCamImageQuadEditOverlay initWithFrame:];
-[ICDocCamImageQuadEditOverlay setImage:];
-[ICDocCamImageQuadEditOverlay outlinePath];
-[ICDocCamImageQuadEditOverlay knobColor];
-[ICDocCamImageQuadEditOverlay quad];
-[ICDocCamImageQuadEditOverlay setKnobColor:];
-[ICDocCamImageQuadEditOverlay setQuad:];
-[ICDocCamImageQuadEditOverlay didPan:];
-[ICDocCamImageQuadEditOverlay setImage:orientation:];
-[ICDocCamImageQuadEditOverlay outlineLayer];
-[ICDocCamImageQuadEditOverlay setOutlineLayer:];
-[ICDocCamImageQuadEditOverlay adjustedQuad];
-[ICDocCamImageQuadEditOverlay closestKnobToPoint:];
-[ICDocCamImageQuadEditOverlay containsPointOutsideOfOverlayBounds];
-[ICDocCamImageQuadEditOverlay invalidRectColor];
-[ICDocCamImageQuadEditOverlay isDisplayingValidQuad];
-[ICDocCamImageQuadEditOverlay isDraggingKnob];
-[ICDocCamImageQuadEditOverlay isQuadValid];
-[ICDocCamImageQuadEditOverlay isTempOverlay];
-[ICDocCamImageQuadEditOverlay knobAccessibilityElements];
-[ICDocCamImageQuadEditOverlay knobHeight];
-[ICDocCamImageQuadEditOverlay knobLayer];
-[ICDocCamImageQuadEditOverlay knobs];
-[ICDocCamImageQuadEditOverlay lastGestureTranslation];
-[ICDocCamImageQuadEditOverlay loupeContentsLayer];
-[ICDocCamImageQuadEditOverlay loupeLayer];
-[ICDocCamImageQuadEditOverlay panGR];
-[ICDocCamImageQuadEditOverlay panHistory];
-[ICDocCamImageQuadEditOverlay panHistoryIdx];
-[ICDocCamImageQuadEditOverlay rectFromApplyingOrientation:toContentsRect:];
-[ICDocCamImageQuadEditOverlay selectedKnob];
-[ICDocCamImageQuadEditOverlay setIsDisplayingValidQuad:];
-[ICDocCamImageQuadEditOverlay setIsTempOverlay:];
-[ICDocCamImageQuadEditOverlay setKnobAccessibilityElements:];
-[ICDocCamImageQuadEditOverlay setKnobHeight:];
-[ICDocCamImageQuadEditOverlay setKnobLayer:];
-[ICDocCamImageQuadEditOverlay setKnobs:];
-[ICDocCamImageQuadEditOverlay setLastGestureTranslation:];
-[ICDocCamImageQuadEditOverlay setLoupeContentsLayer:];
-[ICDocCamImageQuadEditOverlay setLoupeLayer:];
-[ICDocCamImageQuadEditOverlay setPanGR:];
-[ICDocCamImageQuadEditOverlay setPanHistory:];
-[ICDocCamImageQuadEditOverlay setPanHistoryIdx:];
-[ICDocCamImageQuadEditOverlay setSelectedKnob:];
-[ICDocCamImageQuadEditOverlay setTempOverlayMagnification:];
-[ICDocCamImageQuadEditOverlay setTempOverlayMagnification:animationDuration:];
-[ICDocCamImageQuadEditOverlay setTempOverlayQuadIsValid:];
-[ICDocCamImageQuadEditOverlay setUpKnobs];
-[ICDocCamImageQuadEditOverlay setupLoupeLayerIfNeeded];
-[ICDocCamImageQuadEditOverlay tempOverlayMagnification];
-[ICDocCamImageQuadEditOverlay tempOverlayQuadIsValid];
-[ICDocCamImageQuadEditOverlay touchesBeganOnQuadEditPanGestureRecognizerDelegate:];
-[ICDocCamImageQuadEditOverlay unselectAllKnobs];
-[ICDocCamImageQuadEditOverlay updateKnobLocationsToRect:];
-[ICDocCamImageQuadEditOverlay updateOutlineAndKnobColorForCurrentValidityIfNecessary];
-[ICDocCamImageQuadEditOverlay updateOutlineAndKnobColorForIsValid:];
-[ICDocCamImageQuadEditOverlay updateOutlineLayer];
-[ICDocCamImageQuadEditOverlay updateSelectedKnobContents];
-[ICDocCamImageQuadEditOverlay validRectColor];
```
