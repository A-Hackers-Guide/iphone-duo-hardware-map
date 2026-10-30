# `_UINavigationItemButtonView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationItemView`
- Protocols: `UIGestureRecognizerDelegate`
- 9 instance variables, 8 properties, 76 instance methods, 0 class methods

## Instance variables

```
q _style;
B _pressed;
@"_UIBarButtonItemAppearanceStorage" _appearanceStorage;
B _customBackgroundImageChangedToOrFromNil;
@"UIImageView" _backgroundImageView;
@"UIImageView" _imageView;
B _wantsBlendModeForAccessibilityBackgrounds;
Q _abbreviatedTitleIndex;
@"UIColor" _accessibilityBackgroundTintColor;
```

## Properties

```
@property (TQ,N,S_setAbbreviatedTitleIndex:,V_abbreviatedTitleIndex) _abbreviatedTitleIndex;
@property (TB,N,S_setWantsBlendModeForAccessibilityBackgrounds:,V_wantsBlendModeForAccessibilityBackgrounds) _wantsBlendModeForAccessibilityBackgrounds;
@property (T@"UIColor",&,N,S_setAccessibilityBackgroundTintColor:,V_accessibilityBackgroundTintColor) _accessibilityBackgroundTintColor;
@property (T@"UIColor",&,N,S_setTintColor:) _tintColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationItemButtonView _tintColor];
-[_UINavigationItemButtonView _appearanceStorage];
-[_UINavigationItemButtonView _UIAppearance_setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView imageSize];
-[_UINavigationItemButtonView didMoveToWindow];
-[_UINavigationItemButtonView _UIAppearance_setBackButtonBackgroundImage:forState:barMetrics:];
-[_UINavigationItemButtonView _titleTextAttributesForState:];
-[_UINavigationItemButtonView _UIAppearance_setTitleTextAttributes:forState:];
-[_UINavigationItemButtonView _setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView _setTintColor:];
-[_UINavigationItemButtonView gestureRecognizer:shouldReceiveTouch:];
-[_UINavigationItemButtonView _appearanceGuideClass];
-[_UINavigationItemButtonView _setTitleTextAttributes:forState:];
-[_UINavigationItemButtonView setStyle:animated:];
-[_UINavigationItemButtonView didUpdateFocusInContext:withAnimationCoordinator:];
-[_UINavigationItemButtonView alignmentRectInsets];
-[_UINavigationItemButtonView _setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView _didChangeFromIdiom:onScreen:traverseHierarchy:];
-[_UINavigationItemButtonView _accessibilityButtonShapesParametersDidChange];
-[_UINavigationItemButtonView _UIAppearance_setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView _UIAppearance_setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView dealloc];
-[_UINavigationItemButtonView _UIAppearance_setTintColor:];
-[_UINavigationItemButtonView _UIAppearance_setBackgroundImage:forState:style:barMetrics:];
-[_UINavigationItemButtonView _UIAppearance_setTitlePositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView layoutSubviews];
-[_UINavigationItemButtonView _setBackgroundImage:forState:barMetrics:];
-[_UINavigationItemButtonView _accessibilityButtonShapesDidChangeNotification:];
-[_UINavigationItemButtonView _UIAppearance_setBackgroundImage:forState:barMetrics:];
-[_UINavigationItemButtonView _setBackButtonBackgroundImage:forState:barMetrics:];
-[_UINavigationItemButtonView canBecomeFocused];
-[_UINavigationItemButtonView setStyle:];
-[_UINavigationItemButtonView _setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView _setTitlePositionAdjustment:forBarMetrics:];
-[_UINavigationItemButtonView sizeThatFits:];
-[_UINavigationItemButtonView tintColorDidChange];
-[_UINavigationItemButtonView _setBackgroundImage:forState:style:barMetrics:];
-[_UINavigationItemButtonView title];
-[_UINavigationItemButtonView pressed];
-[_UINavigationItemButtonView traitCollectionDidChange:];
-[_UINavigationItemButtonView backgroundImageView];
-[_UINavigationItemButtonView image];
-[_UINavigationItemButtonView pointInside:withEvent:];
-[_UINavigationItemButtonView initWithFrame:];
-[_UINavigationItemButtonView setPressed:];
-[_UINavigationItemButtonView _wantsAccessibilityButtonShapes];
-[_UINavigationItemButtonView _abbreviatedTitleIndex];
-[_UINavigationItemButtonView _accessibilityBackgroundTintColor];
-[_UINavigationItemButtonView _applyBarButtonAppearanceStorage:withTaggedSelectors:];
-[_UINavigationItemButtonView _backButtonBackgroundImageForState:barMetrics:];
-[_UINavigationItemButtonView _backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:];
-[_UINavigationItemButtonView _backButtonTitlePositionAdjustmentForBarMetrics:];
-[_UINavigationItemButtonView _backSelectGestureChanged:];
-[_UINavigationItemButtonView _backgroundVerticalPositionAdjustmentForBarMetrics:];
-[_UINavigationItemButtonView _currentCustomBackgroundNeedsDarkening:];
-[_UINavigationItemButtonView _currentTextColorForBarStyle:];
-[_UINavigationItemButtonView _currentTextShadowColorForBarStyle:];
-[_UINavigationItemButtonView _currentTextShadowOffsetForBarStyle:];
-[_UINavigationItemButtonView _defaultFont];
-[_UINavigationItemButtonView _installBackSelectGestureRecognizer];
-[_UINavigationItemButtonView _resetRenderingModesForAccessibilityBackgrounds];
-[_UINavigationItemButtonView _setAbbreviatedTitleIndex:];
-[_UINavigationItemButtonView _setAccessibilityBackgroundTintColor:];
-[_UINavigationItemButtonView _setWantsBlendModeForAccessibilityBackgrounds:];
-[_UINavigationItemButtonView _showsAccessibilityBackgroundWhenEnabled];
-[_UINavigationItemButtonView _suppressesBackIndicatorView];
-[_UINavigationItemButtonView _titleYAdjustmentCustomization];
-[_UINavigationItemButtonView _uninstallBackSelectGestureRecognizer];
-[_UINavigationItemButtonView _updateBackSelectGestureRecognizer];
-[_UINavigationItemButtonView _useSilverLookForBarStyle:];
-[_UINavigationItemButtonView _wantsBlendModeForAccessibilityBackgrounds];
-[_UINavigationItemButtonView backIndicatorViewHasRespondedToCustomBackgroundImageChange];
-[_UINavigationItemButtonView customBackgroundImageChangedToOrFromNil];
-[_UINavigationItemButtonView hasCustomBackgroundImage];
-[_UINavigationItemButtonView initWithNavigationItem:];
-[_UINavigationItemButtonView setPressed:initialPress:];
```
