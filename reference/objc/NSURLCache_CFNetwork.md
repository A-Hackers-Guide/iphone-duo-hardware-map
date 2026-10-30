# `NSURLCache`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 41 instance methods, 2 class methods

## Instance variables

```
@"NSURLCacheInternal" _internal;
```

## Properties

```
@property (TQ) memoryCapacity;
@property (TQ) diskCapacity;
@property (TQ,R) currentMemoryUsage;
@property (TQ,R) currentDiskUsage;
```

## Class methods

```
+[NSURLCache sharedURLCache];
+[NSURLCache setSharedURLCache:];
```

## Instance methods

```
-[NSURLCache removeCachedResponseForRequest:];
-[NSURLCache _nscfBridgeURLCacheRemoveCachedResponseForRequest:];
-[NSURLCache memoryCapacity];
-[NSURLCache diskCapacity];
-[NSURLCache initWithMemoryCapacity:diskCapacity:diskPath:];
-[NSURLCache init];
-[NSURLCache storeCachedResponse:forRequest:];
-[NSURLCache _maxCacheableEntrySizeRatio];
-[NSURLCache removeAllCachedResponses];
-[NSURLCache dealloc];
-[NSURLCache _diskCacheDefaultPath];
-[NSURLCache _nscfBridgeURLCacheSetDiskCapacity:];
-[NSURLCache _initVaryHeaderEnabledWithPath:];
-[NSURLCache currentDiskUsage];
-[NSURLCache setDiskCapacity:];
-[NSURLCache _varyStateForURL:];
-[NSURLCache getCachedResponseForDataTask:completionHandler:];
-[NSURLCache _initWithMemoryCapacity:diskCapacity:relativePath:];
-[NSURLCache _nscfBridgeURLCacheCurrentMemoryUsage];
-[NSURLCache _nscfBridgeURLCacheStoreCachedResponse:forRequest:];
-[NSURLCache initWithMemoryCapacity:diskCapacity:directoryURL:];
-[NSURLCache set_maxCacheableEntrySizeRatio:];
-[NSURLCache removeCachedResponsesSinceDate:];
-[NSURLCache _nscfBridgeURLCacheMemoryCapacity];
-[NSURLCache _cacheDirectory];
-[NSURLCache flushWithCompletion:];
-[NSURLCache cachedResponseForRequest:];
-[NSURLCache _nscfBridgeURLCacheDiskCapacity];
-[NSURLCache _initWithExistingCFURLCache:];
-[NSURLCache _nscfBridgeURLCacheCurrentDiskUsage];
-[NSURLCache storeCachedResponse:forDataTask:];
-[NSURLCache removeCachedResponseForDataTask:];
-[NSURLCache _isVaryHeaderSupportEnabled];
-[NSURLCache _nscfBridgeURLCacheSetMemoryCapacity:];
-[NSURLCache _CFURLCache];
-[NSURLCache setMemoryCapacity:];
-[NSURLCache _nscfBridgeURLCacheCopyResponseForRequest:];
-[NSURLCache currentMemoryUsage];
-[NSURLCache _initWithIdentifier:memoryCapacity:diskCapacity:private:];
-[NSURLCache _updateVaryState:forURL:];
-[NSURLCache _nscfBridgeURLCacheRemoveAllCachedResponses];
```
