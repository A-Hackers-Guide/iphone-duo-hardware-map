# `CAMThumbnailGenerator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" __generationQueue;
^{OpaqueVTPixelTransferSession=} __generationQueuePixelTransferSession;
@"NSMapTable" __generationQueueRotationSessionsMapTable;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__generationQueue) _generationQueue;
@property (T^{OpaqueVTPixelTransferSession=},R,N,V__generationQueuePixelTransferSession) _generationQueuePixelTransferSession;
@property (T@"NSMapTable",R,N,V__generationQueueRotationSessionsMapTable) _generationQueueRotationSessionsMapTable;
```

## Instance methods

```
-[CAMThumbnailGenerator init];
-[CAMThumbnailGenerator dealloc];
-[CAMThumbnailGenerator _generationQueue];
-[CAMThumbnailGenerator _generationQueuePixelTransferSession];
-[CAMThumbnailGenerator _generationQueueRotationSessionsMapTable];
-[CAMThumbnailGenerator _neededColorspacePropertiesFromMetadata:];
-[CAMThumbnailGenerator _newThumbnailOfFormat:inOrientation:withPixelFormat:usingPixelBuffer:];
-[CAMThumbnailGenerator _newThumbnailOfSize:inOrientation:withPixelFormat:usingPixelBuffer:];
-[CAMThumbnailGenerator newBGRAImageInOrientation:usingPixelBuffer:];
-[CAMThumbnailGenerator newBGRAImageInOrientation:usingSurface:];
-[CAMThumbnailGenerator newBGRAImageOfFormat:inOrientation:usingPixelBuffer:];
-[CAMThumbnailGenerator newBGRAImageOfFormat:inOrientation:usingSurface:];
-[CAMThumbnailGenerator newJPEGDataInOrientation:usingPixelBuffer:];
-[CAMThumbnailGenerator newJPEGDataInOrientation:usingSurface:withMetadata:];
-[CAMThumbnailGenerator newJPEGDataOfFormat:inOrientation:usingSurface:withMetadata:];
-[CAMThumbnailGenerator newRotatedPixelBuffer:inOrientation:];
```
