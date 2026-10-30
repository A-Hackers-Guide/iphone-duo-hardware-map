# `MLTreeEnsembleClassifier`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLClassifier`
- Protocols: `MLModelSpecificationLoader`, `MLCompiledModelLoader`, `MLSpecificationCompiler`
- 8 instance variables, 4 properties, 5 instance methods, 6 class methods

## Instance variables

```
{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}} _cached_model;
@"NSData" _model_data;
Q num_dimensions;
{vector<std::string, std::allocator<std::string>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _classes_by_string;
{vector<long long, std::allocator<long long>>="__begin_"^q"__end_"^q""{?="__cap_"^q}} _classes_by_int64_t;
q _class_type;
@"NSArray" _class_values;
@"NSString" _single_array_key;
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
+[MLTreeEnsembleClassifier loadModelFromSpecificationWithCompilationOptions:options:error:];
+[MLTreeEnsembleClassifier _convertStringClassVector:int64ClassVector:dimensions:toClassLabel:classType:andReturnError:];
+[MLTreeEnsembleClassifier compileSpecification:toArchive:options:error:];
+[MLTreeEnsembleClassifier compiledVersionForSpecification:options:error:];
+[MLTreeEnsembleClassifier loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLTreeEnsembleClassifier loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLTreeEnsembleClassifier _buildClassificationClasses:topk:error:];
-[MLTreeEnsembleClassifier _setSingleArrayLookupField];
-[MLTreeEnsembleClassifier prepareInput:error:];
-[MLTreeEnsembleClassifier modelData];
-[MLTreeEnsembleClassifier classify:options:error:];
```
