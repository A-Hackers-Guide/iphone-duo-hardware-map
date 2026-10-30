# `CAMVisualIntelligenceCameraPhotoResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIImage" _previewImage;
^{__CVBuffer=} _previewPixelBuffer;
@"UIImage" _fullsizeImage;
@"NSData" _fullsizeImageData;
@"NSDictionary" _metadata;
@"NSURL" _fileURL;
```

## Properties

```
@property (T@"UIImage",R,N,V_previewImage) previewImage;
@property (T^{__CVBuffer=},R,N,V_previewPixelBuffer) previewPixelBuffer;
@property (T@"UIImage",R,N,V_fullsizeImage) fullsizeImage;
@property (T@"NSData",R,N,V_fullsizeImageData) fullsizeImageData;
@property (T@"NSDictionary",R,N,V_metadata) metadata;
@property (T@"NSURL",R,N,V_fileURL) fileURL;
```

## Instance methods

```
-[CAMVisualIntelligenceCameraPhotoResult fileURL];
-[CAMVisualIntelligenceCameraPhotoResult dealloc];
-[CAMVisualIntelligenceCameraPhotoResult metadata];
-[CAMVisualIntelligenceCameraPhotoResult previewImage];
-[CAMVisualIntelligenceCameraPhotoResult previewPixelBuffer];
-[CAMVisualIntelligenceCameraPhotoResult fullsizeImage];
-[CAMVisualIntelligenceCameraPhotoResult fullsizeImageData];
-[CAMVisualIntelligenceCameraPhotoResult initWithPreviewImage:previewPixelBuffer:fullsizeImage:fullsizeImageData:metadata:fileURL:];
```
