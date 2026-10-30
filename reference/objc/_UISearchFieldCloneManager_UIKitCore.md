# `_UISearchFieldCloneManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _recentClones;
@"UISearchTextField" _activeClone;
@"UISearchTextField" _cloneUndergoingUpdates;
B _updatingClone;
```

## Properties

```
@property (T@"UISearchTextField",R,N) activeClone;
@property (TB,N,GisUpdatingClone,V_updatingClone) updatingClone;
```

## Instance methods

```
-[_UISearchFieldCloneManager addClone:];
-[_UISearchFieldCloneManager description];
-[_UISearchFieldCloneManager isUpdatingClone];
-[_UISearchFieldCloneManager activeClone];
-[_UISearchFieldCloneManager cloneDidMoveToWindowNotification:];
-[_UISearchFieldCloneManager refreshCloneAssignments];
-[_UISearchFieldCloneManager setUpdatingClone:];
-[_UISearchFieldCloneManager updateClonesOfSearchField:updates:];
```
