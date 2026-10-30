# `_UIStackedImageContainerLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `_UIStackedImageContainerRenderer`, `CALayerDelegate`
- 62 instance variables, 10 properties, 150 instance methods, 2 class methods

## Instance variables

```
{CGSize="width"d"height"d} _lastLayoutSize;
q _lastLayoutSelectionStyle;
B _isContainedInStackedImageContainerView;
B _animatingToNormalState;
B _animatingStateChange;
d _selectionStartTime;
d _selectionDuration;
q _selectionStyle;
{CGSize="width"d"height"d} _radiosityImageScale;
B _radiosityNeedsLayout;
d _scale;
@"NSString" _imageStackContentsGravity;
d _radiosityRequestTime;
{CGPoint="x"d"y"d} _rotationAmount;
{CGPoint="x"d"y"d} _translationOffset;
d _maximumParallaxDepth;
B _nonOpaqueShadow;
B _singleLayerNoMask;
B _layerStackSupportsInflation;
B _layerStackInflated;
Q _layerStackInflationSeed;
B _deferredInflationPending;
@ _flatImage;
@"NSArray" _parallaxImages;
@"NSArray" _parallaxLayerDepths;
@"NSArray" _imageLayers;
@"CALayer" _flatLayer;
@"CALayer" _flatMaskLayer;
@"CALayer" _maskLayer;
@"CALayer" _radiosityLayer;
@"CALayer" _selectedPlaceholderLayer;
@"CALayer" _shadowLayer;
@"CALayer" _unfocusedShadowLayer;
@"_UIFocusSpecularHighlightLayer" _specularLayer;
@"CALayer" _cursorLayer;
@"CALayer" _cursorLayerContainer;
@"CALayer" _focusKeylineStrokeLayer;
@"CALayer" _overlayLayer;
@"CALayer" _overlayContainerLayer;
@"CALayer" _unmaskedOverlayLayer;
@"CALayer" _unmaskedOverlayContainerLayer;
@"CALayer" _imageLayersContainer;
@"CATransformLayer" _imageBackgroundEffectScaleTransformLayer;
@"CALayer" _imagePrePerspectiveRotationBackgroundEffectContainer;
@"CATransformLayer" _imagePrePerspectiveRotationParallaxTransformLayer;
@"CATransformLayer" _imagePerspectiveTransformLayer;
@"CATransformLayer" _imageRotationTransformLayer;
@"CALayer" _imagePostPerspectiveRotationBackgroundEffectContainer;
@"CATransformLayer" _imagePostPerspectiveRotationParallaxTransformLayer;
@"CATransformLayer" _maskPerspectiveTransformLayer;
@"CATransformLayer" _maskRotationTransformLayer;
@"CATransformLayer" _unmaskedOverlayPerspectiveTransformLayer;
@"CATransformLayer" _unmaskedOverlayRotationTransformLayer;
@"CATransformLayer" _cursorRotationTransformLayer;
@"CALayer" _frontmostPerspectiveTransformLayer;
@"CATransformLayer" _frontmostRotationTransformLayer;
@"_UIStackedImageLayerDelegate" _layoutDelegate;
@"UIView" _animationView;
@"_UIStackedImageConfiguration" _configuration;
@"<UINamedLayerStack>" _layerStack;
Q _controlState;
{CGPoint="x"d"y"d} _focusDirection;
```

## Properties

```
@property (T@"_UIStackedImageConfiguration",&,N,V_configuration) configuration;
@property (T@"<UINamedLayerStack>",&,N,V_layerStack) layerStack;
@property (TQ,N,V_controlState) controlState;
@property (TB,N,GisPressed) pressed;
@property (TB,N,GisSelected) selected;
@property (T{CGPoint=dd},N,V_focusDirection) focusDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStackedImageContainerLayer _layerStackObservingKeys];
+[_UIStackedImageContainerLayer _scaledSizeForSize:focusSizeIncrease:selectionStyle:];
```

## Instance methods

```
-[_UIStackedImageContainerLayer actionForLayer:forKey:];
-[_UIStackedImageContainerLayer setSelected:];
-[_UIStackedImageContainerLayer observeValueForKeyPath:ofObject:change:context:];
-[_UIStackedImageContainerLayer init];
-[_UIStackedImageContainerLayer dealloc];
-[_UIStackedImageContainerLayer setConfiguration:];
-[_UIStackedImageContainerLayer setBounds:];
-[_UIStackedImageContainerLayer setRasterizationScale:];
-[_UIStackedImageContainerLayer configuration];
-[_UIStackedImageContainerLayer removeAllAnimations];
-[_UIStackedImageContainerLayer setContentsScale:];
-[_UIStackedImageContainerLayer _setSelectionStyle:];
-[_UIStackedImageContainerLayer isPressed];
-[_UIStackedImageContainerLayer isSelected];
-[_UIStackedImageContainerLayer _setLayerStack:];
-[_UIStackedImageContainerLayer layoutSublayers];
-[_UIStackedImageContainerLayer setSelected:animated:];
-[_UIStackedImageContainerLayer setPressed:];
-[_UIStackedImageContainerLayer _isSelected];
-[_UIStackedImageContainerLayer _isEligibleForSolariumRendering];
-[_UIStackedImageContainerLayer _wrapImageLayerHierarchyInViews];
-[_UIStackedImageContainerLayer setPressed:animated:completion:];
-[_UIStackedImageContainerLayer _layerForInnerParallaxTransform];
-[_UIStackedImageContainerLayer _layerStackToDisplayScaleFactor];
-[_UIStackedImageContainerLayer _selectionStyle];
-[_UIStackedImageContainerLayer _setControlState:animated:focusAnimationCoordinator:completion:];
-[_UIStackedImageContainerLayer _updateShadowWithCATransaction:];
-[_UIStackedImageContainerLayer _applyFocusDirectionTransform];
-[_UIStackedImageContainerLayer _applyFocusDirectionTransformWithAnimationCoordinator:];
-[_UIStackedImageContainerLayer _aspectMatchesLayerStack];
-[_UIStackedImageContainerLayer _cgImageForLayeredImage:];
-[_UIStackedImageContainerLayer _configureForContainedInStackedImageContainerView];
-[_UIStackedImageContainerLayer _configuredForNonOpaqueShadow];
-[_UIStackedImageContainerLayer _contentLayers];
-[_UIStackedImageContainerLayer _currentStackLayoutBounds];
-[_UIStackedImageContainerLayer _cursorBounds];
-[_UIStackedImageContainerLayer _cursorLayer];
-[_UIStackedImageContainerLayer _deepestParallaxDepthWithOverlayDepth:];
-[_UIStackedImageContainerLayer _deselect];
-[_UIStackedImageContainerLayer _displayFrameForModelFrame:];
-[_UIStackedImageContainerLayer _effectiveAdjustMotionForSize];
-[_UIStackedImageContainerLayer _effectiveScaleSizeIncrease];
-[_UIStackedImageContainerLayer _expandedStackLayoutBounds];
-[_UIStackedImageContainerLayer _fixedFrameImageLayersTransformForDepth:fudgeFactor:];
-[_UIStackedImageContainerLayer _flatLayer];
-[_UIStackedImageContainerLayer _focusCursorInsetSizeForSize:];
-[_UIStackedImageContainerLayer _focusedScaleFactorForCurrentBounds];
-[_UIStackedImageContainerLayer _focusedShadowRadius];
-[_UIStackedImageContainerLayer _getShadowOpacity];
-[_UIStackedImageContainerLayer _hasPotentialSolariumImpact];
-[_UIStackedImageContainerLayer _idleModeFocusSizeOffset];
-[_UIStackedImageContainerLayer _imageLayersContainer];
-[_UIStackedImageContainerLayer _imageLayersScaleAmountsForCurrentState];
-[_UIStackedImageContainerLayer _imageLayersScaleTransformForCurrentState];
-[_UIStackedImageContainerLayer _imageStackContentsGravity];
-[_UIStackedImageContainerLayer _isEligibleFor3DTransforms];
-[_UIStackedImageContainerLayer _isFocused];
-[_UIStackedImageContainerLayer _isHighlighted];
-[_UIStackedImageContainerLayer _isNormal];
-[_UIStackedImageContainerLayer _layerAboveImageLayers];
-[_UIStackedImageContainerLayer _layerAboveOverlayContainer];
-[_UIStackedImageContainerLayer _layerBelowTitles];
-[_UIStackedImageContainerLayer _layerForBackgroundEffects];
-[_UIStackedImageContainerLayer _layerForImageStackHosting];
-[_UIStackedImageContainerLayer _layerForUnfocusedOverlayContainerHosting];
-[_UIStackedImageContainerLayer _layoutRadiosityLayer];
-[_UIStackedImageContainerLayer _layoutSublayer:inSuperlayerWithBounds:layoutPosition:];
-[_UIStackedImageContainerLayer _layoutSublayer:withBounds:position:];
-[_UIStackedImageContainerLayer _maskLayer];
-[_UIStackedImageContainerLayer _overlayLayer];
-[_UIStackedImageContainerLayer _parallaxDepthAtIndex:];
-[_UIStackedImageContainerLayer _parallaxLayerDepths];
-[_UIStackedImageContainerLayer _perspectiveTransformForCurrentState];
-[_UIStackedImageContainerLayer _positionAndSizeForLayerImage:];
-[_UIStackedImageContainerLayer _preferredLayoutDelegateForLayer:];
-[_UIStackedImageContainerLayer _primaryControlStateForState:];
-[_UIStackedImageContainerLayer _radiosityEnabled];
-[_UIStackedImageContainerLayer _randomImage];
-[_UIStackedImageContainerLayer _removeLayerFromSuperlayer:];
-[_UIStackedImageContainerLayer _resetAnimatingToNormalState];
-[_UIStackedImageContainerLayer _rotationTransformForCurrentFocusDirection];
-[_UIStackedImageContainerLayer _roundedBoundsSize];
-[_UIStackedImageContainerLayer _scaleAmountsForCurrentState];
-[_UIStackedImageContainerLayer _scaleTransform3DForCurrentState];
-[_UIStackedImageContainerLayer _scaleTransform3DForScaleAmounts:];
-[_UIStackedImageContainerLayer _scaledSizeForCurrentState];
-[_UIStackedImageContainerLayer _setDefaultParallaxLayerDepths];
-[_UIStackedImageContainerLayer _setFlatImage:];
-[_UIStackedImageContainerLayer _setFocusDirection:duration:];
-[_UIStackedImageContainerLayer _setIdleModeFocusSizeOffset:];
-[_UIStackedImageContainerLayer _setImageStackContentsGravity:];
-[_UIStackedImageContainerLayer _setLayerStackInflated:seed:];
-[_UIStackedImageContainerLayer _setOverlayLayer:];
-[_UIStackedImageContainerLayer _setParallaxImages:];
-[_UIStackedImageContainerLayer _setParallaxLayerDepths:];
-[_UIStackedImageContainerLayer _setUnmaskedOverlayLayer:];
-[_UIStackedImageContainerLayer _setupFrontmostTransformLayers];
-[_UIStackedImageContainerLayer _shadowLayer];
-[_UIStackedImageContainerLayer _shouldHaveNonOpaqueShadowFromLayerStack];
-[_UIStackedImageContainerLayer _showImageLayers];
-[_UIStackedImageContainerLayer _unfocusedShadowRadius];
-[_UIStackedImageContainerLayer _unmaskedOverlayLayer];
-[_UIStackedImageContainerLayer _updateContentProviderLayerFocusDirection];
-[_UIStackedImageContainerLayer _updateCornerRadiusFromConfig];
-[_UIStackedImageContainerLayer _updateFocusKeylineStrokeScale];
-[_UIStackedImageContainerLayer _updateFocusKeylineStrokeTranslation:];
-[_UIStackedImageContainerLayer _updateFullBleedImageLayers];
-[_UIStackedImageContainerLayer _updateImageLayerFilterChains];
-[_UIStackedImageContainerLayer _updateImageLayerFilterValues];
-[_UIStackedImageContainerLayer _updateImageLayersContainerMaskingAndBounds];
-[_UIStackedImageContainerLayer _updateInnerParallaxTransform];
-[_UIStackedImageContainerLayer _updateLayer:isHidden:];
-[_UIStackedImageContainerLayer _updateLayerForSelection];
-[_UIStackedImageContainerLayer _updateLayerForSelectionWithAnimationCoordinator:];
-[_UIStackedImageContainerLayer _updateMarkerLayerIfPresent];
-[_UIStackedImageContainerLayer _updateMaskScaleTransform];
-[_UIStackedImageContainerLayer _updateNonOpaqueShadowStateFromLayerStack];
-[_UIStackedImageContainerLayer _updateNormalImageLayers];
-[_UIStackedImageContainerLayer _updateOverlayContainerLayerHierarchy:];
-[_UIStackedImageContainerLayer _updateOverlayLayerTransforms];
-[_UIStackedImageContainerLayer _updateOverlayLayout];
-[_UIStackedImageContainerLayer _updatePerspective];
-[_UIStackedImageContainerLayer _updateRadiosityFromLayerStack];
-[_UIStackedImageContainerLayer _updateRotationAndTranslation:];
-[_UIStackedImageContainerLayer _updateShadowBounds];
-[_UIStackedImageContainerLayer _updateShadowLayerVisibility];
-[_UIStackedImageContainerLayer _updateShadowPositionWithOffset:];
-[_UIStackedImageContainerLayer _updateSingleLayerNoMaskFromLayerStack];
-[_UIStackedImageContainerLayer _updateSpecularLayerVisibility];
-[_UIStackedImageContainerLayer _updateSpecularTransform];
-[_UIStackedImageContainerLayer _wrapLayerInView:];
-[_UIStackedImageContainerLayer controlState];
-[_UIStackedImageContainerLayer focusDirection];
-[_UIStackedImageContainerLayer layerStack];
-[_UIStackedImageContainerLayer maskedOverlayView];
-[_UIStackedImageContainerLayer rendererControlState];
-[_UIStackedImageContainerLayer setControlState:];
-[_UIStackedImageContainerLayer setControlState:animated:];
-[_UIStackedImageContainerLayer setControlState:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerLayer setFocusDirection:];
-[_UIStackedImageContainerLayer setFocusDirection:animated:];
-[_UIStackedImageContainerLayer setLayerStack:];
-[_UIStackedImageContainerLayer setMaskedOverlayView:];
-[_UIStackedImageContainerLayer setPressed:animated:];
-[_UIStackedImageContainerLayer setRendererControlState:];
-[_UIStackedImageContainerLayer setRendererControlState:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerLayer setSelected:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerLayer setUnmaskedOverlayView:];
-[_UIStackedImageContainerLayer unmaskedOverlayView];
-[_UIStackedImageContainerLayer viewForBackgroundEffects];
```
