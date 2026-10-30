# `JTAssetMediaItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JTLocalAssetMediaItem`
- 5 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"PHAsset" _asset;
@"NSString" _assetIdentifier;
@"NSString" _masterFingerprint;
@"NSString" _adjustedFingerprint;
@"NSURL" _assetLocalURL;
```

## Properties

```
@property (T@"NSString",C,N,V_assetIdentifier) assetIdentifier;
@property (T@"NSString",C,N,V_masterFingerprint) masterFingerprint;
@property (T@"NSString",C,N,V_adjustedFingerprint) adjustedFingerprint;
@property (T@"PHAsset",&,N,V_asset) asset;
@property (T@"NSURL",&,N,V_assetLocalURL) assetLocalURL;
```

## Instance methods

```
-[JTAssetMediaItem assetIdentifier];
-[JTAssetMediaItem asset];
-[JTAssetMediaItem info];
-[JTAssetMediaItem setAsset:];
-[JTAssetMediaItem init];
-[JTAssetMediaItem dealloc];
-[JTAssetMediaItem hash];
-[JTAssetMediaItem description];
-[JTAssetMediaItem copyWithZone:];
-[JTAssetMediaItem isEqual:];
-[JTAssetMediaItem setAssetIdentifier:];
-[JTAssetMediaItem initWithAssetIdentifier:];
-[JTAssetMediaItem adjustedFingerprint];
-[JTAssetMediaItem assetLocalURL];
-[JTAssetMediaItem checkIfAssetIsMissing];
-[JTAssetMediaItem fetchAssetForce:];
-[JTAssetMediaItem initWithInfo:delegate:];
-[JTAssetMediaItem masterFingerprint];
-[JTAssetMediaItem reloadAsset];
-[JTAssetMediaItem setAdjustedFingerprint:];
-[JTAssetMediaItem setAssetLocalURL:];
-[JTAssetMediaItem setMasterFingerprint:];
```
