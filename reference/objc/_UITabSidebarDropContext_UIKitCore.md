# `_UITabSidebarDropContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"UITabGroup" _activeTabGroup;
@"NSIndexPath" _proposedIndexPath;
q _insertionIndex;
```

## Properties

```
@property (T@"UITabGroup",R,W,N,V_activeTabGroup) activeTabGroup;
@property (T@"NSIndexPath",R,C,N,V_proposedIndexPath) proposedIndexPath;
@property (Tq,R,N,V_insertionIndex) insertionIndex;
```

## Class methods

```
+[_UITabSidebarDropContext contextWithGroup:proposedIndexPath:insertionIndex:];
```

## Instance methods

```
-[_UITabSidebarDropContext activeTabGroup];
-[_UITabSidebarDropContext insertionIndex];
-[_UITabSidebarDropContext proposedIndexPath];
```
