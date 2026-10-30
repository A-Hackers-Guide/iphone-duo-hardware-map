# `_UIEditMenuListPage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
d _width;
d _overlapWidth;
d _itemSpacing;
q _numberOfItemsUsingItemSpacing;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (T{_NSRange=QQ},R,N,V_range) range;
@property (Td,R,N,V_width) width;
@property (Td,N,V_overlapWidth) overlapWidth;
@property (Td,N,V_itemSpacing) itemSpacing;
@property (Tq,N,V_numberOfItemsUsingItemSpacing) numberOfItemsUsingItemSpacing;
```

## Instance methods

```
-[_UIEditMenuListPage range];
-[_UIEditMenuListPage itemSpacing];
-[_UIEditMenuListPage setItemSpacing:];
-[_UIEditMenuListPage description];
-[_UIEditMenuListPage width];
-[_UIEditMenuListPage isEqual:];
-[_UIEditMenuListPage _resolvedNumberOfPagesForItemSpacing];
-[_UIEditMenuListPage appendItemWithWidth:];
-[_UIEditMenuListPage enforceMinimumWidth:];
-[_UIEditMenuListPage initWithStartIndex:];
-[_UIEditMenuListPage numberOfItemsUsingItemSpacing];
-[_UIEditMenuListPage overlapWidth];
-[_UIEditMenuListPage prependItemWithWidth:];
-[_UIEditMenuListPage removeLastItemWithWidth:];
-[_UIEditMenuListPage setNumberOfItemsUsingItemSpacing:];
-[_UIEditMenuListPage setOverlapWidth:];
```
