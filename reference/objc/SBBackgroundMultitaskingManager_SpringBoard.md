# `SBBackgroundMultitaskingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _lock_appToBackgroundTasks;
```

## Instance methods

```
-[SBBackgroundMultitaskingManager init];
-[SBBackgroundMultitaskingManager _appProcessStateDidChange:];
-[SBBackgroundMultitaskingManager _backgroundTaskFinished:forAppInfo:];
-[SBBackgroundMultitaskingManager _createBackgroundFetchTaskForAppInfo:];
-[SBBackgroundMultitaskingManager createBackgroundFetchExternalRequestForAppInfo:];
```
