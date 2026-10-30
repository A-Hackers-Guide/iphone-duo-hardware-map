# `_UIStatusBarActivityItem_Split`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarActivityItem_SyncOnly`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"_UIStatusBarActivityView" _activityView;
@"_UIStatusBarActivityIndicator" _syncStartView;
```

## Properties

```
@property (T@"_UIStatusBarActivityView",&,N,V_activityView) activityView;
@property (T@"_UIStatusBarActivityIndicator",&,N,V_syncStartView) syncStartView;
```

## Class methods

```
+[_UIStatusBarActivityItem_Split pillDisplayIdentifier];
+[_UIStatusBarActivityItem_Split syncStartDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarActivityItem_Split _create_syncStartView];
-[_UIStatusBarActivityItem_Split viewForIdentifier:];
-[_UIStatusBarActivityItem_Split setActivityView:];
-[_UIStatusBarActivityItem_Split additionAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarActivityItem_Split _create_activityView];
-[_UIStatusBarActivityItem_Split setSyncStartView:];
-[_UIStatusBarActivityItem_Split activityView];
-[_UIStatusBarActivityItem_Split removalAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarActivityItem_Split applyUpdate:toDisplayItem:];
-[_UIStatusBarActivityItem_Split syncStartView];
-[_UIStatusBarActivityItem_Split activityIndicatorAlignmentRectInsets];
```
