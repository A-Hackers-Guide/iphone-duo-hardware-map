# `PKLRUCache`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"PKLRUCacheItem" _firstItem;
@"PKLRUCacheItem" _lastItem;
@"PKLRUCacheItem" _freeItems;
@"NSMapTable" _itemTable;
Q _currentCost;
@"NSMutableArray" _freeKeys;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _totalCostLimit;
q _freeItemCount;
```

## Instance methods

```
-[PKLRUCache init];
-[PKLRUCache dealloc];
```
