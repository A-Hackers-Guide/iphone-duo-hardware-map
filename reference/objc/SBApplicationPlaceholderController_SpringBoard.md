# `SBApplicationPlaceholderController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLeafIconObserver`, `SBApplicationPlaceholderLifecycleObserver`, `SBHProxiedApplicationPlaceholderDelegate`
- 8 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _appController;
@"SBApplicationLibraryObserver" _lsWorkspaceObserver;
@"NSMutableDictionary" _placeholdersByBundleID;
@"NSMutableSet" _pendingAdded;
@"NSMutableSet" _pendingInstalled;
@"NSMutableSet" _pendingCancelled;
B _hasDownloadedFromStore;
B _usingNetwork;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationPlaceholderController applicationPlaceholdersNetworkUsageChanged:];
-[SBApplicationPlaceholderController placeholdersByDisplayID];
-[SBApplicationPlaceholderController _addPlaceholders:];
-[SBApplicationPlaceholderController _removePlaceholders:forInstall:];
-[SBApplicationPlaceholderController initWithApplicationController:];
-[SBApplicationPlaceholderController dealloc];
-[SBApplicationPlaceholderController isUsingNetwork];
-[SBApplicationPlaceholderController iconAccessoriesDidUpdate:];
-[SBApplicationPlaceholderController iconControllers];
-[SBApplicationPlaceholderController applicationPlaceholdersAdded:];
-[SBApplicationPlaceholderController applicationPlaceholdersInstalled:];
-[SBApplicationPlaceholderController placeholderWantsUninstall:];
-[SBApplicationPlaceholderController _postPlaceholdersDidChangeForAdded:modified:removed:];
-[SBApplicationPlaceholderController _finishPlaceholder:];
-[SBApplicationPlaceholderController placeholderShouldAllowPausing:];
-[SBApplicationPlaceholderController hasDownloadedStoreApplication];
-[SBApplicationPlaceholderController _processPendingProxies];
-[SBApplicationPlaceholderController applicationPlaceholdersCancelled:];
-[SBApplicationPlaceholderController placeholderForDisplayID:];
-[SBApplicationPlaceholderController placeholderRepresentsNewAppInstallFromStore:];
```
