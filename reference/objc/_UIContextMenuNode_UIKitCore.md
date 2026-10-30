# `_UIContextMenuNode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _leftOfParentWhenCascading;
@"_UIContextMenuListView" _listView;
@"UIMenu" _menu;
@"_UIContextMenuNode" _previous;
@"_UIContextMenuNode" _next;
```

## Properties

```
@property (T@"_UIContextMenuListView",&,N,V_listView) listView;
@property (T@"UIMenu",&,N,V_menu) menu;
@property (T@"_UIContextMenuNode",W,N,V_previous) previous;
@property (T@"_UIContextMenuNode",W,N,V_next) next;
@property (TB,N,V_leftOfParentWhenCascading) leftOfParentWhenCascading;
```

## Instance methods

```
-[_UIContextMenuNode menu];
-[_UIContextMenuNode setPrevious:];
-[_UIContextMenuNode next];
-[_UIContextMenuNode previous];
-[_UIContextMenuNode setNext:];
-[_UIContextMenuNode setListView:];
-[_UIContextMenuNode setLeftOfParentWhenCascading:];
-[_UIContextMenuNode listView];
-[_UIContextMenuNode description];
-[_UIContextMenuNode leftOfParentWhenCascading];
-[_UIContextMenuNode setMenu:];
```
