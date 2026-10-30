# `SBApplicationShortcutStore`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSLock" _stateLock;
@"NSObject<OS_dispatch_queue>" _saveQueue;
@"NSArray" _cachedApplicationShortcutItems;
@"NSArray" _cachedLanguages;
Q _cachedVersion;
B _isLoaded;
B _isDirty;
@"FBSApplicationDataStore" _dataStore;
@"NSString" _bundleIdentifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSArray",R,C,N) applicationShortcutItems;
@property (T@"NSArray",R,C,N) languages;
@property (TQ,R,N) version;
```

## Class methods

```
+[SBApplicationShortcutStore clearStore];
```

## Instance methods

```
-[SBApplicationShortcutStore invalidateCache];
-[SBApplicationShortcutStore bundleIdentifier];
-[SBApplicationShortcutStore version];
-[SBApplicationShortcutStore applicationShortcutItems];
-[SBApplicationShortcutStore languages];
-[SBApplicationShortcutStore description];
-[SBApplicationShortcutStore initWithBundleIdentifier:];
-[SBApplicationShortcutStore _saveQueue_save];
-[SBApplicationShortcutStore _applicationShortcutItemsFromPlistArray:];
-[SBApplicationShortcutStore _plistArrayFromApplicationShortcutItems:];
-[SBApplicationShortcutStore _stateLock_loadFromStoreIfNeeded];
-[SBApplicationShortcutStore _stateLock_markDirty];
-[SBApplicationShortcutStore _stateLock_truncateIfNeeded:];
-[SBApplicationShortcutStore saveSynchronously];
-[SBApplicationShortcutStore setApplicationShortcutItems:withLanguages:version:];
-[SBApplicationShortcutStore truncateIfNecessary];
```
