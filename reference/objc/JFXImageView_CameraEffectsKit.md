# `JFXImageView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 9 properties, 28 instance methods, 3 class methods

## Instance variables

```
B _preferIOSurfaceForYUV;
B _preferMetalKit;
B _enableDebugDrawing;
B _disableIOSurface;
B _disableMetalKit;
@"JTImage" _jtImage;
q _imageViewType;
q _currentImageViewType;
@"UIView" _imageView;
```

## Properties

```
@property (Tq,N,V_currentImageViewType) currentImageViewType;
@property (T@"UIView",&,N,V_imageView) imageView;
@property (T@"JTImage",&,N,V_jtImage) jtImage;
@property (Tq,N,V_imageViewType) imageViewType;
@property (TB,N,V_preferIOSurfaceForYUV) preferIOSurfaceForYUV;
@property (TB,N,V_preferMetalKit) preferMetalKit;
@property (TB,N,V_enableDebugDrawing) enableDebugDrawing;
@property (TB,N,V_disableIOSurface) disableIOSurface;
@property (TB,N,V_disableMetalKit) disableMetalKit;
```

## Class methods

```
+[JFXImageView colorFromImageViewType:];
+[JFXImageView colorFromRenderingType:];
+[JFXImageView normalizedQuadVertices:viewSize:textureSize:contentMode:];
```

## Instance methods

```
-[JFXImageView setContentMode:];
-[JFXImageView setImageView:];
-[JFXImageView initWithCoder:];
-[JFXImageView imageView];
-[JFXImageView initWithFrame:];
-[JFXImageView flipX];
-[JFXImageView JFXImageView_commonInit];
-[JFXImageView disableMetalKit];
-[JFXImageView jtImage];
-[JFXImageView preferredImageViewTypeForImage:];
-[JFXImageView currentImageViewType];
-[JFXImageView disableIOSurface];
-[JFXImageView enableDebugDrawing];
-[JFXImageView imageViewType];
-[JFXImageView preferIOSurfaceForYUV];
-[JFXImageView preferMetalKit];
-[JFXImageView reconfigureImageView];
-[JFXImageView setCurrentImageViewType:];
-[JFXImageView setDisableIOSurface:];
-[JFXImageView setDisableMetalKit:];
-[JFXImageView setEnableDebugDrawing:];
-[JFXImageView setImageViewType:];
-[JFXImageView setJtImage:];
-[JFXImageView setPreferIOSurfaceForYUV:];
-[JFXImageView setPreferMetalKit:];
-[JFXImageView stringFromImageViewType:];
-[JFXImageView updateDebugDrawing];
-[JFXImageView updateImageViewImage];
```
