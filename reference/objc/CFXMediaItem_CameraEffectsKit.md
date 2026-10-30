# `CFXMediaItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _initializedWithoutSettingAllProperties;
B _adjustmentsDataWasSet;
@"CFXClip" _clip;
@"NSURL" _adjustedAssetURL;
@"NSURL" _originalAssetURL;
q _type;
q _cameraMode;
@"NSURL" _metadataURL;
q _cameraPosition;
```

## Properties

```
@property (TB,N,V_initializedWithoutSettingAllProperties) initializedWithoutSettingAllProperties;
@property (TB,N,V_adjustmentsDataWasSet) adjustmentsDataWasSet;
@property (Tq,R,N,V_cameraMode) cameraMode;
@property (T@"NSURL",R,N,V_metadataURL) metadataURL;
@property (Tq,R,N,V_cameraPosition) cameraPosition;
@property (T@"CFXClip",R,N,V_clip) clip;
@property (T@"NSData",C,N) adjustmentsData;
@property (T@"NSURL",C,N,V_adjustedAssetURL) adjustedAssetURL;
@property (T@"NSURL",C,N,V_originalAssetURL) originalAssetURL;
@property (Tq,N,V_type) type;
```

## Instance methods

```
-[CFXMediaItem init];
-[CFXMediaItem metadataURL];
-[CFXMediaItem setType:];
-[CFXMediaItem type];
-[CFXMediaItem adjustmentsData];
-[CFXMediaItem clip];
-[CFXMediaItem originalAssetURL];
-[CFXMediaItem setOriginalAssetURL:];
-[CFXMediaItem cameraMode];
-[CFXMediaItem cameraPosition];
-[CFXMediaItem CFX_updateCameraPositionForPhotoType];
-[CFXMediaItem adjustedAssetURL];
-[CFXMediaItem adjustmentsDataWasSet];
-[CFXMediaItem createClipForMediaType:assetURL:cameraMode:effectStack:];
-[CFXMediaItem initWithCameraMode:clip:assetMediaURL:assetMetadataURL:cameraPosition:];
-[CFXMediaItem initWithType:originalAssetURL:adjustmentsData:];
-[CFXMediaItem initializedWithoutSettingAllProperties];
-[CFXMediaItem setAdjustedAssetURL:];
-[CFXMediaItem setAdjustmentsData:];
-[CFXMediaItem setAdjustmentsDataWasSet:];
-[CFXMediaItem setInitializedWithoutSettingAllProperties:];
```
