# `AVAssetCache`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 1 properties, 17 instance methods, 4 class methods

## Properties

```
@property (TB,R,N,GisPlayableOffline) playableOffline;
```

## Class methods

```
+[AVAssetCache assetCacheForHTTPLiveStreamingWithURL:];
+[AVAssetCache assetCacheForProgressiveDownloadAndHTTPLiveStreamingWithURL:];
+[AVAssetCache assetCacheForProgressiveDownloadWithURL:];
+[AVAssetCache assetCacheWithURL:];
```

## Instance methods

```
-[AVAssetCache isPlayableOffline];
-[AVAssetCache maxSize];
-[AVAssetCache isDefunct];
-[AVAssetCache _init];
-[AVAssetCache initWithURL:];
-[AVAssetCache allKeys];
-[AVAssetCache URL];
-[AVAssetCache currentSize];
-[AVAssetCache lastModifiedDateOfEntryForKey:];
-[AVAssetCache maxEntrySize];
-[AVAssetCache mediaPresentationLanguagesForMediaSelectionGroup:];
-[AVAssetCache mediaPresentationSettingsForMediaSelectionGroup:];
-[AVAssetCache mediaSelectionOptionsInMediaSelectionGroup:];
-[AVAssetCache removeEntryForKey:];
-[AVAssetCache retrieveMediaStreamInfosForVariant:mediaSelection:completionHandler:];
-[AVAssetCache sizeOfEntryForKey:];
-[AVAssetCache variantsForMediaSelection:];
```
