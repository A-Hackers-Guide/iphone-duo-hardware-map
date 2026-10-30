# `_UINavigationBarItemStackEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 9 properties, 17 instance methods, 2 class methods

## Instance variables

```
B _searchActive;
@"_UITypedStorage" _typedStorage;
@"UINavigationItem" _item;
@"_UINavigationBarLayout" _normalLayout;
@"_UINavigationBarLayout" _searchLayout;
```

## Properties

```
@property (TB,N,R) isActiveLayoutVariableHeight;
@property (T{?=ddd},N,R) layoutHeightsForActiveLayout;
@property (T@"NSString",N,R) swiftDescription;
@property (T@"UINavigationItem",R,N,V_item) item;
@property (T@"_UINavigationBarLayout",R,N) activeLayout;
@property (T@"_UINavigationBarLayout",R,N) inactiveLayout;
@property (TB,N,GisSearchActive,V_searchActive) searchActive;
@property (T@"_UINavigationBarLayout",&,N,V_normalLayout) normalLayout;
@property (T@"_UINavigationBarLayout",&,N,V_searchLayout) searchLayout;
```

## Class methods

```
+[_UINavigationBarItemStackEntry entryForItem:replaceExistingWithNew:];
+[_UINavigationBarItemStackEntry newEntryForItem:];
```

## Instance methods

```
-[_UINavigationBarItemStackEntry activeLayout];
-[_UINavigationBarItemStackEntry updateStateFromCounterpart:];
-[_UINavigationBarItemStackEntry searchLayout];
-[_UINavigationBarItemStackEntry isSearchActive];
-[_UINavigationBarItemStackEntry setSearchActive:];
-[_UINavigationBarItemStackEntry dealloc];
-[_UINavigationBarItemStackEntry item];
-[_UINavigationBarItemStackEntry swiftDescription];
-[_UINavigationBarItemStackEntry activeLayoutHeightRevealingPart:];
-[_UINavigationBarItemStackEntry isActiveLayoutVariableHeight];
-[_UINavigationBarItemStackEntry layoutHeightsForActiveLayout];
-[_UINavigationBarItemStackEntry inactiveLayout];
-[_UINavigationBarItemStackEntry description];
-[_UINavigationBarItemStackEntry activeLayoutHeightStackingPart:];
-[_UINavigationBarItemStackEntry setNormalLayout:];
-[_UINavigationBarItemStackEntry setSearchLayout:];
-[_UINavigationBarItemStackEntry normalLayout];
```
