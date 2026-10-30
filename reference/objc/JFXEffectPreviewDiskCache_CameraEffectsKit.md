# `JFXEffectPreviewDiskCache`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSString" _cacheDirectoryPath;
@"NSString" _directoryName;
@"NSOperationQueue" _diskAccessQueue;
```

## Properties

```
@property (T@"NSString",R,N,V_directoryName) directoryName;
@property (T@"NSString",R,N,V_cacheDirectoryPath) cacheDirectoryPath;
@property (T@"NSOperationQueue",R,N,V_diskAccessQueue) diskAccessQueue;
```

## Class methods

```
+[JFXEffectPreviewDiskCache cachedPathForEffect:version:directoryPath:];
+[JFXEffectPreviewDiskCache createCacheAtDirectory:];
```

## Instance methods

```
-[JFXEffectPreviewDiskCache initWithDirectory:];
-[JFXEffectPreviewDiskCache dealloc];
-[JFXEffectPreviewDiskCache cacheDirectoryPath];
-[JFXEffectPreviewDiskCache directoryName];
-[JFXEffectPreviewDiskCache diskAccessQueue];
-[JFXEffectPreviewDiskCache cachedURLForEffect:version:];
-[JFXEffectPreviewDiskCache previewForEffectID:version:completion:];
-[JFXEffectPreviewDiskCache removePreviewForEffectID:excludingVersion:completion:];
-[JFXEffectPreviewDiskCache savePreviewForEffectID:image:version:completion:];
```
