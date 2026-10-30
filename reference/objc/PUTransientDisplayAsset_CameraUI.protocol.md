# `PUTransientDisplayAsset` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `PUDisplayAsset`
- 0 instance variables, 5 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSURL",R,C,N) persistenceURL;
@property (TB,R,N,GisHDR) HDR;
@property (T@"NSString",R,C,N) burstIdentifier;
@property (TQ,R,N) numberOfRepresentedAssets;
@property (T@"UIImage",R,N) placeholderImage;
```

## Instance methods

```
-[PUTransientDisplayAsset isHDR];
-[PUTransientDisplayAsset persistenceURL];
-[PUTransientDisplayAsset burstIdentifier];
-[PUTransientDisplayAsset placeholderImage];
-[PUTransientDisplayAsset numberOfRepresentedAssets];
```
