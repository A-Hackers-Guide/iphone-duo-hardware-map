# `MLPipelineLoader`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLModelAssetDescriptionLoader`, `MLCompiledModelLoader`
- 0 instance variables, 4 properties, 0 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLPipelineLoader ensureFrameworkSupportsCompilerVersion:error:];
+[MLPipelineLoader loadModelAssetDescriptionFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLPipelineLoader loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```
