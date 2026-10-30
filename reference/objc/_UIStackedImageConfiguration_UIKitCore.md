# `_UIStackedImageConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 56 instance variables, 57 properties, 118 instance methods, 3 class methods

## Instance variables

```
B _overlayFixedFrame;
B _adjustMotionForSize;
B _flatImageContainsCornerRadius;
B _useSeparateUnfocusedShadowImage;
B _allowsNonOpaqueShadow;
B _boostBrightness;
B _hueShift;
B _disableMask;
B _focusCursorEnabled;
B _fullBleedCenteredGrowth;
q _selectionStyle;
Q _maximumParallaxImages;
d _maximumParallaxDepth;
d _overlayDepth;
d _zDepth;
d _rotationAmount;
d _scaleSizeIncrease;
d _pressedScaleAdjustment;
d _unmaskedOverlayScaleFactor;
d _cornerRadius;
d _continuousCornerRadiusEnabled;
d _specularHighlightHorizontalPositionSensitivity;
d _specularHighlightVerticalPosition;
d _specularHighlightVerticalPositionSensitivity;
d _specularOpacity;
d _defaultFocusedShadowOpacity;
d _defaultHighlightedShadowOpacity;
d _defaultUnfocusedShadowOpacity;
d _fullBleedFocusedShadowOpacity;
d _fullBleedUnfocusedShadowOpacity;
d _focusCursorShadowOpacityAdjustment;
d _defaultFocusedShadowRadius;
d _defaultHighlightedShadowRadius;
d _defaultUnfocusedShadowRadius;
d _fullBleedFocusedShadowRadius;
d _fullBleedUnfocusedShadowRadius;
d _defaultFocusedShadowVerticalOffset;
d _defaultHighlightedShadowVerticalOffset;
d _defaultUnfocusedShadowVerticalOffset;
d _defaultSelectedShadowVerticalOffset;
@"UIImage" _placeholderImage;
d _focusCursorBorderWidth;
d _radiosityOffset;
d _radiosityStrength;
d _shadowSelectionDuration;
d _shadowUnselectionDuration;
d _repositionUnselectionDuration;
d _layerSelectionDuration;
d _layerUnselectionDuration;
d _minimumFocusDuration;
d _pressedDuration;
d _unpressedDuration;
d _fullBleedOffset;
d _expansionAmount;
{CGPoint="x"d"y"d} _translationOffset;
{CACornerRadii="minXMaxY"{CGSize="width"d"height"d}"maxXMaxY"{CGSize="width"d"height"d}"maxXMinY"{CGSize="width"d"height"d}"minXMinY"{CGSize="width"d"height"d}} _cornerRadii;
```

## Properties

```
@property (Tq,N,V_selectionStyle) selectionStyle;
@property (TQ,N,V_maximumParallaxImages) maximumParallaxImages;
@property (Td,N,V_maximumParallaxDepth) maximumParallaxDepth;
@property (Td,N,V_overlayDepth) overlayDepth;
@property (TB,N,V_overlayFixedFrame) overlayFixedFrame;
@property (Td,N,V_zDepth) zDepth;
@property (TB,N,V_adjustMotionForSize) adjustMotionForSize;
@property (Td,N,V_rotationAmount) rotationAmount;
@property (Td,N,V_scaleSizeIncrease) scaleSizeIncrease;
@property (Td,N,V_pressedScaleAdjustment) pressedScaleAdjustment;
@property (T{CGPoint=dd},N,V_translationOffset) translationOffset;
@property (Td,N,V_unmaskedOverlayScaleFactor) unmaskedOverlayScaleFactor;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N,V_cornerRadii) cornerRadii;
@property (Td,N,GisContinuousCornerRadiusEnabled,V_continuousCornerRadiusEnabled) continuousCornerRadiusEnabled;
@property (TB,N,V_flatImageContainsCornerRadius) flatImageContainsCornerRadius;
@property (Td,N,V_specularHighlightHorizontalPositionSensitivity) specularHighlightHorizontalPositionSensitivity;
@property (Td,N,V_specularHighlightVerticalPosition) specularHighlightVerticalPosition;
@property (Td,N,V_specularHighlightVerticalPositionSensitivity) specularHighlightVerticalPositionSensitivity;
@property (Td,N,V_specularOpacity) specularOpacity;
@property (Td,N,V_defaultFocusedShadowOpacity) defaultFocusedShadowOpacity;
@property (Td,N,V_defaultHighlightedShadowOpacity) defaultHighlightedShadowOpacity;
@property (Td,N,V_defaultUnfocusedShadowOpacity) defaultUnfocusedShadowOpacity;
@property (Td,N,V_fullBleedFocusedShadowOpacity) fullBleedFocusedShadowOpacity;
@property (Td,N,V_fullBleedUnfocusedShadowOpacity) fullBleedUnfocusedShadowOpacity;
@property (Td,N,V_focusCursorShadowOpacityAdjustment) focusCursorShadowOpacityAdjustment;
@property (Td,N,V_defaultFocusedShadowRadius) defaultFocusedShadowRadius;
@property (Td,N,V_defaultHighlightedShadowRadius) defaultHighlightedShadowRadius;
@property (Td,N,V_defaultUnfocusedShadowRadius) defaultUnfocusedShadowRadius;
@property (Td,N,V_fullBleedFocusedShadowRadius) fullBleedFocusedShadowRadius;
@property (Td,N,V_fullBleedUnfocusedShadowRadius) fullBleedUnfocusedShadowRadius;
@property (Td,N,V_defaultFocusedShadowVerticalOffset) defaultFocusedShadowVerticalOffset;
@property (Td,N,V_defaultHighlightedShadowVerticalOffset) defaultHighlightedShadowVerticalOffset;
@property (Td,N,V_defaultUnfocusedShadowVerticalOffset) defaultUnfocusedShadowVerticalOffset;
@property (Td,N,V_defaultSelectedShadowVerticalOffset) defaultSelectedShadowVerticalOffset;
@property (TB,N,V_useSeparateUnfocusedShadowImage) useSeparateUnfocusedShadowImage;
@property (T@"UIImage",&,N,V_placeholderImage) placeholderImage;
@property (TB,N,V_allowsNonOpaqueShadow) allowsNonOpaqueShadow;
@property (TB,N,V_boostBrightness) boostBrightness;
@property (TB,N,V_hueShift) hueShift;
@property (TB,N,V_disableMask) disableMask;
@property (TB,N,V_focusCursorEnabled) focusCursorEnabled;
@property (Td,N,V_focusCursorBorderWidth) focusCursorBorderWidth;
@property (Td,N,V_radiosityOffset) radiosityOffset;
@property (Td,N,V_radiosityStrength) radiosityStrength;
@property (T@"_UIFocusAnimationConfiguration",R,C,N) focusAnimationConfiguration;
@property (Td,N,V_shadowSelectionDuration) shadowSelectionDuration;
@property (Td,N,V_shadowUnselectionDuration) shadowUnselectionDuration;
@property (Td,N,V_repositionUnselectionDuration) repositionUnselectionDuration;
@property (Td,N,V_layerSelectionDuration) layerSelectionDuration;
@property (Td,N,V_layerUnselectionDuration) layerUnselectionDuration;
@property (Td,N,V_minimumFocusDuration) minimumFocusDuration;
@property (Td,N,V_pressedDuration) pressedDuration;
@property (Td,N,V_unpressedDuration) unpressedDuration;
@property (TB,N,V_fullBleedCenteredGrowth) fullBleedCenteredGrowth;
@property (Td,N,V_fullBleedOffset) fullBleedOffset;
@property (Td,N,V_expansionAmount) expansionAmount;
```

## Class methods

```
+[_UIStackedImageConfiguration _scaledSizeForSize:focusSizeIncrease:selectionStyle:];
+[_UIStackedImageConfiguration newAppIconConfiguration];
+[_UIStackedImageConfiguration newStandardConfiguration];
```

## Instance methods

```
-[_UIStackedImageConfiguration cornerRadii];
-[_UIStackedImageConfiguration init];
-[_UIStackedImageConfiguration setSelectionStyle:];
-[_UIStackedImageConfiguration dealloc];
-[_UIStackedImageConfiguration setCornerRadii:];
-[_UIStackedImageConfiguration selectionStyle];
-[_UIStackedImageConfiguration minimumFocusDuration];
-[_UIStackedImageConfiguration setCornerRadius:];
-[_UIStackedImageConfiguration placeholderImage];
-[_UIStackedImageConfiguration cornerRadius];
-[_UIStackedImageConfiguration setMinimumFocusDuration:];
-[_UIStackedImageConfiguration copyWithZone:];
-[_UIStackedImageConfiguration isEqual:];
-[_UIStackedImageConfiguration setPlaceholderImage:];
-[_UIStackedImageConfiguration defaultHighlightedShadowOpacity];
-[_UIStackedImageConfiguration expansionAmount];
-[_UIStackedImageConfiguration fullBleedOffset];
-[_UIStackedImageConfiguration radiosityOffset];
-[_UIStackedImageConfiguration setDisableMask:];
-[_UIStackedImageConfiguration boostBrightness];
-[_UIStackedImageConfiguration fullBleedUnfocusedShadowOpacity];
-[_UIStackedImageConfiguration isContinuousCornerRadiusEnabled];
-[_UIStackedImageConfiguration pressedDuration];
-[_UIStackedImageConfiguration setDefaultFocusedShadowOpacity:];
-[_UIStackedImageConfiguration specularOpacity];
-[_UIStackedImageConfiguration useSeparateUnfocusedShadowImage];
-[_UIStackedImageConfiguration _highContrastFocusIndicatorChanged:];
-[_UIStackedImageConfiguration adjustMotionForSize];
-[_UIStackedImageConfiguration allowsNonOpaqueShadow];
-[_UIStackedImageConfiguration defaultFocusedShadowOpacity];
-[_UIStackedImageConfiguration defaultFocusedShadowRadius];
-[_UIStackedImageConfiguration defaultFocusedShadowVerticalOffset];
-[_UIStackedImageConfiguration defaultHighlightedShadowRadius];
-[_UIStackedImageConfiguration defaultHighlightedShadowVerticalOffset];
-[_UIStackedImageConfiguration defaultSelectedShadowVerticalOffset];
-[_UIStackedImageConfiguration defaultUnfocusedShadowOpacity];
-[_UIStackedImageConfiguration defaultUnfocusedShadowRadius];
-[_UIStackedImageConfiguration defaultUnfocusedShadowVerticalOffset];
-[_UIStackedImageConfiguration disableMask];
-[_UIStackedImageConfiguration flatImageContainsCornerRadius];
-[_UIStackedImageConfiguration focusAnimationConfiguration];
-[_UIStackedImageConfiguration focusCursorBorderWidth];
-[_UIStackedImageConfiguration focusCursorEnabled];
-[_UIStackedImageConfiguration focusCursorShadowOpacityAdjustment];
-[_UIStackedImageConfiguration fullBleedCenteredGrowth];
-[_UIStackedImageConfiguration fullBleedFocusedShadowOpacity];
-[_UIStackedImageConfiguration fullBleedFocusedShadowRadius];
-[_UIStackedImageConfiguration fullBleedUnfocusedShadowRadius];
-[_UIStackedImageConfiguration hueShift];
-[_UIStackedImageConfiguration layerSelectionDuration];
-[_UIStackedImageConfiguration layerUnselectionDuration];
-[_UIStackedImageConfiguration maximumParallaxDepth];
-[_UIStackedImageConfiguration maximumParallaxImages];
-[_UIStackedImageConfiguration overlayDepth];
-[_UIStackedImageConfiguration overlayFixedFrame];
-[_UIStackedImageConfiguration pressedScaleAdjustment];
-[_UIStackedImageConfiguration radiosityStrength];
-[_UIStackedImageConfiguration repositionUnselectionDuration];
-[_UIStackedImageConfiguration rotationAmount];
-[_UIStackedImageConfiguration scaleSizeIncrease];
-[_UIStackedImageConfiguration setAdjustMotionForSize:];
-[_UIStackedImageConfiguration setAllowsNonOpaqueShadow:];
-[_UIStackedImageConfiguration setBoostBrightness:];
-[_UIStackedImageConfiguration setContinuousCornerRadiusEnabled:];
-[_UIStackedImageConfiguration setDefaultFocusedShadowRadius:];
-[_UIStackedImageConfiguration setDefaultFocusedShadowVerticalOffset:];
-[_UIStackedImageConfiguration setDefaultHighlightedShadowOpacity:];
-[_UIStackedImageConfiguration setDefaultHighlightedShadowRadius:];
-[_UIStackedImageConfiguration setDefaultHighlightedShadowVerticalOffset:];
-[_UIStackedImageConfiguration setDefaultSelectedShadowVerticalOffset:];
-[_UIStackedImageConfiguration setDefaultUnfocusedShadowOpacity:];
-[_UIStackedImageConfiguration setDefaultUnfocusedShadowRadius:];
-[_UIStackedImageConfiguration setDefaultUnfocusedShadowVerticalOffset:];
-[_UIStackedImageConfiguration setExpansionAmount:];
-[_UIStackedImageConfiguration setFlatImageContainsCornerRadius:];
-[_UIStackedImageConfiguration setFocusCursorBorderWidth:];
-[_UIStackedImageConfiguration setFocusCursorEnabled:];
-[_UIStackedImageConfiguration setFocusCursorShadowOpacityAdjustment:];
-[_UIStackedImageConfiguration setFullBleedCenteredGrowth:];
-[_UIStackedImageConfiguration setFullBleedFocusedShadowOpacity:];
-[_UIStackedImageConfiguration setFullBleedFocusedShadowRadius:];
-[_UIStackedImageConfiguration setFullBleedOffset:];
-[_UIStackedImageConfiguration setFullBleedUnfocusedShadowOpacity:];
-[_UIStackedImageConfiguration setFullBleedUnfocusedShadowRadius:];
-[_UIStackedImageConfiguration setHueShift:];
-[_UIStackedImageConfiguration setLayerSelectionDuration:];
-[_UIStackedImageConfiguration setLayerUnselectionDuration:];
-[_UIStackedImageConfiguration setMaximumParallaxDepth:];
-[_UIStackedImageConfiguration setMaximumParallaxImages:];
-[_UIStackedImageConfiguration setOverlayDepth:];
-[_UIStackedImageConfiguration setOverlayFixedFrame:];
-[_UIStackedImageConfiguration setPressedDuration:];
-[_UIStackedImageConfiguration setPressedScaleAdjustment:];
-[_UIStackedImageConfiguration setRadiosityOffset:];
-[_UIStackedImageConfiguration setRadiosityStrength:];
-[_UIStackedImageConfiguration setRepositionUnselectionDuration:];
-[_UIStackedImageConfiguration setRotationAmount:];
-[_UIStackedImageConfiguration setScaleSizeIncrease:];
-[_UIStackedImageConfiguration setShadowSelectionDuration:];
-[_UIStackedImageConfiguration setShadowUnselectionDuration:];
-[_UIStackedImageConfiguration setSpecularHighlightHorizontalPositionSensitivity:];
-[_UIStackedImageConfiguration setSpecularHighlightVerticalPosition:];
-[_UIStackedImageConfiguration setSpecularHighlightVerticalPositionSensitivity:];
-[_UIStackedImageConfiguration setSpecularOpacity:];
-[_UIStackedImageConfiguration setTranslationOffset:];
-[_UIStackedImageConfiguration setUnmaskedOverlayScaleFactor:];
-[_UIStackedImageConfiguration setUnpressedDuration:];
-[_UIStackedImageConfiguration setUseSeparateUnfocusedShadowImage:];
-[_UIStackedImageConfiguration setZDepth:];
-[_UIStackedImageConfiguration shadowSelectionDuration];
-[_UIStackedImageConfiguration shadowUnselectionDuration];
-[_UIStackedImageConfiguration specularHighlightHorizontalPositionSensitivity];
-[_UIStackedImageConfiguration specularHighlightVerticalPosition];
-[_UIStackedImageConfiguration specularHighlightVerticalPositionSensitivity];
-[_UIStackedImageConfiguration translationOffset];
-[_UIStackedImageConfiguration unmaskedOverlayScaleFactor];
-[_UIStackedImageConfiguration unpressedDuration];
-[_UIStackedImageConfiguration zDepth];
```
