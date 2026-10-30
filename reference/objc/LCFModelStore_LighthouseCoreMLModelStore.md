# `LCFModelStore`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLModelStore.framework__LighthouseCoreMLModelStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _key;
@"NSURL" _modelStoreRootURL;
@"NSURL" _emptyModelURL;
@"LCFModelStoreModelMetadataProvider" _modelMetadataProvider;
@"NSURL" _originalEmptyModelURL;
@"NSURL" _modelStoreRootWithKeyURL;
```

## Properties

```
@property (T@"NSURL",R,N,V_originalEmptyModelURL) originalEmptyModelURL;
@property (T@"NSURL",R,N,V_modelStoreRootWithKeyURL) modelStoreRootWithKeyURL;
@property (T@"NSString",R,N,V_key) key;
@property (T@"NSURL",R,N,V_modelStoreRootURL) modelStoreRootURL;
@property (T@"NSURL",R,N,V_emptyModelURL) emptyModelURL;
@property (T@"LCFModelStoreModelMetadataProvider",R,N,V_modelMetadataProvider) modelMetadataProvider;
```

## Instance methods

```
-[LCFModelStore clear];
-[LCFModelStore key];
-[LCFModelStore getModelConfig:];
-[LCFModelStore getModelURL:];
-[LCFModelStore init:modelStoreRootURL:];
-[LCFModelStore deleteModel:];
-[LCFModelStore emptyModelURL];
-[LCFModelStore getBaseModelURL:modelConfig:];
-[LCFModelStore getModelMetadata:];
-[LCFModelStore init:modelStoreRootURL:originalEmptyModelURL:];
-[LCFModelStore listModelNames];
-[LCFModelStore markModelTrained:];
-[LCFModelStore modelMetadataProvider];
-[LCFModelStore modelStoreRootURL];
-[LCFModelStore modelStoreRootWithKeyURL];
-[LCFModelStore originalEmptyModelURL];
-[LCFModelStore setModelMetadata:key:value:];
-[LCFModelStore storeModel:];
-[LCFModelStore storeModel:modelConfig:];
```
