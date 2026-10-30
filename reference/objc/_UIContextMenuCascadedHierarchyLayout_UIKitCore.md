# `_UIContextMenuCascadedHierarchyLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuHierarchyLayout`
- 2 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _isAnimatingMenuAddition;
@"_UIContextMenuView" _menuView;
```

## Properties

```
@property (T@"_UIContextMenuView",W,N,V_menuView) menuView;
@property (TB,N,V_isAnimatingMenuAddition) isAnimatingMenuAddition;
```

## Instance methods

```
-[_UIContextMenuCascadedHierarchyLayout setMenuView:];
-[_UIContextMenuCascadedHierarchyLayout _metrics];
-[_UIContextMenuCascadedHierarchyLayout menuView];
-[_UIContextMenuCascadedHierarchyLayout _submenuOffsetForCascadingLeft:];
-[_UIContextMenuCascadedHierarchyLayout _cascadingAreaBounds];
-[_UIContextMenuCascadedHierarchyLayout encompassingSize];
-[_UIContextMenuCascadedHierarchyLayout initWithMenuView:];
-[_UIContextMenuCascadedHierarchyLayout isAnimatingMenuAddition];
-[_UIContextMenuCascadedHierarchyLayout navigateDownFromNode:toNode:alongsideAnimations:completion:];
-[_UIContextMenuCascadedHierarchyLayout navigateUpFromNode:toNode:alongsideAnimations:completion:];
-[_UIContextMenuCascadedHierarchyLayout performLayoutForComputingPreferredContentSize:withMaxContainerSize:];
-[_UIContextMenuCascadedHierarchyLayout setIsAnimatingMenuAddition:];
```
