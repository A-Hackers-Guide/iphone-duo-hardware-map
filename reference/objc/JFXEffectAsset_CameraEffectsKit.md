# `JFXEffectAsset`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _contentUpdateAvailable;
@"NSString" _assetID;
@"NSURL" _localURL;
@"JFXEffectAssetAttributes" _attributes;
```

## Properties

```
@property (T@"NSString",R,N,V_assetID) assetID;
@property (T@"NSURL",R,N,V_localURL) localURL;
@property (T@"JFXEffectAssetAttributes",R,N,V_attributes) attributes;
@property (TB,R,N,V_contentUpdateAvailable) contentUpdateAvailable;
```

## Class methods

```
+[JFXEffectAsset firstAssetInAssets:matchingFilterAttributes:];
```

## Instance methods

```
-[JFXEffectAsset localURL];
-[JFXEffectAsset hash];
-[JFXEffectAsset description];
-[JFXEffectAsset attributes];
-[JFXEffectAsset isEqual:];
-[JFXEffectAsset assetID];
-[JFXEffectAsset contentUpdateAvailable];
-[JFXEffectAsset initWithAssetID:URL:copyOfAttributes:];
-[JFXEffectAsset initWithAssetID:URL:copyOfAttributes:contentUpdateAvailable:];
```
