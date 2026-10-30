# `BWSemanticStyleColorCubeCache`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"BWColorLookupCache" _colorLookupCache;
@"NSMutableDictionary" _cubeFilterCache;
@"NSMutableArray" _recentFilterCacheKeys;
B _cachingEnabled;
Q _cacheMaxSize;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _filterCacheLock;
```

## Class methods

```
+[BWSemanticStyleColorCubeCache initialize];
```

## Instance methods

```
-[BWSemanticStyleColorCubeCache dealloc];
-[BWSemanticStyleColorCubeCache filtersForSemanticStyle:sceneType:personSegmentationEnabled:maskVisualizationEnabled:applyStyleBackgroundToEntireFrame:filtersToCombine:];
-[BWSemanticStyleColorCubeCache initWithColorLookupCache:];
```
