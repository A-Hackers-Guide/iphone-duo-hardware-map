# `CAMZoomDial`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 31 instance variables, 45 properties, 102 instance methods, 6 class methods

## Instance variables

```
B _expanded;
B _hideLabels;
B _hideFocalLengthLabels;
B __backgroundViewUpdateNeeded;
B __labelsUpdateNeeded;
B __ticksUpdateNeeded;
B __maskUpdateNeeded;
B __canLoadImages;
@"NSArray" _zoomFactors;
@"NSArray" _zoomPoints;
d _minAvailableZoomFactor;
d _maxAvailableZoomFactor;
d _zoomFactor;
d _contentMaskingHeight;
d _contractionDistance;
q _orientation;
d _angleDeltaForZoomRange;
@"UIImageView" __backgroundView;
@"UIView" __contentContainerView;
@"UIView" __labelContainerView;
@"UIView" __focalLengthLabelContainerView;
@"UIImageView" __ticksView;
@"UIImageView" __contentMaskView;
@"UIView" __needleView;
@"NSArray" __focalLengthLabelsPortrait;
@"NSArray" __focalLengthLabelsLandscape;
@"NSArray" __labels;
@"NSObject<OS_dispatch_queue>" __imageGenerationQueue;
q __backgroundImageJobIdentifier;
q __ticksImageJobIdentifier;
q __maskImageJobIdentifier;
```

## Properties

```
@property (Td,R,N) _backgroundAlpha;
@property (T@"UIImageView",R,N,V__backgroundView) _backgroundView;
@property (T@"UIView",R,N,V__contentContainerView) _contentContainerView;
@property (T@"UIView",R,N,V__labelContainerView) _labelContainerView;
@property (T@"UIView",R,N,V__focalLengthLabelContainerView) _focalLengthLabelContainerView;
@property (T@"UIImageView",R,N,V__ticksView) _ticksView;
@property (T@"UIImageView",R,N,V__contentMaskView) _contentMaskView;
@property (T@"UIView",R,N,V__needleView) _needleView;
@property (T@"NSArray",&,N,S_setFocalLengthLabelsPortrait:,V__focalLengthLabelsPortrait) _focalLengthLabelsPortrait;
@property (T@"NSArray",&,N,S_setFocalLengthLabelsLandscape:,V__focalLengthLabelsLandscape) _focalLengthLabelsLandscape;
@property (T@"NSArray",&,N,S_setLabels:,V__labels) _labels;
@property (Td,R,N) _fullRadius;
@property (Td,R,N) _fullRadiusInset;
@property (Td,R,N) _radiusDelta;
@property (Td,R,N) _borderStrokeWidth;
@property (Td,R,N) _tickLabelCenterRadialInset;
@property (Td,R,N) _focalLengthInsetPortrait;
@property (Td,R,N) _focalLengthInsetLandscape;
@property (Td,R,N) _labelPaddingForContentSizeCategory;
@property (TB,N,G_isBackgroundViewUpdateNeeded,S_setBackgroundViewUpdateNeeded:,V__backgroundViewUpdateNeeded) _backgroundViewUpdateNeeded;
@property (TB,N,G_isLabelsUpdateNeeded,S_setLabelsUpdateNeeded:,V__labelsUpdateNeeded) _labelsUpdateNeeded;
@property (TB,N,G_isTicksUpdateNeeded,S_setTicksUpdateNeeded:,V__ticksUpdateNeeded) _ticksUpdateNeeded;
@property (TB,N,G_isMaskUpdateNeeded,S_setMaskUpdateNeeded:,V__maskUpdateNeeded) _maskUpdateNeeded;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__imageGenerationQueue) _imageGenerationQueue;
@property (Tq,N,S_setBackgroundImageJobIdentifier:,V__backgroundImageJobIdentifier) _backgroundImageJobIdentifier;
@property (Tq,N,S_setTicksImageJobIdentifier:,V__ticksImageJobIdentifier) _ticksImageJobIdentifier;
@property (Tq,N,S_setMaskImageJobIdentifier:,V__maskImageJobIdentifier) _maskImageJobIdentifier;
@property (TB,N,S_setCanLoadImages:,V__canLoadImages) _canLoadImages;
@property (T@"NSArray",R,N,V_zoomFactors) zoomFactors;
@property (T@"NSArray",&,N,V_zoomPoints) zoomPoints;
@property (Td,R,N) minimumZoomFactor;
@property (Td,R,N) maximumZoomFactor;
@property (Td,N,V_minAvailableZoomFactor) minAvailableZoomFactor;
@property (Td,N,V_maxAvailableZoomFactor) maxAvailableZoomFactor;
@property (Td,N,V_zoomFactor) zoomFactor;
@property (Td,N,V_contentMaskingHeight) contentMaskingHeight;
@property (Td,N,V_contractionDistance) contractionDistance;
@property (TB,N,GisExpanded,V_expanded) expanded;
@property (Tq,N,V_orientation) orientation;
@property (TB,N,V_hideLabels) hideLabels;
@property (TB,N,V_hideFocalLengthLabels) hideFocalLengthLabels;
@property (T@"NSArray",R,N) activeZoomFactorLabels;
@property (T{CGPoint=dd},R,N) dialCenter;
@property (Td,R,N) dialBorderWidth;
@property (Td,N,V_angleDeltaForZoomRange) angleDeltaForZoomRange;
```

## Class methods

```
+[CAMZoomDial _createBackgroundImageForBounds:dialCenter:radius:backgroundAlpha:borderStrokeWidth:];
+[CAMZoomDial _createMaskImageWithSize:tickLabelCenterRadialInset:notchMaskImage:];
+[CAMZoomDial _createTicksImageForBounds:dialCenter:radius:pixelWidth:zoomFactors:minAvailableZoomFactor:maxAvailableZoomFactor:signedAngleDeltaForZoomRange:];
+[CAMZoomDial _normalizedValueForZoomFactor:min:max:];
+[CAMZoomDial _offsetAngleForZoomFactor:relativeToCurrentZoomFactor:currentZoomFactor:min:max:signedAngleDeltaForZoomRange:];
+[CAMZoomDial _pointForOffsetAngle:dialCenter:radius:];
```

## Instance methods

```
-[CAMZoomDial setOrientation:animated:];
-[CAMZoomDial setOrientation:];
-[CAMZoomDial _setCanLoadImages:];
-[CAMZoomDial _setBackgroundViewUpdateNeeded:];
-[CAMZoomDial _zoomPointIndexesForPrioritizedFocalLengthLabels];
-[CAMZoomDial angleDeltaForZoomRange];
-[CAMZoomDial setMaxAvailableZoomFactor:];
-[CAMZoomDial prepareForDisplay];
-[CAMZoomDial _updateBackgroundImageViewIfNeeded];
-[CAMZoomDial zoomFactor];
-[CAMZoomDial hideFocalLengthLabels];
-[CAMZoomDial _backgroundAlpha];
-[CAMZoomDial setExpanded:];
-[CAMZoomDial setZoomFactor:];
-[CAMZoomDial _setTicksUpdateNeeded:];
-[CAMZoomDial setHideLabels:];
-[CAMZoomDial _commonCAMZoomDialInitialization];
-[CAMZoomDial dialBorderWidth];
-[CAMZoomDial _isTicksUpdateNeeded];
-[CAMZoomDial maximumZoomFactor];
-[CAMZoomDial isExpanded];
-[CAMZoomDial setZoomPoints:];
-[CAMZoomDial _setLabels:];
-[CAMZoomDial _layoutSubviewsWithTicks];
-[CAMZoomDial _invalidateImagesForViewSize];
-[CAMZoomDial _updateMaskImageIfNeeded];
-[CAMZoomDial zoomPoints];
-[CAMZoomDial offsetAngleForPoint:];
-[CAMZoomDial offsetAngleForZoomFactor:];
-[CAMZoomDial _radiusDelta];
-[CAMZoomDial minimumZoomFactor];
-[CAMZoomDial orientation];
-[CAMZoomDial _imageGenerationQueue];
-[CAMZoomDial maxAvailableZoomFactor];
-[CAMZoomDial _updateContentIfNeeded];
-[CAMZoomDial layoutSubviews];
-[CAMZoomDial _needleView];
-[CAMZoomDial _labels];
-[CAMZoomDial contentMaskingHeight];
-[CAMZoomDial normalizedValueForZoomFactor:];
-[CAMZoomDial zoomFactorForOffsetAngle:];
-[CAMZoomDial _fullRadiusInset];
-[CAMZoomDial _setTicksImageJobIdentifier:];
-[CAMZoomDial contractionDistance];
-[CAMZoomDial _updateTicksImageIfNeeded];
-[CAMZoomDial _pointForOffsetAngle:radialInset:assumeExpanded:];
-[CAMZoomDial zoomFactors];
-[CAMZoomDial _isBackgroundViewUpdateNeeded];
-[CAMZoomDial _offsetAngleForZoomPoint:];
-[CAMZoomDial _contentMaskView];
-[CAMZoomDial _backgroundView];
-[CAMZoomDial hideLabels];
-[CAMZoomDial _backgroundImageJobIdentifier];
-[CAMZoomDial setBounds:];
-[CAMZoomDial _labelContainerView];
-[CAMZoomDial _textCenterForOffsetAngle:assumeExpanded:];
-[CAMZoomDial _maskImageJobIdentifier];
-[CAMZoomDial _focalLengthLabelsPortrait];
-[CAMZoomDial activeZoomFactorLabels];
-[CAMZoomDial setHideFocalLengthLabels:];
-[CAMZoomDial _focalLengthInsetPortrait];
-[CAMZoomDial _setBackgroundImageJobIdentifier:];
-[CAMZoomDial _updatePortraitFocalLengthLabelAlphas];
-[CAMZoomDial _offsetAngleForZoomFactor:relativeToCurrentZoomFactor:];
-[CAMZoomDial minAvailableZoomFactor];
-[CAMZoomDial _contentContainerView];
-[CAMZoomDial _focalLengthInsetLandscape];
-[CAMZoomDial _updateLabels];
-[CAMZoomDial _tickEndpointForOffsetAngle:isTop:];
-[CAMZoomDial setFrame:];
-[CAMZoomDial setContractionDistance:];
-[CAMZoomDial _fullRadius];
-[CAMZoomDial setAngleDeltaForZoomRange:];
-[CAMZoomDial _borderStrokeWidth];
-[CAMZoomDial _updateLabelsIfNeeded];
-[CAMZoomDial _tickLabelCenterRadialInset];
-[CAMZoomDial zoomFactorForNormalizedValue:];
-[CAMZoomDial _focalLengthLabelContainerView];
-[CAMZoomDial _ticksView];
-[CAMZoomDial _setMaskImageJobIdentifier:];
-[CAMZoomDial _labelPaddingForContentSizeCategory];
-[CAMZoomDial _preferredContentSizeCategoryChanged];
-[CAMZoomDial _signedAngleDeltaForZoomRange];
-[CAMZoomDial _updateFocalLengthLabelAlphas];
-[CAMZoomDial setMinAvailableZoomFactor:];
-[CAMZoomDial setContentMaskingHeight:];
-[CAMZoomDial _layoutBackgroundAndContainerWithContentInset:];
-[CAMZoomDial _isLabelsUpdateNeeded];
-[CAMZoomDial initWithFrame:];
-[CAMZoomDial _updateFocalLengthLabels];
-[CAMZoomDial _focalLengthLabelsLandscape];
-[CAMZoomDial _setLabelsUpdateNeeded:];
-[CAMZoomDial _labelRotationAngleForOrientation];
-[CAMZoomDial _ticksImageJobIdentifier];
-[CAMZoomDial _setMaskUpdateNeeded:];
-[CAMZoomDial dialCenter];
-[CAMZoomDial _isMaskUpdateNeeded];
-[CAMZoomDial textCenterForZoomFactor:assumeExpanded:];
-[CAMZoomDial _setFocalLengthLabelsPortrait:];
-[CAMZoomDial _updateMinimizedLabels];
-[CAMZoomDial _canLoadImages];
-[CAMZoomDial _setFocalLengthLabelsLandscape:];
```
