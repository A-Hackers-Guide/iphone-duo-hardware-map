# `UITabBarItemStateAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UITabBarItemAppearance" _owner;
q _state;
@"_UITabBarItemData" _data;
@"NSArray" _itemEffects;
```

## Properties

```
@property (T@"_UITabBarItemData",&,N,S_setData:,V_data) _data;
@property (T@"NSArray",C,N,V_itemEffects) itemEffects;
@property (T@"NSDictionary",C,N) titleTextAttributes;
@property (T{UIOffset=dd},N) titlePositionAdjustment;
@property (T@"UIColor",C,N) iconColor;
@property (T{UIOffset=dd},N) badgePositionAdjustment;
@property (T@"UIColor",C,N) badgeBackgroundColor;
@property (T@"NSDictionary",C,N) badgeTextAttributes;
@property (T{UIOffset=dd},N) badgeTitlePositionAdjustment;
```

## Instance methods

```
-[UITabBarItemStateAppearance setTitlePositionAdjustment:];
-[UITabBarItemStateAppearance init];
-[UITabBarItemStateAppearance badgeBackgroundColor];
-[UITabBarItemStateAppearance _setData:];
-[UITabBarItemStateAppearance _data];
-[UITabBarItemStateAppearance setTitleTextAttributes:];
-[UITabBarItemStateAppearance titleTextAttributes];
-[UITabBarItemStateAppearance titlePositionAdjustment];
-[UITabBarItemStateAppearance _writeToStorage:];
-[UITabBarItemStateAppearance setItemEffects:];
-[UITabBarItemStateAppearance _clearOwner];
-[UITabBarItemStateAppearance _initWithOwner:data:state:];
-[UITabBarItemStateAppearance badgePositionAdjustment];
-[UITabBarItemStateAppearance badgeTextAttributes];
-[UITabBarItemStateAppearance badgeTitlePositionAdjustment];
-[UITabBarItemStateAppearance iconColor];
-[UITabBarItemStateAppearance itemEffects];
-[UITabBarItemStateAppearance setBadgeBackgroundColor:];
-[UITabBarItemStateAppearance setBadgePositionAdjustment:];
-[UITabBarItemStateAppearance setBadgeTextAttributes:];
-[UITabBarItemStateAppearance setBadgeTitlePositionAdjustment:];
-[UITabBarItemStateAppearance setIconColor:];
```
