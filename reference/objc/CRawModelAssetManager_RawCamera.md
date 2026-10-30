# `CRawModelAssetManager`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _nextAttemptTime;
@"NSMutableDictionary" _lastLoggedSource;
@"NSMutableDictionary" _installedDirCache;
@"NSMutableDictionary" _installedDirCacheExpiry;
@"NSMutableDictionary" _downloadProgress;
@"NSMutableDictionary" _pendingStartCompletions;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableDictionary",&,N,V_nextAttemptTime) nextAttemptTime;
@property (T@"NSMutableDictionary",&,N,V_lastLoggedSource) lastLoggedSource;
@property (T@"NSMutableDictionary",&,N,V_installedDirCache) installedDirCache;
@property (T@"NSMutableDictionary",&,N,V_installedDirCacheExpiry) installedDirCacheExpiry;
@property (T@"NSMutableDictionary",&,N,V_downloadProgress) downloadProgress;
@property (T@"NSMutableDictionary",&,N,V_pendingStartCompletions) pendingStartCompletions;
```

## Class methods

```
+[CRawModelAssetManager shared];
```

## Instance methods

```
-[CRawModelAssetManager setDownloadProgress:];
-[CRawModelAssetManager downloadProgress];
-[CRawModelAssetManager init];
-[CRawModelAssetManager queue];
-[CRawModelAssetManager pendingStartCompletions];
-[CRawModelAssetManager setPendingStartCompletions:];
-[CRawModelAssetManager setQueue:];
-[CRawModelAssetManager nextAttemptTime];
-[CRawModelAssetManager addDownloadProgressForClass:version:expectedBytes:];
-[CRawModelAssetManager attachDownloadProgressForAsset:class:version:];
-[CRawModelAssetManager beginDownloadProgressForAsset:class:version:];
-[CRawModelAssetManager bestAssetForClass:version:inCatalog:];
-[CRawModelAssetManager downloadedDirectoryForClass:];
-[CRawModelAssetManager ensureModelDownloadedForClass:timeout:];
-[CRawModelAssetManager finishDownloadProgressForClass:version:success:];
-[CRawModelAssetManager installedDirCache];
-[CRawModelAssetManager installedDirCacheExpiry];
-[CRawModelAssetManager installedModelDirectoryForClass:];
-[CRawModelAssetManager invalidateInstalledDirCache];
-[CRawModelAssetManager isDownloadInFlightForClass:version:];
-[CRawModelAssetManager isModelInstalledForClass:];
-[CRawModelAssetManager lastLoggedSource];
-[CRawModelAssetManager markDownloadInFlightForClass:version:];
-[CRawModelAssetManager prefetchModelForClass:];
-[CRawModelAssetManager resolveModelDirectoryForClass:source:];
-[CRawModelAssetManager setInstalledDirCache:];
-[CRawModelAssetManager setInstalledDirCacheExpiry:];
-[CRawModelAssetManager setLastLoggedSource:];
-[CRawModelAssetManager setNextAttemptTime:];
-[CRawModelAssetManager startAssetDownloadForClass:version:inCatalog:];
-[CRawModelAssetManager startDownloadForAllModelsWithCompletion:];
-[CRawModelAssetManager startDownloadForClass:version:expectedBytes:completion:];
-[CRawModelAssetManager watchInFlightDownloadForClass:version:asset:deadline:];
```
