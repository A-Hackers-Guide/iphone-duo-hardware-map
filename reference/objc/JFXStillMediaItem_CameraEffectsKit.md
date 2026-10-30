# `JFXStillMediaItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JTAssetMediaItem`
- 4 instance variables, 4 properties, 33 instance methods, 1 class methods

## Instance variables

```
B _hasGainMap;
f _meteorPlusHeadroom;
@"PVColorSpace" _imageColorSpace;
{CGSize="width"d"height"d} _sourceImageSize;
```

## Properties

```
@property (T{CGSize=dd},N,V_sourceImageSize) sourceImageSize;
@property (TB,N,V_hasGainMap) hasGainMap;
@property (T@"PVColorSpace",&,N,V_imageColorSpace) imageColorSpace;
@property (Tf,N,V_meteorPlusHeadroom) meteorPlusHeadroom;
```

## Class methods

```
+[JFXStillMediaItem stillMediaItemWithLocalURL:delegate:completionHandler:];
```

## Instance methods

```
-[JFXStillMediaItem commonInit];
-[JFXStillMediaItem assetURL];
-[JFXStillMediaItem info];
-[JFXStillMediaItem colorSpace];
-[JFXStillMediaItem hash];
-[JFXStillMediaItem description];
-[JFXStillMediaItem hasGainMap];
-[JFXStillMediaItem copyWithZone:];
-[JFXStillMediaItem isEqual:];
-[JFXStillMediaItem sourceImageSize];
-[JFXStillMediaItem setSourceImageSize:];
-[JFXStillMediaItem imageColorSpace];
-[JFXStillMediaItem setImageColorSpace:];
-[JFXStillMediaItem durationAt30fps];
-[JFXStillMediaItem JT_maximumPixelsForStillImage:];
-[JFXStillMediaItem sizeForQuality:];
-[JFXStillMediaItem thumbImageSize:];
-[JFXStillMediaItem canBeAddedToSequence];
-[JFXStillMediaItem exportImageSize:];
-[JFXStillMediaItem generateLocalURLForAsset];
-[JFXStillMediaItem hasPhotoCharacteristic];
-[JFXStillMediaItem hasVisualCharacteristic];
-[JFXStillMediaItem hdrGainMapImageForURL:renderingIntent:];
-[JFXStillMediaItem imageForURL:renderingIntent:];
-[JFXStillMediaItem imageForURL:renderingIntent:useAuxillaryMap:];
-[JFXStillMediaItem imageSizeForRenderingIntent:originalSize:];
-[JFXStillMediaItem isImageValid:renderingIntent:size:];
-[JFXStillMediaItem meteorPlusHeadroom];
-[JFXStillMediaItem playBackImageSize:];
-[JFXStillMediaItem setHasGainMap:];
-[JFXStillMediaItem setMeteorPlusHeadroom:];
-[JFXStillMediaItem sizeForMaxPixels:sourceSize:];
-[JFXStillMediaItem updateAssetImageColorSpace];
```
