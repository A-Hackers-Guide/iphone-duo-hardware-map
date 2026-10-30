# `UITabBarAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIBarAppearance`
- 5 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"_UITabBarLayoutData" _layoutData;
@"UITabBarItemAppearance" _carPlayAppearance;
@"UITabBarItemAppearance" _stackedLayoutAppearance;
@"UITabBarItemAppearance" _inlineLayoutAppearance;
@"UITabBarItemAppearance" _compactInlineLayoutAppearance;
```

## Properties

```
@property (T@"UIVibrancyEffect",C,D,N,S_setSelectedItemVibrancyEffect:) _selectedItemVibrancyEffect;
@property (T@"UITabBarItemAppearance",C,N,V_stackedLayoutAppearance) stackedLayoutAppearance;
@property (T@"UITabBarItemAppearance",C,N,V_inlineLayoutAppearance) inlineLayoutAppearance;
@property (T@"UITabBarItemAppearance",C,N,V_compactInlineLayoutAppearance) compactInlineLayoutAppearance;
@property (T@"UIColor",C,N) selectionIndicatorTintColor;
@property (T@"UIImage",&,N) selectionIndicatorImage;
@property (Tq,N) stackedItemPositioning;
@property (Td,N) stackedItemWidth;
@property (Td,N) stackedItemSpacing;
```

## Class methods

```
+[UITabBarAppearance supportsSecureCoding];
```

## Instance methods

```
-[UITabBarAppearance selectionIndicatorImage];
-[UITabBarAppearance setSelectionIndicatorImage:];
-[UITabBarAppearance setStackedItemPositioning:];
-[UITabBarAppearance setInlineLayoutAppearance:];
-[UITabBarAppearance _stackedTabButtonAppearanceData];
-[UITabBarAppearance setCompactInlineLayoutAppearance:];
-[UITabBarAppearance stackedLayoutAppearance];
-[UITabBarAppearance stackedItemWidth];
-[UITabBarAppearance setStackedItemWidth:];
-[UITabBarAppearance setStackedItemSpacing:];
-[UITabBarAppearance _checkEqualTo:];
-[UITabBarAppearance inlineLayoutAppearance];
-[UITabBarAppearance stackedItemSpacing];
-[UITabBarAppearance _dataForItemStyle:];
-[UITabBarAppearance _describeInto:];
-[UITabBarAppearance _decodeFromCoder:];
-[UITabBarAppearance setStackedLayoutAppearance:];
-[UITabBarAppearance _setupDefaults];
-[UITabBarAppearance stackedItemPositioning];
-[UITabBarAppearance _inlineTabButtonAppearanceData];
-[UITabBarAppearance encodeWithCoder:];
-[UITabBarAppearance _carPlayTabButtonAppearanceData];
-[UITabBarAppearance _tabLayoutAppearanceData];
-[UITabBarAppearance selectionIndicatorTintColor];
-[UITabBarAppearance _completeInit];
-[UITabBarAppearance setSelectionIndicatorTintColor:];
-[UITabBarAppearance _hashInto:];
-[UITabBarAppearance _compactInlineTabButtonAppearanceData];
-[UITabBarAppearance compactInlineLayoutAppearance];
-[UITabBarAppearance _copyFromAppearance:];
-[UITabBarAppearance _tabBarItemDataChanged:];
```
