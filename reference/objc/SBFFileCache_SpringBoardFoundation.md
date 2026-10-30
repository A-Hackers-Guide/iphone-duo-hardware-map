# `SBFFileCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 7 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _manifest;
d _accessDateTimeAdjustment;
@"<SBFFileCacheStore>" _store;
@"<SBFFileCacheFaultHandler>" _faultHandler;
@"<SBFFileCacheDelegate>" _delegate;
Q _maxTotalFileSize;
Q _maxTotalFileCount;
d _maxAllowedTimeSinceLastAccess;
d _maxAllowedTimeSinceGeneration;
```

## Properties

```
@property (T@"<SBFFileCacheStore>",R,N,V_store) store;
@property (T@"<SBFFileCacheFaultHandler>",R,N,V_faultHandler) faultHandler;
@property (T@"<SBFFileCacheDelegate>",W,V_delegate) delegate;
@property (TQ,V_maxTotalFileSize) maxTotalFileSize;
@property (TQ,V_maxTotalFileCount) maxTotalFileCount;
@property (Td,V_maxAllowedTimeSinceLastAccess) maxAllowedTimeSinceLastAccess;
@property (Td,V_maxAllowedTimeSinceGeneration) maxAllowedTimeSinceGeneration;
```

## Instance methods

```
-[SBFFileCache store];
-[SBFFileCache init];
-[SBFFileCache setDelegate:];
-[SBFFileCache callbackQueue];
-[SBFFileCache delegate];
-[SBFFileCache description];
-[SBFFileCache _queue_evictIfNeededUsingStore:];
-[SBFFileCache _queue_accessDateTimeAdjustment];
-[SBFFileCache _queue_resetManifestUsingStore:];
-[SBFFileCache _queue_createManifestEntryForGeneratedFileWrapper:filename:usingStore:];
-[SBFFileCache _queue_evictFileWithInfo:usingStore:];
-[SBFFileCache _queue_evictFilesAtManifestIndexes:usingStore:];
-[SBFFileCache _queue_loadManifestUsingStore:];
-[SBFFileCache _queue_removeManifestEntryForFilename:usingStore:];
-[SBFFileCache _queue_saveManifestUsingStore:];
-[SBFFileCache _queue_updateManifestForLoadedFileWrapper:filename:usingStore:];
-[SBFFileCache faultHandler];
-[SBFFileCache fileNameForIdentifier:];
-[SBFFileCache initWithStore:faultHandler:];
-[SBFFileCache loadFileWithIdentifier:completionHandler:];
-[SBFFileCache maxAllowedTimeSinceGeneration];
-[SBFFileCache maxAllowedTimeSinceLastAccess];
-[SBFFileCache maxTotalFileCount];
-[SBFFileCache maxTotalFileSize];
-[SBFFileCache performOnWorkQueueUsingBlock:];
-[SBFFileCache removeAllFiles];
-[SBFFileCache removeFileWithIdentifier:];
-[SBFFileCache setAccessDateTimeAdjustment:];
-[SBFFileCache setMaxAllowedTimeSinceGeneration:];
-[SBFFileCache setMaxAllowedTimeSinceLastAccess:];
-[SBFFileCache setMaxTotalFileCount:];
-[SBFFileCache setMaxTotalFileSize:];
```
