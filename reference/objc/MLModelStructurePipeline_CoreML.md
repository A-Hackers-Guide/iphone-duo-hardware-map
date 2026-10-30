# `MLModelStructurePipeline`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _subModelNames;
@"NSArray" _subModels;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_subModelNames) subModelNames;
@property (T@"NSArray",R,C,N,V_subModels) subModels;
```

## Class methods

```
+[MLModelStructurePipeline loadModelStructureFromCompiledArchive:modelVersionInfo:compilerVersionInfo:path:error:];
```

## Instance methods

```
-[MLModelStructurePipeline initWithSubModelNames:subModels:];
-[MLModelStructurePipeline subModelNames];
-[MLModelStructurePipeline subModels];
```
