# `_UITabSidebarContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"UITab" _tab;
@"UIAction" _action;
@"UITabGroup" _group;
@"_UITabOutlineNode" _node;
```

## Properties

```
@property (T@"_UITabOutlineNode",&,N,V_node) node;
@property (T@"UITab",R,N,V_tab) tab;
@property (T@"UIAction",R,N,V_action) action;
@property (T@"UITabGroup",R,N,V_group) group;
```

## Class methods

```
+[_UITabSidebarContent contentForAction:group:];
+[_UITabSidebarContent contentForTab:];
```

## Instance methods

```
-[_UITabSidebarContent group];
-[_UITabSidebarContent setNode:];
-[_UITabSidebarContent action];
-[_UITabSidebarContent node];
-[_UITabSidebarContent tab];
-[_UITabSidebarContent _isTabContent];
-[_UITabSidebarContent isCompatibleWithContent:];
-[_UITabSidebarContent isEmptyGroup];
-[_UITabSidebarContent updatedContentForTab:];
```
