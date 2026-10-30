# `AVManagedAssetCache`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetCache`
- 1 instance variables, 0 properties, 21 instance methods, 4 class methods

## Instance variables

```
@"AVManagedAssetCacheInternal" _priv;
```

## Class methods

```
+[AVManagedAssetCache assetCacheForHTTPLiveStreamingWithURL:];
+[AVManagedAssetCache assetCacheForProgressiveDownloadAndHTTPLiveStreamingWithURL:];
+[AVManagedAssetCache assetCacheForProgressiveDownloadWithURL:];
+[AVManagedAssetCache assetCacheWithURL:];
```

## Instance methods

```
-[AVManagedAssetCache isPlayableOffline];
-[AVManagedAssetCache dealloc];
-[AVManagedAssetCache maxSize];
-[AVManagedAssetCache isDefunct];
-[AVManagedAssetCache setMaxSize:];
-[AVManagedAssetCache initWithURL:];
-[AVManagedAssetCache allKeys];
-[AVManagedAssetCache URL];
-[AVManagedAssetCache isHTTPLiveStreamingCacheEnabled];
-[AVManagedAssetCache currentSize];
-[AVManagedAssetCache enableAutomaticCacheSizeManagement];
-[AVManagedAssetCache initWithURL:enableCRABSCache:enableHLSCache:];
-[AVManagedAssetCache isProgressiveDownloadCacheEnabled];
-[AVManagedAssetCache lastModifiedDateOfEntryForKey:];
-[AVManagedAssetCache maxEntrySize];
-[AVManagedAssetCache mediaPresentationLanguagesForMediaSelectionGroup:];
-[AVManagedAssetCache mediaPresentationSettingsForMediaSelectionGroup:];
-[AVManagedAssetCache mediaSelectionOptionsInMediaSelectionGroup:];
-[AVManagedAssetCache removeEntryForKey:];
-[AVManagedAssetCache setMaxEntrySize:];
-[AVManagedAssetCache sizeOfEntryForKey:];
```
