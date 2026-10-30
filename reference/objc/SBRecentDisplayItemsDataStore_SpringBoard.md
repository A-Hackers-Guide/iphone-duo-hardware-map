# `SBRecentDisplayItemsDataStore`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _recentLayouts;
@"<SBRecentDisplayItemsPersistenceDelegate>" _persistenceDelegate;
B _shouldFallbackToRecentAppLayouts;
```

## Properties

```
@property (T@"NSOrderedSet",C,N) displayItems;
@property (T@"<SBRecentDisplayItemsPersistenceDelegate>",W,N,V_persistenceDelegate) persistenceDelegate;
```

## Instance methods

```
-[SBRecentDisplayItemsDataStore displayItems];
-[SBRecentDisplayItemsDataStore init];
-[SBRecentDisplayItemsDataStore setDisplayItems:];
-[SBRecentDisplayItemsDataStore persistenceDelegate];
-[SBRecentDisplayItemsDataStore setPersistenceDelegate:];
-[SBRecentDisplayItemsDataStore _displayItemsFromRecentAppLayouts:];
-[SBRecentDisplayItemsDataStore initWithRecentLayouts:fallbackToRecentAppLayouts:];
```
