# `ASAccessoryExperenceRequest`

- Image: [`/System/Library/PrivateFrameworks/AccessorySetupKitCore.framework/AccessorySetupKitCore`](../userland/System__Library__PrivateFrameworks__AccessorySetupKitCore.framework__AccessorySetupKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
q type;
? overrideBundleID;
q targetBundleType;
@"DADevice" device;
@"ASAccessoryAssetDescriptor" assetDescriptor;
? customTitle;
? customSubtitle;
```

## Properties

```
@property (Tq,N,R,Vtype) type;
@property (T@"NSString",N,C) overrideBundleID;
@property (Tq,N,VtargetBundleType) targetBundleType;
@property (T@"DADevice",N,R,Vdevice) device;
@property (T@"ASAccessoryAssetDescriptor",N,R,VassetDescriptor) assetDescriptor;
@property (T@"NSString",N,R) customTitle;
@property (T@"NSString",N,R) customSubtitle;
```

## Instance methods

```
-[ASAccessoryExperenceRequest device];
-[ASAccessoryExperenceRequest init];
-[ASAccessoryExperenceRequest type];
-[ASAccessoryExperenceRequest customTitle];
-[ASAccessoryExperenceRequest assetDescriptor];
-[ASAccessoryExperenceRequest customSubtitle];
-[ASAccessoryExperenceRequest initWithType:customTitle:customSubtitle:assetDescriptor:];
-[ASAccessoryExperenceRequest initWithType:device:assetDescriptor:];
-[ASAccessoryExperenceRequest overrideBundleID];
-[ASAccessoryExperenceRequest setOverrideBundleID:];
-[ASAccessoryExperenceRequest setTargetBundleType:];
-[ASAccessoryExperenceRequest targetBundleType];
```
