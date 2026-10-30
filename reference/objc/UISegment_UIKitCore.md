# `UISegment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIImageView`
- Protocols: `CAAnimationDelegate`, `UISegmentProtocol`
- 19 instance variables, 17 properties, 121 instance methods, 1 class methods

## Instance variables

```
@"UIView" _info;
@"UIImageView" _backgroundView;
@"UIView" _selectionIndicatorView;
@"UIImageView" _selectionImageView;
@"UIView" _focusIndicatorView;
@"UIView<UISegmentBezelView>" _bezelView;
@"_UISegmentedControlAppearanceStorage" _appearanceStorage;
@"UIView<_UISegmentedControlContentView>" _infoContentView;
d _width;
{CGSize="width"d"height"d} _contentOffset;
q _barStyle;
Q _rightSegmentState;
@"NSString" _badgeValue;
@"_UIBadgeView" _badgeView;
@ _objectValue;
{?="size"b2"selected"b1"highlighted"b1"showDivider"b1"hasImage"b1"position"b3"autosizeText"b1"isMomentary"b1"wasSelected"b1"needsBackgroundAndContentViewUpdate"b1"usesAXTextSize"b1"selectionIndicatorDragged"b1"adjustsForContentSizeCategory"b1"hovered"b1"animatingSelectionIndicator"b1"hasCustomInfoView"b1"hasMaterial"b1"useSpringBoardVibrancy"b1} _segmentFlags;
@"NSArray" _infoConstraints;
@"UIAction" _action;
d _requestedScaleFactor;
```

## Properties

```
@property (T@"NSArray",C,N,S_setInfoConstraints:,V_infoConstraints) _infoConstraints;
@property (T@"UIAction",C,N,V_action) action;
@property (TB,N,GisSelected) selected;
@property (TB,N,GisMomentary) momentary;
@property (T@"NSString",C,N) badgeValue;
@property (T@"UIView",R) badgeView;
@property (Td,N,V_requestedScaleFactor) requestedScaleFactor;
@property (TI,N) segmentPosition;
@property (TB,N,GisEnabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisHighlighted) highlighted;
@property (TB,R,N,GisRightSelected) rightSelected;
@property (TB,R,N,GisRightHighlighted) rightHighlighted;
@property (Ti,R,N) controlSize;
```

## Class methods

```
+[UISegment _backgroundImageWithStorage:mini:state:position:drawMode:isCustom:defaultBlock:];
```

## Instance methods

```
-[UISegment badgeValue];
-[UISegment objectValue];
-[UISegment setBadgeValue:];
-[UISegment setSelected:];
-[UISegment animationDidStop:finished:];
-[UISegment label];
-[UISegment isMomentary];
-[UISegment focusEffect];
-[UISegment didUpdateFocusInContext:withAnimationCoordinator:];
-[UISegment contentRect];
-[UISegment isHighlighted];
-[UISegment _updateHighlight];
-[UISegment badgeView];
-[UISegment setContentOffset:];
-[UISegment dealloc];
-[UISegment disabledTextColor];
-[UISegment viewForLastBaselineLayout];
-[UISegment layoutSubviews];
-[UISegment setAction:];
-[UISegment hitTest:withEvent:];
-[UISegment action];
-[UISegment contentSize];
-[UISegment parentFocusEnvironment];
-[UISegment _updateFocusIndicator];
-[UISegment isHovered];
-[UISegment setBounds:];
-[UISegment canBecomeFocused];
-[UISegment _encodableSubviews];
-[UISegment setHovered:];
-[UISegment isEnabled];
-[UISegment tintColorDidChange];
-[UISegment setHighlighted:];
-[UISegment setTintColor:];
-[UISegment setObjectValue:];
-[UISegment removeFromSuperview];
-[UISegment setEnabled:];
-[UISegment setBarStyle:];
-[UISegment encodeWithCoder:];
-[UISegment isSelected];
-[UISegment setFrame:];
-[UISegment updateConstraints];
-[UISegment setControlSize:];
-[UISegment initWithCoder:];
-[UISegment traitCollectionDidChange:];
-[UISegment _populateArchivedSubviews:];
-[UISegment _baselineOffsetsAtSize:];
-[UISegment isRightSelected];
-[UISegment setAnimatingSelectionIndicator:];
-[UISegment setWasSelected:];
-[UISegment useBlockyMagnificationInClassic];
-[UISegment segmentPosition];
-[UISegment setShowDivider:];
-[UISegment _attributedTextForState:selected:forceSelectedAppearance:];
-[UISegment _barHeight];
-[UISegment _contentRectForBounds:];
-[UISegment _dividerImage];
-[UISegment _dividerImageIsCustom:];
-[UISegment _effectiveBackgroundTintColor];
-[UISegment _effectiveBackgroundView];
-[UISegment _effectiveDisableShadow];
-[UISegment _effectiveSelectedSegmentTintColor];
-[UISegment _effectiveSelectionView];
-[UISegment _effectiveUseDynamicShadow];
-[UISegment _effectiveVisualEffect];
-[UISegment _evaluateHighlight];
-[UISegment _finishInitialSegmentSetup];
-[UISegment _forceInfoDisplay];
-[UISegment _hasSelectedColor];
-[UISegment _highlightSelectionInfoTransform];
-[UISegment _idealWidth];
-[UISegment _infoConstraints];
-[UISegment _insertSelectionView];
-[UISegment _invalidateInfoConstraints];
-[UISegment _maximumTextSize];
-[UISegment _paddingInsets];
-[UISegment _parentSegmentedControl];
-[UISegment _positionInfo];
-[UISegment _positionInfoWithoutAnimation];
-[UISegment _preferredConfigurationForFocusAnimation:inContext:];
-[UISegment _removeSelectionIndicator];
-[UISegment _segmentLabel];
-[UISegment _segmentState];
-[UISegment _segmentedControlClass];
-[UISegment _setEnabledAppearance:];
-[UISegment _setHasMaterial:];
-[UISegment _setHighlighted:animated:];
-[UISegment _setInfoConstraints:];
-[UISegment _setSelectionIndicatorDragged:animated:];
-[UISegment _stateTextAttibutes:segmentState:];
-[UISegment _tintColorArchivingKey];
-[UISegment _updateBackgroundAndContentViews];
-[UISegment _updateBackgroundAndContentViewsIfNeeded];
-[UISegment _updateDynamicShadow:animated:];
-[UISegment _updateFloatingContentControlState:context:withAnimationCoordinator:animated:];
-[UISegment _updateSelectionIndicator];
-[UISegment _updateSelectionToTransform:infoTransform:hideSelection:shouldAnimate:];
-[UISegment _updateTextColors];
-[UISegment _wantsFocusWithoutSelectionForStyleProvider:];
-[UISegment animateAdd:];
-[UISegment animateRemoveForWidth:];
-[UISegment controlSize];
-[UISegment hitTest:forEvent:];
-[UISegment initWithInfo:size:barStyle:tintColor:appearanceStorage:position:autosizeText:adjustsForContentSizeCategory:hasMaterial:customInfoView:traitCollection:];
-[UISegment insertDividerView];
-[UISegment isAnimatingSelectionIndicator];
-[UISegment isRightHighlighted];
-[UISegment isSelectionIndicatorDragged];
-[UISegment requestedScaleFactor];
-[UISegment setAdjustsForContentSizeCategory:];
-[UISegment setAutosizeText:];
-[UISegment setMomentary:];
-[UISegment setNeedsBackgroundAndContentViewUpdate];
-[UISegment setRequestedScaleFactor:];
-[UISegment setSegmentPosition:];
-[UISegment setSelected:highlighted:];
-[UISegment setSelectionIndicatorDragged:];
-[UISegment setUsesAXTextSize:];
-[UISegment showDivider];
-[UISegment updateDividerViewForChangedSegment:];
-[UISegment updateForAppearance:];
-[UISegment updateMasking];
```
