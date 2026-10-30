# `_UISlideriOSVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`, `_UISliderVisualElement`
- 18 instance variables, 7 properties, 95 instance methods, 2 class methods

## Instance variables

```
@"UIImageView" _innerThumbView;
@"UIImageView" _minValueImageView;
@"UIImageView" _maxValueImageView;
@"UIImageView" _thumbView;
@"UIImageView" _minTrackView;
@"UIImageView" _maxTrackView;
@"UIView" _minTrackClipView;
@"UIView" _maxTrackClipView;
{?="animating"b1"preparingToAnimate"b1"overridesModifiedTrackRect"b1"hasTickConfiguration"b1} _sliderFlags;
{CGPoint="x"d"y"d} _beginPoint;
d _hitOffset;
@"UIView" _thumbViewNeue;
@"NSArray" _trackColors;
B _trackIsArtworkBased;
B _thumbIsArtworkBased;
B _maxColorIsValid;
@"UISliderDataModel" _data;
@"UISlider" _slider;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UISlider",W,N,V_slider) slider;
@property (T@"UISliderDataModel",&,N,V_data) data;
@property (T@"NSArray",?,R,N) additionalTrackingViews;
```

## Class methods

```
+[_UISlideriOSVisualElement _modernThumbImageWithTraitCollection:tintColor:];
+[_UISlideriOSVisualElement drawingMetricsForPlatform];
```

## Instance methods

```
-[_UISlideriOSVisualElement cancelTouchTracking];
-[_UISlideriOSVisualElement didSetThumbTintColor];
-[_UISlideriOSVisualElement didSetMaximumTrackImageForState:];
-[_UISlideriOSVisualElement setValue:animated:];
-[_UISlideriOSVisualElement didSetSelected];
-[_UISlideriOSVisualElement thumbView];
-[_UISlideriOSVisualElement didSetValues];
-[_UISlideriOSVisualElement minimumValueImageRectForBounds:];
-[_UISlideriOSVisualElement pointerInteraction:styleForRegion:];
-[_UISlideriOSVisualElement valueTextRectForBounds:];
-[_UISlideriOSVisualElement didSetEnabled];
-[_UISlideriOSVisualElement _intrinsicSizeWithinSize:];
-[_UISlideriOSVisualElement init];
-[_UISlideriOSVisualElement maxTrackView];
-[_UISlideriOSVisualElement didSetHighlighted];
-[_UISlideriOSVisualElement didUpdateConfiguration];
-[_UISlideriOSVisualElement alignmentRectInsets];
-[_UISlideriOSVisualElement thumbHitEdgeInsets];
-[_UISlideriOSVisualElement createThumbView];
-[_UISlideriOSVisualElement endTrackingWithTouch:withEvent:];
-[_UISlideriOSVisualElement currentMaximumTrackImage];
-[_UISlideriOSVisualElement continueTrackingWithTouch:withEvent:];
-[_UISlideriOSVisualElement data];
-[_UISlideriOSVisualElement didPerformLayout];
-[_UISlideriOSVisualElement dealloc];
-[_UISlideriOSVisualElement didSetMinimumValueImage];
-[_UISlideriOSVisualElement isAnimatingValueChange];
-[_UISlideriOSVisualElement setSlider:];
-[_UISlideriOSVisualElement currentMinimumTrackImage];
-[_UISlideriOSVisualElement hitTest:withEvent:];
-[_UISlideriOSVisualElement currentThumbImage];
-[_UISlideriOSVisualElement maximumValueImage];
-[_UISlideriOSVisualElement beginTrackingWithTouch:withEvent:];
-[_UISlideriOSVisualElement didSetMinimumTrackTintColor];
-[_UISlideriOSVisualElement setBounds:];
-[_UISlideriOSVisualElement didSetMaximumTrackImageForStates];
-[_UISlideriOSVisualElement sizeThatFits:];
-[_UISlideriOSVisualElement _contentHuggingDefault_isUsuallyFixedHeight];
-[_UISlideriOSVisualElement tintColorDidChange];
-[_UISlideriOSVisualElement thumbTintColor];
-[_UISlideriOSVisualElement gestureRecognizerShouldBegin:];
-[_UISlideriOSVisualElement didSetThumbImageForStates];
-[_UISlideriOSVisualElement didSetMaximumTrackTintColor];
-[_UISlideriOSVisualElement didSetThumbImageForState:];
-[_UISlideriOSVisualElement setData:];
-[_UISlideriOSVisualElement didSetShowValue];
-[_UISlideriOSVisualElement maximumValueImageRectForBounds:];
-[_UISlideriOSVisualElement didChangeMinimumTrackVisibleWithDuration:];
-[_UISlideriOSVisualElement slider];
-[_UISlideriOSVisualElement pointerInteraction:regionForRequest:defaultRegion:];
-[_UISlideriOSVisualElement thumbViewNeue];
-[_UISlideriOSVisualElement setFrame:];
-[_UISlideriOSVisualElement minTrackView];
-[_UISlideriOSVisualElement _controlTouchBegan:withEvent:];
-[_UISlideriOSVisualElement thumbRectForBounds:trackRect:value:];
-[_UISlideriOSVisualElement didUpdateTraitCollection];
-[_UISlideriOSVisualElement didSetMinimumTrackImageForState:];
-[_UISlideriOSVisualElement _traitCollectionDidChangeInternal:];
-[_UISlideriOSVisualElement trackRectForBounds:];
-[_UISlideriOSVisualElement minValueImageView];
-[_UISlideriOSVisualElement _controlTouchMoved:withEvent:];
-[_UISlideriOSVisualElement didSetThumbEnabled];
-[_UISlideriOSVisualElement didSetMinimumTrackImageForStates];
-[_UISlideriOSVisualElement initWithFrame:];
-[_UISlideriOSVisualElement cancelMouseTracking];
-[_UISlideriOSVisualElement maxValueImageView];
-[_UISlideriOSVisualElement _controlTouchEnded:withEvent:];
-[_UISlideriOSVisualElement state];
-[_UISlideriOSVisualElement didSetContinuous];
-[_UISlideriOSVisualElement didSetMaximumValueImage];
-[_UISlideriOSVisualElement _layoutSubviewsForBoundsChange:];
-[_UISlideriOSVisualElement _bounceMinMaxValueImageViewsIfNeeded];
-[_UISlideriOSVisualElement _buildTrackArtwork];
-[_UISlideriOSVisualElement _contentSizeCategoryChanged:];
-[_UISlideriOSVisualElement _cornerRadiusForRect:];
-[_UISlideriOSVisualElement _initImages];
-[_UISlideriOSVisualElement _initSubviews];
-[_UISlideriOSVisualElement _listenForContentSizeCategoryChangesIfNecessary];
-[_UISlideriOSVisualElement _maxTrackClipView];
-[_UISlideriOSVisualElement _minTrackClipView];
-[_UISlideriOSVisualElement _modifiedTrackRect:];
-[_UISlideriOSVisualElement _rebuildControlThumb:track:];
-[_UISlideriOSVisualElement _setSliderNeedsLayout];
-[_UISlideriOSVisualElement _setValue:andSendAction:];
-[_UISlideriOSVisualElement _setupFeedback];
-[_UISlideriOSVisualElement _shouldBeginTrackingAtPoint:pointInKnob:inKnob:];
-[_UISlideriOSVisualElement _sliderAnimationDidStop:];
-[_UISlideriOSVisualElement _sliderAnimationWillStart];
-[_UISlideriOSVisualElement _updateAppearanceForEnabled:];
-[_UISlideriOSVisualElement _updateMaxTrackColorForInitialization:];
-[_UISlideriOSVisualElement _updateMinimumTrackTintColor];
-[_UISlideriOSVisualElement createThumbViewNeue];
-[_UISlideriOSVisualElement didUpdateExpansionFactor];
-[_UISlideriOSVisualElement showValueDidChange];
-[_UISlideriOSVisualElement thumbDimensionNeue];
```
