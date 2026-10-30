# `UIStatusBarCarPlayDockAppItemButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- Protocols: `NSCopying`
- 8 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSLayoutConstraint" _heightConstraint;
@"NSLayoutConstraint" _widthConstraint;
B _active;
B _hasBadge;
@"NSString" _bundleIdentifier;
@"UIImageView" _iconImageView;
@"UIImageView" _iconHighlightImageView;
@"UIImageView" _badgeView;
```

## Properties

```
@property (TB,N,GisActive,V_active) active;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"UIImageView",&,N,V_iconImageView) iconImageView;
@property (T@"UIImageView",&,N,V_iconHighlightImageView) iconHighlightImageView;
@property (T@"UIImageView",&,N,V_badgeView) badgeView;
@property (TB,R,N) itemHasBundleIdentifier;
@property (TB,N,V_hasBadge) hasBadge;
```

## Instance methods

```
-[UIStatusBarCarPlayDockAppItemButton setHasBadge:];
-[UIStatusBarCarPlayDockAppItemButton charge];
-[UIStatusBarCarPlayDockAppItemButton didUpdateFocusInContext:withAnimationCoordinator:];
-[UIStatusBarCarPlayDockAppItemButton pressesCancelled:withEvent:];
-[UIStatusBarCarPlayDockAppItemButton pressesEnded:withEvent:];
-[UIStatusBarCarPlayDockAppItemButton badgeView];
-[UIStatusBarCarPlayDockAppItemButton hasBadge];
-[UIStatusBarCarPlayDockAppItemButton bundleIdentifier];
-[UIStatusBarCarPlayDockAppItemButton setActive:];
-[UIStatusBarCarPlayDockAppItemButton canBecomeFocused];
-[UIStatusBarCarPlayDockAppItemButton pressesBegan:withEvent:];
-[UIStatusBarCarPlayDockAppItemButton setCharge:];
-[UIStatusBarCarPlayDockAppItemButton setBadgeView:];
-[UIStatusBarCarPlayDockAppItemButton setBundleIdentifier:];
-[UIStatusBarCarPlayDockAppItemButton isActive];
-[UIStatusBarCarPlayDockAppItemButton copyWithZone:];
-[UIStatusBarCarPlayDockAppItemButton initWithFrame:];
-[UIStatusBarCarPlayDockAppItemButton iconImageView];
-[UIStatusBarCarPlayDockAppItemButton _buttonPressed:];
-[UIStatusBarCarPlayDockAppItemButton shouldShowBadge];
-[UIStatusBarCarPlayDockAppItemButton iconHighlightImageView];
-[UIStatusBarCarPlayDockAppItemButton itemHasBundleIdentifier];
-[UIStatusBarCarPlayDockAppItemButton setBadgeHidden:animated:];
-[UIStatusBarCarPlayDockAppItemButton setIconHighlightImageView:];
-[UIStatusBarCarPlayDockAppItemButton setIconImageView:];
```
