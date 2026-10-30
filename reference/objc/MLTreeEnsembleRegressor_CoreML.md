# `MLTreeEnsembleRegressor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLRegressor`
- Protocols: `MLModelSpecificationLoader`, `MLCompiledModelLoader`, `MLSpecificationCompiler`
- 4 instance variables, 4 properties, 5 instance methods, 5 class methods

## Instance variables

```
@"NSData" _model_data;
{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}} _cached_model;
Q num_dimensions;
@"NSArray" output_classes;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLTreeEnsembleRegressor loadModelFromSpecificationWithCompilationOptions:options:error:];
+[MLTreeEnsembleRegressor compileSpecification:toArchive:options:error:];
+[MLTreeEnsembleRegressor compiledVersionForSpecification:options:error:];
+[MLTreeEnsembleRegressor loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLTreeEnsembleRegressor loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLTreeEnsembleRegressor regress:options:error:];
-[MLTreeEnsembleRegressor scalarRegress:error:];
-[MLTreeEnsembleRegressor modelData];
-[MLTreeEnsembleRegressor scalarRegress:];
-[MLTreeEnsembleRegressor vectorRegress:dest:];
```
