# `_UITabOutlineParser`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _includeAllowsHidingItems;
@"NSArray" _rootItems;
@"NSArray" _groupItems;
@"NSMutableDictionary" _contentByIdentifier;
@"NSMutableSet" _allGroupIdentifiers;
@"NSMutableSet" _collapsedByDefaultGroupIdentifiers;
@"_UITabSidebarTransaction" _transaction;
```

## Properties

```
@property (TB,R,N,V_includeAllowsHidingItems) includeAllowsHidingItems;
@property (T@"NSMutableDictionary",&,N,V_contentByIdentifier) contentByIdentifier;
@property (T@"NSMutableSet",&,N,V_allGroupIdentifiers) allGroupIdentifiers;
@property (T@"NSMutableSet",&,N,V_collapsedByDefaultGroupIdentifiers) collapsedByDefaultGroupIdentifiers;
@property (T@"_UITabSidebarTransaction",W,N,V_transaction) transaction;
@property (T@"NSArray",R,N,V_rootItems) rootItems;
@property (T@"NSArray",R,N,V_groupItems) groupItems;
```

## Instance methods

```
-[_UITabOutlineParser setTransaction:];
-[_UITabOutlineParser transaction];
-[_UITabOutlineParser rootItems];
-[_UITabOutlineParser allGroupIdentifiers];
-[_UITabOutlineParser _parseNode:tabs:rootNode:];
-[_UITabOutlineParser _parseTabs:];
-[_UITabOutlineParser collapsedByDefaultGroupIdentifiers];
-[_UITabOutlineParser contentByIdentifier];
-[_UITabOutlineParser groupItems];
-[_UITabOutlineParser includeAllowsHidingItems];
-[_UITabOutlineParser initWithTabs:];
-[_UITabOutlineParser initWithTabs:includeAllowsHidingItems:transaction:];
-[_UITabOutlineParser setAllGroupIdentifiers:];
-[_UITabOutlineParser setCollapsedByDefaultGroupIdentifiers:];
-[_UITabOutlineParser setContentByIdentifier:];
```
