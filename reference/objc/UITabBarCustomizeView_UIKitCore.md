# `UITabBarCustomizeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 17 instance variables, 2 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UITabBar" _tabBar;
@"NSMutableArray" _proxies;
@"NSMutableArray" _fixedItems;
@"UITabBarItemProxy" _draggingProxy;
@"UITabBarItem" _draggingItem;
@"UISnapshotView" _dragImage;
@"UIImageView" _replacementGlow;
@"UITabBarItem" _replaceItem;
@"UILabel" _titleLabel;
{CGPoint="x"d"y"d} _startPoint;
q _itemsInRowCount;
d _gridOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _firstItemRect;
@"UITabBarItem" _selectedBeforeItem;
B _isBeingDismissed;
@"NSArray" _availableItems;
@"UINavigationBar" _navigationBar;
```

## Properties

```
@property (T@"NSArray",&,N,V_availableItems) availableItems;
@property (T@"UINavigationBar",&,N,V_navigationBar) navigationBar;
```

## Instance methods

```
-[UITabBarCustomizeView titleLabelFont];
-[UITabBarCustomizeView touchesEnded:withEvent:];
-[UITabBarCustomizeView _barMetrics];
-[UITabBarCustomizeView touchesCancelled:withEvent:];
-[UITabBarCustomizeView navigationBar];
-[UITabBarCustomizeView layoutSubviews];
-[UITabBarCustomizeView touchesBegan:withEvent:];
-[UITabBarCustomizeView touchesMoved:withEvent:];
-[UITabBarCustomizeView setNavigationBar:];
-[UITabBarCustomizeView initWithFrame:];
-[UITabBarCustomizeView adjustDragImageWithTouches:withEvent:];
-[UITabBarCustomizeView availableItems];
-[UITabBarCustomizeView itemInTabBarWithTouches:withEvent:];
-[UITabBarCustomizeView setAvailableItems:];
-[UITabBarCustomizeView setIsBeingDismissed];
-[UITabBarCustomizeView setTabBar:currentItems:availableItems:];
-[UITabBarCustomizeView tabBarTouchesBegan:withEvent:];
-[UITabBarCustomizeView tabBarTouchesCancelled:withEvent:];
-[UITabBarCustomizeView tabBarTouchesEnded:withEvent:];
-[UITabBarCustomizeView tabBarTouchesMoved:withEvent:];
-[UITabBarCustomizeView tintTabBarItemsForEdit:];
-[UITabBarCustomizeView updateProxiesSelection];
```
