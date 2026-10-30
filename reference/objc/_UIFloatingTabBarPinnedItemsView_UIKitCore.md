# `_UIFloatingTabBarPinnedItemsView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _editing;
q _selectionViewIndex;
q _highlightedIndex;
@"NSArray" _items;
@"NSMutableDictionary" _itemViews;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_itemViews) itemViews;
@property (Tq,N,V_selectionViewIndex) selectionViewIndex;
@property (Tq,N,V_highlightedIndex) highlightedIndex;
@property (T@"NSArray",R,N,V_items) items;
@property (TB,N,GisEditing,V_editing) editing;
```

## Instance methods

```
-[_UIFloatingTabBarPinnedItemsView layoutSubviews];
-[_UIFloatingTabBarPinnedItemsView items];
-[_UIFloatingTabBarPinnedItemsView sizeThatFits:];
-[_UIFloatingTabBarPinnedItemsView setEditing:];
-[_UIFloatingTabBarPinnedItemsView itemViews];
-[_UIFloatingTabBarPinnedItemsView isEditing];
-[_UIFloatingTabBarPinnedItemsView initWithFrame:];
-[_UIFloatingTabBarPinnedItemsView setItems:animated:];
-[_UIFloatingTabBarPinnedItemsView _itemViewForItem:];
-[_UIFloatingTabBarPinnedItemsView _itemViewForItemAtIndex:];
-[_UIFloatingTabBarPinnedItemsView _reloadItemViewsWithDifference:animated:];
-[_UIFloatingTabBarPinnedItemsView highlightedIndex];
-[_UIFloatingTabBarPinnedItemsView itemFrameForItemAtIndex:];
-[_UIFloatingTabBarPinnedItemsView itemIndexForItemAtLocation:];
-[_UIFloatingTabBarPinnedItemsView itemIndexForTab:];
-[_UIFloatingTabBarPinnedItemsView itemViewForItemAtIndex:];
-[_UIFloatingTabBarPinnedItemsView reloadItemViewForTab:];
-[_UIFloatingTabBarPinnedItemsView selectionViewIndex];
-[_UIFloatingTabBarPinnedItemsView setHighlightedIndex:];
-[_UIFloatingTabBarPinnedItemsView setSelectionViewIndex:];
-[_UIFloatingTabBarPinnedItemsView tabForSelectionAtItemIndex:];
```
