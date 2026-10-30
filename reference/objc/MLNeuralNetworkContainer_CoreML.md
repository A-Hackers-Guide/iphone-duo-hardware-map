# `MLNeuralNetworkContainer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 33 instance variables, 28 properties, 57 instance methods, 3 class methods

## Instance variables

```
{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>="__tree_"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} widths;
{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>="__tree_"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} heights;
{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>="__tree_"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} ks;
{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>="__tree_"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} batches;
{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>="__tree_"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} sequences;
{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>="__tree_"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} ranks;
B _hasBidirectionalLayer;
B _hasOptionalInputSequenceConcat;
B _hasDynamicLayer;
B _ndArrayInterpretation;
B _modelIsEncrypted;
B _modelIsMIL;
B _modelIsTrainingProgram;
i _precision;
i _engine;
@"NSString" _modelFilePath;
@"NSArray" _inputLayerNames;
@"NSArray" _outputLayerNames;
@"NSString" _name;
@"NSDictionary" _inputDescription;
@"NSDictionary" _outputDescription;
@"NSDictionary" _imageParameters;
@"NSDictionary" _imagePreprocessingParams;
@"NSArray" _configurationList;
@"NSArray" _classLabels;
@"NSString" _classScoreVectorName;
@"MLModelDescription" _modelDescription;
@"MLNeuralNetworksCompileTimeParams" _updatableModelCompiledParams;
@"NSDictionary" _optionalInputDefaultValues;
@"MLVersionInfo" _modelVersionInfo;
@"NSDictionary" _optionalInputTypes;
@"MLVersionInfo" _compilerVersionInfo;
@"MLCompilerNeuralNetworkOutput" _compilerOutput;
```

## Properties

```
@property (Ti,N,V_precision) precision;
@property (Ti,N,V_engine) engine;
@property (T@"NSArray",&,N,V_outputLayerNames) outputLayerNames;
@property (T@"NSArray",&,N,V_inputLayerNames) inputLayerNames;
@property (T@"NSDictionary",&,N,V_optionalInputTypes) optionalInputTypes;
@property (T@"MLVersionInfo",&,N,V_compilerVersionInfo) compilerVersionInfo;
@property (T@"NSString",R,N) activeFunction;
@property (T@"MLCompilerNeuralNetworkOutput",&,N,V_compilerOutput) compilerOutput;
@property (T@"NSString",&,N,V_modelFilePath) modelFilePath;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSDictionary",&,N,V_inputDescription) inputDescription;
@property (T@"NSDictionary",&,N,V_outputDescription) outputDescription;
@property (T@"NSDictionary",&,N,V_imageParameters) imageParameters;
@property (T@"NSDictionary",&,N,V_imagePreprocessingParams) imagePreprocessingParams;
@property (T@"NSArray",&,N,V_configurationList) configurationList;
@property (TB,N,V_hasBidirectionalLayer) hasBidirectionalLayer;
@property (TB,N,V_hasOptionalInputSequenceConcat) hasOptionalInputSequenceConcat;
@property (TB,N,V_hasDynamicLayer) hasDynamicLayer;
@property (T@"NSArray",&,V_classLabels) classLabels;
@property (T@"NSString",&,V_classScoreVectorName) classScoreVectorName;
@property (T@"MLModelDescription",R,C,N,V_modelDescription) modelDescription;
@property (TB,V_ndArrayInterpretation) ndArrayInterpretation;
@property (T@"MLNeuralNetworksCompileTimeParams",&,N,V_updatableModelCompiledParams) updatableModelCompiledParams;
@property (T@"NSDictionary",&,N,V_optionalInputDefaultValues) optionalInputDefaultValues;
@property (TB,N,V_modelIsEncrypted) modelIsEncrypted;
@property (T@"MLVersionInfo",&,N,V_modelVersionInfo) modelVersionInfo;
@property (TB,N,V_modelIsMIL) modelIsMIL;
@property (TB,N,V_modelIsTrainingProgram) modelIsTrainingProgram;
```

## Class methods

```
+[MLNeuralNetworkContainer containerFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLNeuralNetworkContainer containerFromCompiledArchiveCommon:filename:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLNeuralNetworkContainer containerFromFilePath:inputLayerNames:outputLayerNames:parameters:];
```

## Instance methods

```
-[MLNeuralNetworkContainer classLabels];
-[MLNeuralNetworkContainer setEngine:];
-[MLNeuralNetworkContainer precision];
-[MLNeuralNetworkContainer setModelIsEncrypted:];
-[MLNeuralNetworkContainer engine];
-[MLNeuralNetworkContainer setImageParameters:];
-[MLNeuralNetworkContainer compilerOutput];
-[MLNeuralNetworkContainer optionalInputTypes];
-[MLNeuralNetworkContainer imageParameters];
-[MLNeuralNetworkContainer modelDescription];
-[MLNeuralNetworkContainer setName:];
-[MLNeuralNetworkContainer activeFunction];
-[MLNeuralNetworkContainer modelIsEncrypted];
-[MLNeuralNetworkContainer classScoreVectorName];
-[MLNeuralNetworkContainer modelVersionInfo];
-[MLNeuralNetworkContainer compilerVersionInfo];
-[MLNeuralNetworkContainer name];
-[MLNeuralNetworkContainer setClassLabels:];
-[MLNeuralNetworkContainer hasDynamicLayer];
-[MLNeuralNetworkContainer inputLayerNames];
-[MLNeuralNetworkContainer configurationList];
-[MLNeuralNetworkContainer hasBidirectionalLayer];
-[MLNeuralNetworkContainer hasOptionalInputSequenceConcat];
-[MLNeuralNetworkContainer imagePreprocessingParams];
-[MLNeuralNetworkContainer initWithFeatureDescriptions:modelDescription:outputLayerNames:classScoreVectorName:classLabels:isEncrypted:modelVersionInfo:];
-[MLNeuralNetworkContainer initWithFeatureDescriptions:modelDescription:outputLayerNames:classScoreVectorName:classLabels:isEncrypted:modelVersionInfo:compilerVersionInfo:];
-[MLNeuralNetworkContainer initWithFilePath:inputLayerNames:outputLayerNames:parameters:];
-[MLNeuralNetworkContainer inputDescription];
-[MLNeuralNetworkContainer modelFilePath];
-[MLNeuralNetworkContainer modelIsMIL];
-[MLNeuralNetworkContainer modelIsTrainingProgram];
-[MLNeuralNetworkContainer ndArrayInterpretation];
-[MLNeuralNetworkContainer optionalInputDefaultValues];
-[MLNeuralNetworkContainer outputDescription];
-[MLNeuralNetworkContainer outputLayerNames];
-[MLNeuralNetworkContainer setClassScoreVectorName:];
-[MLNeuralNetworkContainer setCompilerOutput:];
-[MLNeuralNetworkContainer setCompilerVersionInfo:];
-[MLNeuralNetworkContainer setConfigurationList:];
-[MLNeuralNetworkContainer setHasBidirectionalLayer:];
-[MLNeuralNetworkContainer setHasDynamicLayer:];
-[MLNeuralNetworkContainer setHasOptionalInputSequenceConcat:];
-[MLNeuralNetworkContainer setImagePreprocessingParams:];
-[MLNeuralNetworkContainer setInputDescription:];
-[MLNeuralNetworkContainer setInputLayerNames:];
-[MLNeuralNetworkContainer setModelFilePath:];
-[MLNeuralNetworkContainer setModelIsMIL:];
-[MLNeuralNetworkContainer setModelIsTrainingProgram:];
-[MLNeuralNetworkContainer setModelVersionInfo:];
-[MLNeuralNetworkContainer setNdArrayInterpretation:];
-[MLNeuralNetworkContainer setOptionalInputDefaultValues:];
-[MLNeuralNetworkContainer setOptionalInputTypes:];
-[MLNeuralNetworkContainer setOutputDescription:];
-[MLNeuralNetworkContainer setOutputLayerNames:];
-[MLNeuralNetworkContainer setPrecision:];
-[MLNeuralNetworkContainer setUpdatableModelCompiledParams:];
-[MLNeuralNetworkContainer updatableModelCompiledParams];
```
