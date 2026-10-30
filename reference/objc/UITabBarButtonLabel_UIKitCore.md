# `UITabBarButtonLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILabel`
- 10 instance variables, 3 properties, 32 instance methods, 1 class methods

## Instance variables

```
d _boundsWidth;
@"_UITabBarItemAppearanceStorage" _appearanceStorage;
B _isSelected;
B _isHighlighted;
B _hasSeenIdiom;
@"NSNumber" _previousKernAttributeForSizing;
@"NSAttributedString" _previousAttributedTextForSizingExcludingKern;
# _appearanceGuideClass;
@"UIColor" _unselectedTintColor;
@"UITabBarButton" _tabBarButton;
```

## Properties

```
@property (T#,&,N,S_setAppearanceGuideClass:,V_appearanceGuideClass) _appearanceGuideClass;
@property (T@"UIColor",&,N,V_unselectedTintColor) unselectedTintColor;
@property (T@"UITabBarButton",W,N,V_tabBarButton) tabBarButton;
```

## Class methods

```
+[UITabBarButtonLabel _fontPointSizeForIdiom:];
```

## Instance methods

```
-[UITabBarButtonLabel _applyTabBarButtonAppearanceStorage:withTaggedSelectors:];
-[UITabBarButtonLabel setSelected:];
-[UITabBarButtonLabel _setAppearanceGuideClass:];
-[UITabBarButtonLabel _titleTextAttributesForState:];
-[UITabBarButtonLabel _UIAppearance_setTitleTextAttributes:forState:];
-[UITabBarButtonLabel _appearanceGuideClass];
-[UITabBarButtonLabel _legacyApperance_updateTextColorsForState];
-[UITabBarButtonLabel _setTitleTextAttributes:forState:];
-[UITabBarButtonLabel _UIAppearance_setBadgeTextAttributes:forState:];
-[UITabBarButtonLabel _didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UITabBarButtonLabel _updateLabelsVibrancy];
-[UITabBarButtonLabel _fontForIdiom:];
-[UITabBarButtonLabel _updateForFontChangeWithIdiom:];
-[UITabBarButtonLabel setUnselectedTintColor:];
-[UITabBarButtonLabel _shouldCeilSizeToViewScale];
-[UITabBarButtonLabel _UIAppearance_setTitlePositionAdjustment:];
-[UITabBarButtonLabel setTabBarButton:];
-[UITabBarButtonLabel updateTextColorsForState];
-[UITabBarButtonLabel tabBarButton];
-[UITabBarButtonLabel _setTitlePositionAdjustment:];
-[UITabBarButtonLabel tintColorDidChange];
-[UITabBarButtonLabel _setBadgeColor:];
-[UITabBarButtonLabel setHighlighted:];
-[UITabBarButtonLabel initWithTabBarDisplayStyle:];
-[UITabBarButtonLabel _UIAppearance_setBadgeColor:];
-[UITabBarButtonLabel traitCollectionDidChange:];
-[UITabBarButtonLabel unselectedTintColor];
-[UITabBarButtonLabel _shouldAnimatePropertyWithKey:];
-[UITabBarButtonLabel initWithFrame:];
-[UITabBarButtonLabel _setBadgeTextAttributes:forState:];
-[UITabBarButtonLabel resizeToFitWidth:];
-[UITabBarButtonLabel _fontForIdiom:forTabBarDisplayStyle:];
```
