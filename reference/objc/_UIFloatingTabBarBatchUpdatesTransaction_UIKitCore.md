# `_UIFloatingTabBarBatchUpdatesTransaction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
_invalidationLevel;
_animateFavoriteOrderInvalidation;
_isSelectedLeafInvalidated;
_updatedTabs;
```

## Properties

```
@property (TB,N,R) isDataSourceInvalidated;
@property (TB,N,R) isFavoriteOrderInvalidated;
@property (TB,N,R) animateFavoriteOrderInvalidation;
@property (TB,N,R) isSelectedLeafInvalidated;
@property (T@"NSSet",N,R) updatedTabs;
```

## Instance methods

```
-[_UIFloatingTabBarBatchUpdatesTransaction tabContentDidChange:];
-[_UIFloatingTabBarBatchUpdatesTransaction init];
-[_UIFloatingTabBarBatchUpdatesTransaction animateFavoriteOrderInvalidation];
-[_UIFloatingTabBarBatchUpdatesTransaction invalidateDataSource];
-[_UIFloatingTabBarBatchUpdatesTransaction invalidateFavoriteOrderAnimated:];
-[_UIFloatingTabBarBatchUpdatesTransaction invalidateSelectedLeaf];
-[_UIFloatingTabBarBatchUpdatesTransaction isDataSourceInvalidated];
-[_UIFloatingTabBarBatchUpdatesTransaction isFavoriteOrderInvalidated];
-[_UIFloatingTabBarBatchUpdatesTransaction isSelectedLeafInvalidated];
-[_UIFloatingTabBarBatchUpdatesTransaction updatedTabs];
```
