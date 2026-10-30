# `CFXMediaItemAdjustmentsData`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 7 instance methods, 2 class methods

## Instance variables

```
q _cameraMode;
@"NSURL" _metadataURL;
q _cameraPosition;
@"NSArray" _effectStack;
```

## Properties

```
@property (Tq,R,N,V_cameraMode) cameraMode;
@property (T@"NSURL",R,N,V_metadataURL) metadataURL;
@property (Tq,R,N,V_cameraPosition) cameraPosition;
@property (T@"NSArray",R,N,V_effectStack) effectStack;
```

## Class methods

```
+[CFXMediaItemAdjustmentsData supportsSecureCoding];
+[CFXMediaItemAdjustmentsData secureCodingClassWhitelist];
```

## Instance methods

```
-[CFXMediaItemAdjustmentsData metadataURL];
-[CFXMediaItemAdjustmentsData encodeWithCoder:];
-[CFXMediaItemAdjustmentsData initWithCoder:];
-[CFXMediaItemAdjustmentsData cameraMode];
-[CFXMediaItemAdjustmentsData cameraPosition];
-[CFXMediaItemAdjustmentsData effectStack];
-[CFXMediaItemAdjustmentsData initWithCameraMode:metadataURL:cameraPosition:effectStack:];
```
