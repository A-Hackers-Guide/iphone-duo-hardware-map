# `_UITableViewDropAnimationContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITableViewContainerView`
- 3 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
q _activeDropAnimationCount;
d _originalTargetCenterY;
{CGPoint="x"d"y"d} __tableViewContainerOffsetFromTargetCenter;
```

## Properties

```
@property (Tq,N,V_activeDropAnimationCount) activeDropAnimationCount;
@property (Td,N,V_originalTargetCenterY) originalTargetCenterY;
@property (T@"NSArray",R,N) cells;
@property (TB,R,N) hasCompletedAllDropAnimations;
@property (T{CGPoint=dd},N,V__tableViewContainerOffsetFromTargetCenter) _tableViewContainerOffsetFromTargetCenter;
```

## Instance methods

```
-[_UITableViewDropAnimationContainerView init];
-[_UITableViewDropAnimationContainerView setCenter:];
-[_UITableViewDropAnimationContainerView setFrame:];
-[_UITableViewDropAnimationContainerView cells];
-[_UITableViewDropAnimationContainerView _tableViewContainerOffsetFromTargetCenter];
-[_UITableViewDropAnimationContainerView activeDropAnimationCount];
-[_UITableViewDropAnimationContainerView beginDropAnimation];
-[_UITableViewDropAnimationContainerView endDropAnimation];
-[_UITableViewDropAnimationContainerView hasCompletedAllDropAnimations];
-[_UITableViewDropAnimationContainerView originalTargetCenterY];
-[_UITableViewDropAnimationContainerView setActiveDropAnimationCount:];
-[_UITableViewDropAnimationContainerView setOriginalTargetCenterY:];
-[_UITableViewDropAnimationContainerView set_tableViewContainerOffsetFromTargetCenter:];
-[_UITableViewDropAnimationContainerView updateOffsetFromTargetCenterIfNeeded];
```
