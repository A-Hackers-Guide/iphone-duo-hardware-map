# `_UITabGroup` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"UITab",R,N) selectedChild;
@property (T@"NSArray",R,C,N) children;
@property (TB,N) allowsReordering;
@property (TB,R,N,GisCollapsedByDefault) collapsedByDefault;
@property (TQ,R,N) sidebarAppearance;
@property (T@"NSArray",R,N) sidebarActions;
```

## Instance methods

```
-[_UITabGroup allowsReordering];
-[_UITabGroup _canReorderChild:];
-[_UITabGroup setAllowsReordering:];
-[_UITabGroup tabForIdentifier:];
-[_UITabGroup _updateForManagingNavigationStackChange];
-[_UITabGroup _selectElement:notifyOnReselection:performBeforeNotifyingDelegate:];
-[_UITabGroup children];
-[_UITabGroup _filteredDisplayOrderIdentifiers];
-[_UITabGroup isCollapsedByDefault];
-[_UITabGroup _setDisplayOrderIdentifiers:];
-[_UITabGroup _updateManagingNavigationStackUsingTransition:];
-[_UITabGroup _defaultChildForSelection];
-[_UITabGroup sidebarAppearance];
-[_UITabGroup sidebarActions];
-[_UITabGroup selectedChild];
-[_UITabGroup _orderedChildrenForDisplayOrder:];
```
