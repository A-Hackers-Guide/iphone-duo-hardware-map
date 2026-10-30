# `_UITabSidebarBatchUpdatesTransaction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B shouldReloadEverything;
B selectedLeafInvalidated;
_updatedTabs;
_replacements;
```

## Properties

```
@property (TB,N,VshouldReloadEverything) shouldReloadEverything;
@property (TB,N,VselectedLeafInvalidated) selectedLeafInvalidated;
@property (T@"NSSet",N,R) updatedTabs;
```

## Instance methods

```
-[_UITabSidebarBatchUpdatesTransaction tabContentDidChange:];
-[_UITabSidebarBatchUpdatesTransaction init];
-[_UITabSidebarBatchUpdatesTransaction enumerateReplacements:];
-[_UITabSidebarBatchUpdatesTransaction invalidateEverything];
-[_UITabSidebarBatchUpdatesTransaction invalidateSelectedLeaf];
-[_UITabSidebarBatchUpdatesTransaction replaceItem:withItem:];
-[_UITabSidebarBatchUpdatesTransaction selectedLeafInvalidated];
-[_UITabSidebarBatchUpdatesTransaction setSelectedLeafInvalidated:];
-[_UITabSidebarBatchUpdatesTransaction setShouldReloadEverything:];
-[_UITabSidebarBatchUpdatesTransaction shouldReloadEverything];
-[_UITabSidebarBatchUpdatesTransaction updatedTabs];
```
