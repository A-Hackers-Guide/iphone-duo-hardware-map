# `CAMBurstThumbnailCluster`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" burstImages;
@? completionBlock;
@"NSMutableDictionary" imageProps;
@"CAMBurstYUVImage" image;
^{__IOSurface=} _fullsizeJpegData;
```

## Properties

```
@property (T@"NSMutableArray",VburstImages) burstImages;
@property (T@"NSMutableDictionary",VimageProps) imageProps;
@property (T@"CAMBurstYUVImage",Vimage) image;
@property (T^{__IOSurface=},V_fullsizeJpegData) fullsizeJpegData;
@property (T@?,VcompletionBlock) completionBlock;
```

## Instance methods

```
-[CAMBurstThumbnailCluster setCompletionBlock:];
-[CAMBurstThumbnailCluster completionBlock];
-[CAMBurstThumbnailCluster init];
-[CAMBurstThumbnailCluster dealloc];
-[CAMBurstThumbnailCluster image];
-[CAMBurstThumbnailCluster setImage:];
-[CAMBurstThumbnailCluster setBurstImages:];
-[CAMBurstThumbnailCluster addItemsFromCluster:];
-[CAMBurstThumbnailCluster burstImages];
-[CAMBurstThumbnailCluster computeMergeCost:::];
-[CAMBurstThumbnailCluster fullsizeJpegData];
-[CAMBurstThumbnailCluster imageProps];
-[CAMBurstThumbnailCluster initWithImageData:dict:identifier:imageProps:completionBlock:];
-[CAMBurstThumbnailCluster releaseImage];
-[CAMBurstThumbnailCluster setFullsizeJpegData:];
-[CAMBurstThumbnailCluster setImageProps:];
```
