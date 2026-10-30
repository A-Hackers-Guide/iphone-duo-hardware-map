# `MLModelAssetResourceFactoryOnDiskImpl`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLModelAssetResourceFactoryImpl`
- 1 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _modelURL;
```

## Properties

```
@property (T@"NSURL",R,N,V_modelURL) modelURL;
@property (T@"NSURL",R,C,N) compiledModelURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLModelAssetResourceFactoryOnDiskImpl compiledModelURL];
-[MLModelAssetResourceFactoryOnDiskImpl modelStructureWithError:];
-[MLModelAssetResourceFactoryOnDiskImpl initWithModelURL:error:];
-[MLModelAssetResourceFactoryOnDiskImpl modelAssetDescriptionWithError:];
-[MLModelAssetResourceFactoryOnDiskImpl modelURL];
-[MLModelAssetResourceFactoryOnDiskImpl modelWithConfiguration:error:];
```
