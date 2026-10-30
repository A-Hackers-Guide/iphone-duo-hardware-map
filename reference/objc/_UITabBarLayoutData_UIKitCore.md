# `_UITabBarLayoutData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarAppearanceData`
- 5 instance variables, 5 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"UIColor" _selectionIndicatorTintColor;
@"UIImage" _selectionIndicatorImage;
q _itemPositioning;
d _itemWidth;
d _itemSpacing;
```

## Properties

```
@property (T@"UIColor",C,N,V_selectionIndicatorTintColor) selectionIndicatorTintColor;
@property (T@"UIImage",&,N,V_selectionIndicatorImage) selectionIndicatorImage;
@property (Tq,N,V_itemPositioning) itemPositioning;
@property (Td,N,V_itemWidth) itemWidth;
@property (Td,N,V_itemSpacing) itemSpacing;
```

## Class methods

```
+[_UITabBarLayoutData decodeFromCoder:prefix:];
+[_UITabBarLayoutData standardLayoutData];
```

## Instance methods

```
-[_UITabBarLayoutData selectionIndicatorImage];
-[_UITabBarLayoutData setSelectionIndicatorImage:];
-[_UITabBarLayoutData describeInto:];
-[_UITabBarLayoutData hashInto:];
-[_UITabBarLayoutData setItemPositioning:];
-[_UITabBarLayoutData encodeToCoder:prefix:];
-[_UITabBarLayoutData itemWidth];
-[_UITabBarLayoutData itemSpacing];
-[_UITabBarLayoutData setItemSpacing:];
-[_UITabBarLayoutData selectionIndicatorTintColor];
-[_UITabBarLayoutData checkEqualTo:];
-[_UITabBarLayoutData itemPositioning];
-[_UITabBarLayoutData setItemWidth:];
-[_UITabBarLayoutData setSelectionIndicatorTintColor:];
-[_UITabBarLayoutData replicate];
-[_UITabBarLayoutData positioningForTraitCollection:];
```
