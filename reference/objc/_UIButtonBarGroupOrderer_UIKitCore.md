# `_UIButtonBarGroupOrderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSMutableOrderedSet" _includedItems;
@"NSMutableSet" _excludedItems;
@"NSArray" _orderedGroups;
@"NSArray" _orderedGroupsPartitionedIntoSections;
@"NSString" _customizationIdentifier;
@"<_UIButtonBarGroupOrderOwner>" _owner;
```

## Class methods

```
+[_UIButtonBarGroupOrderer groupOrdererForCustomizationIdentifier:];
```

## Instance methods

```
-[_UIButtonBarGroupOrderer _hasCustomization];
-[_UIButtonBarGroupOrderer _initWithCustomizationIdentifier:data:];
-[_UIButtonBarGroupOrderer _orderGroups];
```
