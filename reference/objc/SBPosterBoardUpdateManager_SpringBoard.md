# `SBPosterBoardUpdateManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _schedulerQueue;
```

## Class methods

```
+[SBPosterBoardUpdateManager sharedInstance];
```

## Instance methods

```
-[SBPosterBoardUpdateManager removeObserver:];
-[SBPosterBoardUpdateManager init];
-[SBPosterBoardUpdateManager dealloc];
-[SBPosterBoardUpdateManager addObserver:];
-[SBPosterBoardUpdateManager _backgroundTaskIdentifierForUpdate:];
-[SBPosterBoardUpdateManager _isBGSystemTaskUpdate:];
-[SBPosterBoardUpdateManager _noteApplicationsChanged:];
-[SBPosterBoardUpdateManager _notifyDidFinishUpdate:error:];
-[SBPosterBoardUpdateManager _notifyWillBeginUpdate:];
-[SBPosterBoardUpdateManager _registerForWork:];
-[SBPosterBoardUpdateManager _schedulerQueue_submitTaskRequestForUpdate:updateIdentifier:];
-[SBPosterBoardUpdateManager _unregisterForWork:];
-[SBPosterBoardUpdateManager executeUpdate:forBackgroundTask:updateIdentifier:];
```
