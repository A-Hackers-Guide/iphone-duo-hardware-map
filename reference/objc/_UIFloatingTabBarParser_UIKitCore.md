# `_UIFloatingTabBarParser`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _fixedItems;
@"NSArray" _pinnedItems;
@"NSArray" _items;
@"NSSet" _itemIdentifiers;
@"NSOrderedSet" _currentFavoriteOrder;
@"NSOrderedSet" _sourceTabIdentifiers;
@"_UITabModel" _tabModel;
@"NSOrderedSet" _overrideFavoriteOrder;
@"UITab" _placeholderTab;
@"NSSet" _ignoredFavoriteOrderItems;
@"NSMutableArray" _fixedTabs;
@"NSMutableArray" _sourceTabs;
@"NSMutableArray" _pinnedTabs;
@"NSOrderedSet" _favoriteOrder;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_fixedTabs) fixedTabs;
@property (T@"NSMutableArray",R,N,V_sourceTabs) sourceTabs;
@property (T@"NSMutableArray",R,N,V_pinnedTabs) pinnedTabs;
@property (T@"NSOrderedSet",R,N,V_favoriteOrder) favoriteOrder;
```

## Instance methods

```
-[_UIFloatingTabBarParser pinnedTabs];
-[_UIFloatingTabBarParser _canDisplayTabInBar:];
-[_UIFloatingTabBarParser _insertIdentifiersFromItems:intoSet:];
-[_UIFloatingTabBarParser _listItemsForTabs:customizableOnly:];
-[_UIFloatingTabBarParser _listItemsFromFavoriteOrder];
-[_UIFloatingTabBarParser _listItemsFromOverrideFavoriteOrder];
-[_UIFloatingTabBarParser _parseTabs:fixedTabs:sourceTabs:pinnedTabs:sourceIdentifiers:];
-[_UIFloatingTabBarParser favoriteOrder];
-[_UIFloatingTabBarParser fixedTabs];
-[_UIFloatingTabBarParser sourceTabs];
```
