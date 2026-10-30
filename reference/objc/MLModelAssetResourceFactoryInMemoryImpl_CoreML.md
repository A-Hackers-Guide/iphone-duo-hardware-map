# `MLModelAssetResourceFactoryInMemoryImpl`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLModelAssetResourceFactoryImpl`
- 1 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<_MLModelInputArchiver, std::default_delete<_MLModelInputArchiver>>=""{?="__ptr_"^{_MLModelInputArchiver}}} _inputArchiver;
```

## Properties

```
@property (T@"NSURL",R,C,N) compiledModelURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLModelAssetResourceFactoryInMemoryImpl compiledModelURL];
-[MLModelAssetResourceFactoryInMemoryImpl initWithArchiveData:];
-[MLModelAssetResourceFactoryInMemoryImpl modelStructureWithError:];
-[MLModelAssetResourceFactoryInMemoryImpl modelAssetDescriptionWithError:];
-[MLModelAssetResourceFactoryInMemoryImpl modelWithConfiguration:error:];
```
