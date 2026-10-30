# `CWFAssetRootMonitor`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 1 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSString" monitoredPath;
@"NSString" monitoredParentPath;
@"NSMutableSet" pathsUpdated;
@"NSMutableDictionary" pathsFileAttributes;
@"NSMutableDictionary" pathsFileAttributesAtLastCheck;
@"NSMutableSet" pathsExisting;
@"NSMutableSet" pathsExistingAtLastCheck;
q pathPollingInterval;
@"NSObject<OS_dispatch_queue>" timerQueue;
@"NSObject<OS_dispatch_source>" timer;
@"<CWFAssetRootMonitorDelegate>" _delegate;
```

## Properties

```
@property (T@"<CWFAssetRootMonitorDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CWFAssetRootMonitor startMonitoring];
-[CWFAssetRootMonitor dealloc];
-[CWFAssetRootMonitor setDelegate:];
-[CWFAssetRootMonitor delegate];
-[CWFAssetRootMonitor checkForChanges];
-[CWFAssetRootMonitor scheduleTimer];
-[CWFAssetRootMonitor checkForDeletedPath:];
-[CWFAssetRootMonitor handleUpdatedPaths];
-[CWFAssetRootMonitor initMonitorWithPath:];
-[CWFAssetRootMonitor printDictionaryDifferences:dictTwo:];
-[CWFAssetRootMonitor startMonitoringPath:];
-[CWFAssetRootMonitor stopMonitoringStream];
```
