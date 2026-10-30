# `CAMSmartStyleSettingsResourceLoadResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"PICompositionController" _compositionController;
@"<PEAsset>" _asset;
@"NSURL" _fileURL;
@"NSDictionary" _fileURLImageProperties;
@"NSString" _logIdentifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropRect;
```

## Properties

```
@property (T@"PICompositionController",R,N,V_compositionController) compositionController;
@property (T@"<PEAsset>",R,N,V_asset) asset;
@property (T@"NSURL",R,N,V_fileURL) fileURL;
@property (T@"NSDictionary",R,N,V_fileURLImageProperties) fileURLImageProperties;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cropRect) cropRect;
@property (T@"NSString",R,C,N,V_logIdentifier) logIdentifier;
```

## Instance methods

```
-[CAMSmartStyleSettingsResourceLoadResult asset];
-[CAMSmartStyleSettingsResourceLoadResult fileURL];
-[CAMSmartStyleSettingsResourceLoadResult cropRect];
-[CAMSmartStyleSettingsResourceLoadResult logIdentifier];
-[CAMSmartStyleSettingsResourceLoadResult compositionController];
-[CAMSmartStyleSettingsResourceLoadResult fileURLImageProperties];
-[CAMSmartStyleSettingsResourceLoadResult initWithCompositionController:fileURL:imageProperties:cropRect:logIdentifier:];
-[CAMSmartStyleSettingsResourceLoadResult initWithResourceLoadResult:logIdentifier:];
```
