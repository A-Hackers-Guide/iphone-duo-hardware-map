# `UITabBarButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UISpringLoadedInteractionSupporting`, `_UITabBarButton`
- 29 instance variables, 23 properties, 110 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hitRect;
@"UITabBarSwappableImageView" _imageView;
@"UIVisualEffectView" _vibrancyEffectView;
@"UITabBarButtonLabel" _label;
@"_UIBadgeView" _badge;
@"UIImageView" _selectedIndicator;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _imageInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _imageLandscapeInsets;
@"UIImage" _customSelectedIndicatorImage;
{UIOffset="horizontal"d"vertical"d} _labelOffset;
@"NSMutableDictionary" _buttonTintColorsForState;
@"NSMutableDictionary" _contentTintColorsForState;
@"UIColor" _defaultUnselectedLabelTintColor;
@"UIColor" _badgeColor;
@"NSMutableDictionary" _badgeTextAttributesForState;
{UIOffset="horizontal"d"vertical"d} _badgeOffset;
@"UIView" _highContrastFocusIndicator;
B _selected;
B _accessibilityButtonShapesEnabled;
B _accessibilityHighContractFocusIndicatorEnabled;
B _accessibilityGrayStatusEnabled;
B _showsHighlightedState;
@"UIView" _focusView;
# _appearanceGuideClass;
q _layoutStyle;
@"_UITabBarItemData" _itemAppearanceData;
@"UIVibrancyEffect" _itemVibrantEffect;
@"UITabBar" _tabBar;
@"NSArray" _carplayConstraints;
```

## Properties

```
@property (TB,N,GisSpringLoaded) springLoaded;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",&,N,V_carplayConstraints) carplayConstraints;
@property (T@"UIView",R,N,V_focusView) focusView;
@property (TB,R,N,GisDefaultTVLayout) _defaultTVLayout;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (T@"_UITabBarItemData",&,N,V_itemAppearanceData) itemAppearanceData;
@property (T@"UIVibrancyEffect",&,N,V_itemVibrantEffect) itemVibrantEffect;
@property (T@"UITabBar",R,W,N,V_tabBar) tabBar;
@property (T#,&,N,S_setAppearanceGuideClass:,V_appearanceGuideClass) _appearanceGuideClass;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _contentRect;
@property (T@"UIColor",R,N) _defaultUnselectedLabelTintColor;
@property (TB,N,G_isSelected,S_setSelected:) _selected;
@property (T@"UIColor",&,N,G_unselectedTintColor,S_setUnselectedTintColor:) unselectedTintColor;
@property (TB,N,S_setShowsHighlightedState:,V_showsHighlightedState) _showsHighlightedState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisSpringLoaded) springLoaded;
```

## Class methods

```
+[UITabBarButton _defaultLabelColor];
```

## Instance methods

```
-[UITabBarButton setLayoutStyle:];
-[UITabBarButton setSpringLoaded:];
-[UITabBarButton _isEligibleForFocusInteraction];
-[UITabBarButton layoutStyle];
-[UITabBarButton isSpringLoaded];
-[UITabBarButton badgeTextAttributesForState:];
-[UITabBarButton _applyTabBarButtonAppearanceStorage:withTaggedSelectors:];
-[UITabBarButton _setSelected:];
-[UITabBarButton badgeTitlePositionAdjustmentForState:];
-[UITabBarButton pointInside:forEvent:];
-[UITabBarButton _setAppearanceGuideClass:];
-[UITabBarButton _systemDefaultFocusGroupIdentifier];
-[UITabBarButton _responderSelectionRectForWindow:];
-[UITabBarButton _UIAppearance_setTitleTextAttributes:forState:];
-[UITabBarButton _appearanceGuideClass];
-[UITabBarButton _setTitleTextAttributes:forState:];
-[UITabBarButton iconColorForState:];
-[UITabBarButton didUpdateFocusInContext:withAnimationCoordinator:];
-[UITabBarButton _UIAppearance_setBadgeTextAttributes:forState:];
-[UITabBarButton pressesCancelled:withEvent:];
-[UITabBarButton _didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UITabBarButton pressesEnded:withEvent:];
-[UITabBarButton dealloc];
-[UITabBarButton layoutSubviews];
-[UITabBarButton _defaultFocusRegionFrame];
-[UITabBarButton _info];
-[UITabBarButton titlePositionAdjustmentForState:];
-[UITabBarButton _showSelectedIndicator:changeSelection:];
-[UITabBarButton _accessibilityButtonShapesDidChangeNotification:];
-[UITabBarButton _UIAppearance_setTitlePositionAdjustment:];
-[UITabBarButton canBecomeFocused];
-[UITabBarButton setSemanticContentAttribute:];
-[UITabBarButton pressesBegan:withEvent:];
-[UITabBarButton pressesChanged:withEvent:];
-[UITabBarButton sizeThatFits:];
-[UITabBarButton _setTitlePositionAdjustment:];
-[UITabBarButton _setBadgeColor:];
-[UITabBarButton tabBar];
-[UITabBarButton setHighlighted:];
-[UITabBarButton badgePositionAdjustmentForState:];
-[UITabBarButton _selectedIndicatorImage];
-[UITabBarButton setEnabled:];
-[UITabBarButton titleTextAttributesForState:];
-[UITabBarButton _UIAppearance_setBadgeColor:];
-[UITabBarButton _showsHighlightedState];
-[UITabBarButton _setUnselectedTintColor:];
-[UITabBarButton _reducedTransparencyDidChange:];
-[UITabBarButton badgeBackgroundColorForState:];
-[UITabBarButton traitCollectionDidChange:];
-[UITabBarButton _setShowsHighlightedState:];
-[UITabBarButton _setBadgeValue:];
-[UITabBarButton pointInside:withEvent:];
-[UITabBarButton _unselectedTintColor];
-[UITabBarButton shouldUpdateFocusInContext:];
-[UITabBarButton _setBadgeTextAttributes:forState:];
-[UITabBarButton _setBadgeOffset:];
-[UITabBarButton _isSelected];
-[UITabBarButton setImage:];
-[UITabBarButton _horizontalLayout_sizeThatFits:];
-[UITabBarButton _tabBar];
-[UITabBarButton defaultCompositingModeForState:];
-[UITabBarButton labelShouldUseVibrancyForState:];
-[UITabBarButton _accessibilityGrayStatusDidChangeNotification:];
-[UITabBarButton _accessibilityHighContractFocusIndicatorDidChangeNotification:];
-[UITabBarButton _appleTV_layoutSubviews];
-[UITabBarButton _appleTV_sizeThatFits:];
-[UITabBarButton _areTabBarButtonAccessibilityButtonShapesEnabled];
-[UITabBarButton _buttonTintColorForState:];
-[UITabBarButton _contentRect];
-[UITabBarButton _contentTintColorForState:];
-[UITabBarButton _currentItemState];
-[UITabBarButton _defaultUnselectedLabelTintColor];
-[UITabBarButton _focusTouchSensitivityStyle];
-[UITabBarButton _ios_layoutSubviews];
-[UITabBarButton _positionBadge];
-[UITabBarButton _positionBadgeAfterChangesIfNecessary:];
-[UITabBarButton _removeCarplayConstraints];
-[UITabBarButton _responderSelectionRect];
-[UITabBarButton _selectedIndicatorView];
-[UITabBarButton _sendFocusAction:];
-[UITabBarButton _setButtonTintColor:forState:];
-[UITabBarButton _setContentTintColor:forState:];
-[UITabBarButton _setCustomSelectedIndicatorImage:];
-[UITabBarButton _setTabBarHitRect:];
-[UITabBarButton _setupCarplayConstraints];
-[UITabBarButton _setupSymbolConfigurationsForIdiom:];
-[UITabBarButton _tabBarHitRect];
-[UITabBarButton _titlePositionAdjustment];
-[UITabBarButton _updateAfterTraitCollectionOrAccessibilityDidChangeTV];
-[UITabBarButton _updateBadgeAppearanceAndLayoutNow:];
-[UITabBarButton _updateSelectedIndicatorFrame];
-[UITabBarButton _updateSelectedIndicatorView];
-[UITabBarButton _updateToMatchCurrentState];
-[UITabBarButton _updateVibrancyEffectView];
-[UITabBarButton carplayConstraints];
-[UITabBarButton defaultAlphaForState:];
-[UITabBarButton defaultColorForState:];
-[UITabBarButton focusView];
-[UITabBarButton iconShouldUseVibrancyForState:];
-[UITabBarButton initWithImage:landscapeImage:selectedImage:landscapeSelectedImage:label:withInsets:landscapeInsets:tabBar:];
-[UITabBarButton initWithImage:selectedImage:label:withInsets:tabBar:];
-[UITabBarButton isDefaultColor:forState:];
-[UITabBarButton isDefaultTVLayout];
-[UITabBarButton itemAppearanceData];
-[UITabBarButton itemVibrantEffect];
-[UITabBarButton pointMostlyInside:withEvent:];
-[UITabBarButton setCarplayConstraints:];
-[UITabBarButton setItemAppearanceData:];
-[UITabBarButton setItemVibrantEffect:];
-[UITabBarButton set_info:];
```
