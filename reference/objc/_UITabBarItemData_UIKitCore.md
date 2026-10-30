# `_UITabBarItemData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarAppearanceData`
- 9 instance variables, 1 properties, 34 instance methods, 2 class methods

## Instance variables

```
q _style;
[5@"NSDictionary"] _titleTextAttributes;
[5@"NSDictionary"] _badgeTextAttributes;
[5@"UIColor"] _iconColor;
[5@"UIColor"] _badgeBackgroundColor;
[5{UIOffset="horizontal"d"vertical"d}] _titlePositionAdjustment;
[5{UIOffset="horizontal"d"vertical"d}] _badgePositionAdjustment;
[5{UIOffset="horizontal"d"vertical"d}] _badgeTitlePositionAdjustment;
[5{?="hasUserTitleFont"b1"hasUserTitleColor"b1"hasUserTitlePosition"b1"hasUserIconColor"b1"hasUserBadgePosition"b1"hasUserBadgeBackgroundColor"b1"hasUserBadgeTitleFont"b1"hasUserBadgeTitleColor"b1"hasUserBadgeTitlePosition"b1}] _stateFlags;
```

## Properties

```
@property (T@"UIImageSymbolConfiguration",R,N) preferredSymbolConfiguration;
```

## Class methods

```
+[_UITabBarItemData standardItemDataForStyle:];
+[_UITabBarItemData decodeFromCoder:prefix:];
```

## Instance methods

```
-[_UITabBarItemData describeInto:];
-[_UITabBarItemData hashInto:];
-[_UITabBarItemData badgeTextAttributesForState:];
-[_UITabBarItemData badgeTitlePositionAdjustmentForState:];
-[_UITabBarItemData setBadgePositionAdjustment:forState:];
-[_UITabBarItemData setBadgeTextAttributes:forState:];
-[_UITabBarItemData preferredSymbolConfiguration];
-[_UITabBarItemData _fallbackBadgeTitleFontForState:compatibleWithTraitCollection:];
-[_UITabBarItemData _decodeTitleTextAttributesFromCoder:prefix:];
-[_UITabBarItemData _decodeBadgeTextAttributesFromCoder:prefix:];
-[_UITabBarItemData _fallbackBadgeTitleColorForState:];
-[_UITabBarItemData badgeTextAttributesForState:compatibleWithTraitCollection:];
-[_UITabBarItemData encodeToCoder:prefix:];
-[_UITabBarItemData iconColorForState:];
-[_UITabBarItemData setBadgeTitlePositionAdjustment:forState:];
-[_UITabBarItemData _decodeBadgeTitlePositionAdjustmentsFromCoder:prefix:];
-[_UITabBarItemData titlePositionAdjustmentForState:];
-[_UITabBarItemData setIconColor:forState:];
-[_UITabBarItemData setTitleTextAttributes:forState:];
-[_UITabBarItemData titleTextAttributesSpecifyColorForState:];
-[_UITabBarItemData _decodeIconColorFromCoder:prefix:];
-[_UITabBarItemData badgePositionAdjustmentForState:];
-[_UITabBarItemData titleTextAttributesForState:compatibleWithTraitCollection:];
-[_UITabBarItemData titleTextAttributesForState:];
-[_UITabBarItemData _decodeTitlePositionAdjustmentsFromCoder:prefix:];
-[_UITabBarItemData _decodeBadgePositionAdjustmentsFromCoder:prefix:];
-[_UITabBarItemData badgeBackgroundColorForState:];
-[_UITabBarItemData _decodeBadgeBackgroundColorFromCoder:prefix:];
-[_UITabBarItemData _fallbackTitleFontForState:compatibleWithTraitCollection:];
-[_UITabBarItemData setTitlePositionAdjustment:forState:];
-[_UITabBarItemData checkEqualTo:];
-[_UITabBarItemData replicate];
-[_UITabBarItemData _fallbackTitleColorForState:];
-[_UITabBarItemData setBadgeBackgroundColor:forState:];
```
