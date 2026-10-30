# `UIToolbarButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 18 instance variables, 4 properties, 79 instance methods, 3 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hitRect;
@"_UIToolbarNavigationButton" _info;
@"UILabel" _label;
q _barStyle;
q _style;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _glowAdjust;
B _onState;
B _barHeight;
B _bezel;
d _minimumWidth;
d _maximumWidth;
d _labelHeight;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _infoInsets;
@"UIColor" _toolbarTintColor;
@ _appearanceStorage;
B _isInTopBar;
# _appearanceGuideClass;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __additionalSelectionInsets;
```

## Properties

```
@property (T@"UIColor",&,N,S_setTintColor:) _tintColor;
@property (T#,N,S_setAppearanceGuideClass:,V_appearanceGuideClass) _appearanceGuideClass;
@property (TB,N,S_setCreatedByBarButtonItem:) _createdByBarButtonItem;
@property (T{UIEdgeInsets=dddd},N,S_setAdditionalSelectionInsets:,V__additionalSelectionInsets) _additionalSelectionInsets;
```

## Class methods

```
+[UIToolbarButton _defaultLabelColor];
+[UIToolbarButton _defaultLabelFont];
+[UIToolbarButton defaultButtonFont];
```

## Instance methods

```
-[UIToolbarButton _controlEventsForActionTriggered];
-[UIToolbarButton _tintColor];
-[UIToolbarButton _UIAppearance_setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UIToolbarButton pointInside:forEvent:];
-[UIToolbarButton _setAppearanceGuideClass:];
-[UIToolbarButton _UIAppearance_setBackButtonBackgroundImage:forState:barMetrics:];
-[UIToolbarButton _titleTextAttributesForState:];
-[UIToolbarButton _UIAppearance_setTitleTextAttributes:forState:];
-[UIToolbarButton _setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UIToolbarButton _setAdditionalSelectionInsets:];
-[UIToolbarButton _setTintColor:];
-[UIToolbarButton _appearanceGuideClass];
-[UIToolbarButton _setTitleTextAttributes:forState:];
-[UIToolbarButton alignmentRectInsets];
-[UIToolbarButton _setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[UIToolbarButton _UIAppearance_setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UIToolbarButton _UIAppearance_setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[UIToolbarButton dealloc];
-[UIToolbarButton _UIAppearance_setTintColor:];
-[UIToolbarButton _UIAppearance_setBackgroundImage:forState:style:barMetrics:];
-[UIToolbarButton _UIAppearance_setTitlePositionAdjustment:forBarMetrics:];
-[UIToolbarButton layoutSubviews];
-[UIToolbarButton hitTest:withEvent:];
-[UIToolbarButton _info];
-[UIToolbarButton _setBackgroundImage:forState:barMetrics:];
-[UIToolbarButton _UIAppearance_setBackgroundImage:forState:barMetrics:];
-[UIToolbarButton _setBackButtonBackgroundImage:forState:barMetrics:];
-[UIToolbarButton _setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[UIToolbarButton _setTitlePositionAdjustment:forBarMetrics:];
-[UIToolbarButton sizeThatFits:];
-[UIToolbarButton gestureRecognizerShouldBegin:];
-[UIToolbarButton setHighlighted:];
-[UIToolbarButton _setBackgroundImage:forState:style:barMetrics:];
-[UIToolbarButton setEnabled:];
-[UIToolbarButton setBarStyle:];
-[UIToolbarButton _additionalSelectionInsets];
-[UIToolbarButton pointInside:withEvent:];
-[UIToolbarButton setImage:];
-[UIToolbarButton _wantsAccessibilityButtonShapes];
-[UIToolbarButton _accessibilityShouldActivateOnHUDLift];
-[UIToolbarButton _adjustPushButtonForMiniBar:isChangingBarHeight:];
-[UIToolbarButton _adjustToolbarButtonInfo];
-[UIToolbarButton _adjustToolbarButtonInfoTintColorHasChanged:];
-[UIToolbarButton _applyBarButtonAppearanceStorage:withTaggedSelectors:];
-[UIToolbarButton _backgroundImageForState:barMetrics:];
-[UIToolbarButton _backgroundVerticalPositionAdjustmentForBarMetrics:];
-[UIToolbarButton _buttonBarHitRect];
-[UIToolbarButton _canGetPadding];
-[UIToolbarButton _canHandleStatusBarTouchAtLocation:];
-[UIToolbarButton _createdByBarButtonItem];
-[UIToolbarButton _customOrAccessibilityBackgroundImageForState:style:isMini:];
-[UIToolbarButton _defaultTitleShadowOffsetForState:];
-[UIToolbarButton _infoIsButton];
-[UIToolbarButton _isBordered];
-[UIToolbarButton _isBorderedOtherThanAccessibility];
-[UIToolbarButton _paddingForLeft:];
-[UIToolbarButton _setBarHeight:];
-[UIToolbarButton _setButtonBarHitRect:];
-[UIToolbarButton _setCreatedByBarButtonItem:];
-[UIToolbarButton _setInTopBar:];
-[UIToolbarButton _setInfoExtremityWidth:isMin:];
-[UIToolbarButton _setInfoFlexibleWidth:];
-[UIToolbarButton _setInfoWidth:];
-[UIToolbarButton _setLastHighlightSuccessful:];
-[UIToolbarButton _setPressed:];
-[UIToolbarButton _setTouchHasHighlighted:];
-[UIToolbarButton _setWantsBlendModeForAccessibilityBackgrounds:];
-[UIToolbarButton _shouldApplyPadding];
-[UIToolbarButton _showsAccessibilityBackgroundWhenEnabled];
-[UIToolbarButton _sizeView:toPossibleTitles:pressedTitle:];
-[UIToolbarButton _titlePositionAdjustmentForBarMetrics:];
-[UIToolbarButton _updateInfoTextColorsForState:];
-[UIToolbarButton _updateShadowOffsetWithAttributes:forState:];
-[UIToolbarButton _useBarHeight];
-[UIToolbarButton hitTest:forEvent:];
-[UIToolbarButton initWithImage:pressedImage:label:labelHeight:withBarStyle:withStyle:withInsets:possibleTitles:possibleSystemItems:withToolbarTintColor:bezel:imageInsets:glowInsets:landscape:];
-[UIToolbarButton pointMostlyInside:withEvent:];
-[UIToolbarButton setToolbarTintColor:];
-[UIToolbarButton setUseSelectedImage:];
```
