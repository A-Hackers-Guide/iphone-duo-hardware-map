# `SBApplicationShortcutStoreManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSLock" _stateLock;
@"NSMutableDictionary" _storesKeyedByBundleIdentifier;
```

## Instance methods

```
-[SBApplicationShortcutStoreManager invalidateCache];
-[SBApplicationShortcutStoreManager init];
-[SBApplicationShortcutStoreManager dealloc];
-[SBApplicationShortcutStoreManager _installedAppsDidChange:];
-[SBApplicationShortcutStoreManager _stateLock_storeForBundleIdentifier:];
-[SBApplicationShortcutStoreManager applicationShortcutItemsForBundleIdentifier:withVersion:];
-[SBApplicationShortcutStoreManager saveSynchronously];
-[SBApplicationShortcutStoreManager setApplicationShortcutItems:forBundleIdentifier:withVersion:];
```
