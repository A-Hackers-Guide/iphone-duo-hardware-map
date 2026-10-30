# `MLModelAssetModelVendor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"MLModelAssetResourceFactory" _resourceFactory;
@"MLModelConfiguration" _cachedConfiguration;
@"MLModel" _cachedModel;
```

## Properties

```
@property (T@"MLModelAssetResourceFactory",R,N,V_resourceFactory) resourceFactory;
@property (T@"MLModelConfiguration",C,N,V_cachedConfiguration) cachedConfiguration;
@property (T@"MLModel",&,N,V_cachedModel) cachedModel;
```

## Instance methods

```
-[MLModelAssetModelVendor cachedConfiguration];
-[MLModelAssetModelVendor cachedModel];
-[MLModelAssetModelVendor resourceFactory];
-[MLModelAssetModelVendor setCachedConfiguration:];
-[MLModelAssetModelVendor setCachedModel:];
-[MLModelAssetModelVendor modelWithConfiguration:completionHandler:];
-[MLModelAssetModelVendor initWithResourceFactory:];
-[MLModelAssetModelVendor modelWithConfiguration:error:];
```
