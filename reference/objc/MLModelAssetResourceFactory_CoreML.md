# `MLModelAssetResourceFactory`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _modelLoadQueue;
@"NSObject<OS_dispatch_queue>" _descriptionLoadQueue;
@"NSObject<OS_dispatch_queue>" _structureLoadQueue;
@"<MLModelAssetResourceFactoryImpl>" _impl;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_modelLoadQueue) modelLoadQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_descriptionLoadQueue) descriptionLoadQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_structureLoadQueue) structureLoadQueue;
@property (T@"<MLModelAssetResourceFactoryImpl>",R,N,V_impl) impl;
@property (T@"NSURL",R,C,N) compiledModelURL;
```

## Class methods

```
+[MLModelAssetResourceFactory resourceFactoryWithArchiveData:];
+[MLModelAssetResourceFactory resourceFactoryWithModelURL:error:];
```

## Instance methods

```
-[MLModelAssetResourceFactory impl];
-[MLModelAssetResourceFactory initWithImpl:];
-[MLModelAssetResourceFactory compiledModelURL];
-[MLModelAssetResourceFactory modelAssetDescriptionWithCompletionHandler:];
-[MLModelAssetResourceFactory modelLoadQueue];
-[MLModelAssetResourceFactory structureLoadQueue];
-[MLModelAssetResourceFactory modelStructureWithCompletionHandler:];
-[MLModelAssetResourceFactory descriptionLoadQueue];
-[MLModelAssetResourceFactory modelWithConfiguration:completionHandler:];
-[MLModelAssetResourceFactory modelWithConfiguration:error:];
```
