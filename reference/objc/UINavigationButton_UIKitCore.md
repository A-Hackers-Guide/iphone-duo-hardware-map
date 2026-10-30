# `UINavigationButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 22 instance variables, 21 properties, 123 instance methods, 2 class methods

## Instance variables

```
@"NSSet" _possibleTitles;
i _style;
q _barStyle;
@"UIColor" _navigationBarTintColor;
{CGSize="width"d"height"d} _boundsAdjustment;
@"_UIBarButtonItemAppearanceStorage" _appearanceStorage;
@"NSSet" _possibleSystemItems;
b2 _size;
@"UIBarButtonItem" _originatingButtonItem;
@"UINavigationItem" _originatingNavigationItem;
B _createdByBarButtonItem;
B _isFontScaleInvalid;
B _wantsBlendModeForAccessibilityBackgrounds;
q _buttonItemStyle;
@"NSDictionary" _stylesForSizingTitles;
d _fontScaleAdjustment;
@"UIColor" _accessibilityBackgroundTintColor;
# _appearanceGuideClass;
@"UIView" __enclosingBar;
d _minimumWidth;
d _maximumWidth;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __additionalSelectionInsets;
```

## Properties

```
@property (T@"UIView",W,N,S_setEnclosingBar:,V__enclosingBar) _enclosingBar;
@property (Td,N,V_minimumWidth) minimumWidth;
@property (Td,N,V_maximumWidth) maximumWidth;
@property (T@"UINavigationItem",W,N,V_originatingNavigationItem) originatingNavigationItem;
@property (T@"UIBarButtonItem",W,N,V_originatingButtonItem) originatingButtonItem;
@property (T#,&,N,S_setAppearanceGuideClass:,V_appearanceGuideClass) _appearanceGuideClass;
@property (Tq,N,S_setButtonItemStyle:,V_buttonItemStyle) _buttonItemStyle;
@property (T@"NSDictionary",C,N,S_setStylesForSizingTitles:,V_stylesForSizingTitles) _stylesForSizingTitles;
@property (Td,N,S_setFontScaleAdjustment:,V_fontScaleAdjustment) _fontScaleAdjustment;
@property (TB,N,S_setFontScaleInvalid:,V_isFontScaleInvalid) _isFontScaleInvalid;
@property (TB,N,S_setWantsBlendModeForAccessibilityBackgrounds:,V_wantsBlendModeForAccessibilityBackgrounds) _wantsBlendModeForAccessibilityBackgrounds;
@property (T@"UIColor",&,N,S_setAccessibilityBackgroundTintColor:,V_accessibilityBackgroundTintColor) _accessibilityBackgroundTintColor;
@property (T@"UIColor",&,N,S_setTintColor:) _tintColor;
@property (T{UIEdgeInsets=dddd},N,S_setAdditionalSelectionInsets:,V__additionalSelectionInsets) _additionalSelectionInsets;
@property (TB,N,S_setCreatedByBarButtonItem:,V_createdByBarButtonItem) _createdByBarButtonItem;
@property (T@"NSString",&,N) title;
@property (T@"UIImage",&,N) image;
@property (Tq,N,V_barStyle) barStyle;
@property (Ti,N,V_style) style;
@property (Ti,N) controlSize;
@property (T@"UIColor",&,D,N) tintColor;
```

## Class methods

```
+[UINavigationButton defaultFont];
+[UINavigationButton _resetRenderingModesForBackgroundImageView:inBarStyle:isEnabled:withAccessibilityBackground:wantsBlendModeForAccessibilityBackgrounds:accessibilityBackgroundTintColor:];
```

## Instance methods

```
-[UINavigationButton _tintColor];
-[UINavigationButton _appearanceStorage];
-[UINavigationButton _UIAppearance_setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UINavigationButton maximumWidth];
-[UINavigationButton buttonType];
-[UINavigationButton initWithImage:];
-[UINavigationButton _setAppearanceGuideClass:];
-[UINavigationButton _UIAppearance_setBackButtonBackgroundImage:forState:barMetrics:];
-[UINavigationButton _titleTextAttributesForState:];
-[UINavigationButton minimumWidth];
-[UINavigationButton _UIAppearance_setTitleTextAttributes:forState:];
-[UINavigationButton _setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UINavigationButton initWithTitle:];
-[UINavigationButton _setAdditionalSelectionInsets:];
-[UINavigationButton _setTintColor:];
-[UINavigationButton _appearanceGuideClass];
-[UINavigationButton _setTitleTextAttributes:forState:];
-[UINavigationButton _intrinsicSizeWithinSize:];
-[UINavigationButton _setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[UINavigationButton _didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UINavigationButton _accessibilityButtonShapesParametersDidChange];
-[UINavigationButton _UIAppearance_setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UINavigationButton setMinimumWidth:];
-[UINavigationButton _UIAppearance_setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[UINavigationButton dealloc];
-[UINavigationButton _UIAppearance_setTintColor:];
-[UINavigationButton _UIAppearance_setBackgroundImage:forState:style:barMetrics:];
-[UINavigationButton _updateContentInsets];
-[UINavigationButton barStyle];
-[UINavigationButton _UIAppearance_setTitlePositionAdjustment:forBarMetrics:];
-[UINavigationButton layoutSubviews];
-[UINavigationButton _updateStyle];
-[UINavigationButton _didMoveFromWindow:toWindow:];
-[UINavigationButton _setBackgroundImage:forState:barMetrics:];
-[UINavigationButton _accessibilityButtonShapesDidChangeNotification:];
-[UINavigationButton _selectedIndicatorBounds];
-[UINavigationButton _UIAppearance_setBackgroundImage:forState:barMetrics:];
-[UINavigationButton style];
-[UINavigationButton _setBackButtonBackgroundImage:forState:barMetrics:];
-[UINavigationButton canBecomeFocused];
-[UINavigationButton setStyle:];
-[UINavigationButton _setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UINavigationButton _setTitlePositionAdjustment:forBarMetrics:];
-[UINavigationButton sizeThatFits:];
-[UINavigationButton _contentHuggingDefault_isUsuallyFixedHeight];
-[UINavigationButton setHighlighted:];
-[UINavigationButton _setBackgroundImage:forState:style:barMetrics:];
-[UINavigationButton title];
-[UINavigationButton _isModernButton];
-[UINavigationButton setEnabled:];
-[UINavigationButton setBarStyle:];
-[UINavigationButton setMaximumWidth:];
-[UINavigationButton setPointerInteractionEnabled:];
-[UINavigationButton setControlSize:];
-[UINavigationButton setTitle:];
-[UINavigationButton _supportsMacIdiom];
-[UINavigationButton _additionalSelectionInsets];
-[UINavigationButton image];
-[UINavigationButton setImage:];
-[UINavigationButton _setGroupName:forNavigationBar:];
-[UINavigationButton _wantsAccessibilityButtonShapes];
-[UINavigationButton _accessibilityBackgroundTintColor];
-[UINavigationButton _activeBarMetrics];
-[UINavigationButton _activeVisualStyle];
-[UINavigationButton _adjustBounds];
-[UINavigationButton _adjustedDefaultTitleFont];
-[UINavigationButton _applyBarButtonAppearanceStorage:withTaggedSelectors:];
-[UINavigationButton _backgroundImageForState:barMetrics:];
-[UINavigationButton _backgroundVerticalPositionAdjustmentForBarMetrics:];
-[UINavigationButton _barButtonItemStyle];
-[UINavigationButton _buttonItemStyle];
-[UINavigationButton _buttonTitleEdgeInsets];
-[UINavigationButton _canHandleStatusBarTouchAtLocation:];
-[UINavigationButton _createdByBarButtonItem];
-[UINavigationButton _customOrAccessibilityBackgroundImageForState:style:isMini:];
-[UINavigationButton _defaultTitleColorForState:isTintColor:];
-[UINavigationButton _defaultTitleShadowColorForState:];
-[UINavigationButton _defaultTitleShadowOffsetForState:];
-[UINavigationButton _enclosingBar];
-[UINavigationButton _externalDrawingStyleForState:];
-[UINavigationButton _externalTitleColorForState:isTintColor:];
-[UINavigationButton _externalUnfocusedBorderColor];
-[UINavigationButton _fontScaleAdjustment];
-[UINavigationButton _hasBaselineAlignedAbsoluteVerticalPosition:withinNavBar:forSize:];
-[UINavigationButton _isCarPlaySystemTypeButton];
-[UINavigationButton _isExternalRoundedRectButton];
-[UINavigationButton _isFontScaleInvalid];
-[UINavigationButton _pathImageEdgeInsets];
-[UINavigationButton _pathTitleEdgeInsets];
-[UINavigationButton _sendSetNeedsLayoutToSuperviewOnTitleAnimationCompletionIfNecessary];
-[UINavigationButton _setAccessibilityBackgroundTintColor:];
-[UINavigationButton _setBoundsAdjustment:];
-[UINavigationButton _setButtonItemStyle:];
-[UINavigationButton _setCreatedByBarButtonItem:];
-[UINavigationButton _setEnclosingBar:];
-[UINavigationButton _setFontScaleAdjustment:];
-[UINavigationButton _setFontScaleInvalid:];
-[UINavigationButton _setFrame:deferLayout:];
-[UINavigationButton _setStylesForSizingTitles:];
-[UINavigationButton _setTitleFrozen:];
-[UINavigationButton _setWantsBlendModeForAccessibilityBackgrounds:];
-[UINavigationButton _showsAccessibilityBackgroundWhenEnabled];
-[UINavigationButton _stylesForSizingTitles];
-[UINavigationButton _titlePositionAdjustmentForBarMetrics:];
-[UINavigationButton _uinavigationbar_prepareToAppearInNavigationItem:onLeft:];
-[UINavigationButton _updateShadowOffsetWithAttributes:forState:];
-[UINavigationButton _updateTitleColorsForState:];
-[UINavigationButton _visualStyleForMetrics:];
-[UINavigationButton _wantsBlendModeForAccessibilityBackgrounds];
-[UINavigationButton contentsEqualTo:withStyle:];
-[UINavigationButton controlSize];
-[UINavigationButton initWithImage:style:];
-[UINavigationButton initWithImage:width:style:];
-[UINavigationButton initWithImage:width:style:applyBezel:forBarStyle:buttonItemStyle:];
-[UINavigationButton initWithTitle:possibleTitles:style:];
-[UINavigationButton initWithTitle:style:];
-[UINavigationButton initWithValue:width:style:barStyle:possibleTitles:possibleSystemItems:tintColor:applyBezel:forButtonItemStyle:];
-[UINavigationButton initWithValue:width:style:barStyle:possibleTitles:tintColor:];
-[UINavigationButton originatingButtonItem];
-[UINavigationButton originatingNavigationItem];
-[UINavigationButton setNavigationBarTintColor:];
-[UINavigationButton setOriginatingButtonItem:];
-[UINavigationButton setOriginatingNavigationItem:];
```
