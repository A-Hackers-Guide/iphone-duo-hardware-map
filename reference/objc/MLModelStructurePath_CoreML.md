# `MLModelStructurePath`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
{Path="m_components"{vector<std::variant<CoreML::ModelStructure::Path::Root, CoreML::ModelStructure::Path::Program, CoreML::ModelStructure::Path::Program::Function, CoreML::ModelStructure::Path::Program::Block, CoreML::ModelStructure::Path::Program::Operation, CoreML::ModelStructure::Path::NeuralNetwork, CoreML::ModelStructure::Path::NeuralNetwork::Layer, CoreML::ModelStructure::Path::Pipeline, CoreML::ModelStructure::Path::Pipeline::SubModel>, std::allocator<std::variant<CoreML::ModelStructure::Path::Root, CoreML::ModelStructure::Path::Program, CoreML::ModelStructure::Path::Program::Function, CoreML::ModelStructure::Path::Program::Block, CoreML::ModelStructure::Path::Program::Operation, CoreML::ModelStructure::Path::NeuralNetwork, CoreML::ModelStructure::Path::NeuralNetwork::Layer, CoreML::ModelStructure::Path::Pipeline, CoreML::ModelStructure::Path::Pipeline::SubModel>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}} _cppPath;
```

## Properties

```
@property (T{Path={vector<std::variant<CoreML::ModelStructure::Path::Root, CoreML::ModelStructure::Path::Program, CoreML::ModelStructure::Path::Program::Function, CoreML::ModelStructure::Path::Program::Block, CoreML::ModelStructure::Path::Program::Operation, CoreML::ModelStructure::Path::NeuralNetwork, CoreML::ModelStructure::Path::NeuralNetwork::Layer, CoreML::ModelStructure::Path::Pipeline, CoreML::ModelStructure::Path::Pipeline::SubModel>, std::allocator<std::variant<CoreML::ModelStructure::Path::Root, CoreML::ModelStructure::Path::Program, CoreML::ModelStructure::Path::Program::Function, CoreML::ModelStructure::Path::Program::Block, CoreML::ModelStructure::Path::Program::Operation, CoreML::ModelStructure::Path::NeuralNetwork, CoreML::ModelStructure::Path::NeuralNetwork::Layer, CoreML::ModelStructure::Path::Pipeline, CoreML::ModelStructure::Path::Pipeline::SubModel>>>=^v^v{?=^v}}},R,N,V_cppPath) cppPath;
@property (T@"NSArray",R,C,N) components;
@property (TB,R,N) isNeuralNetworkLayerPath;
@property (TB,R,N) isMLProgramOperationPath;
```

## Instance methods

```
-[MLModelStructurePath components];
-[MLModelStructurePath hash];
-[MLModelStructurePath description];
-[MLModelStructurePath copyWithZone:];
-[MLModelStructurePath isEqual:];
-[MLModelStructurePath cppPath];
-[MLModelStructurePath initWithCppPath:];
-[MLModelStructurePath initWithMLProgramOperationPathComponents:scopedModelNames:error:];
-[MLModelStructurePath initWithNeuralNetworkLayerName:scopedModelNames:];
-[MLModelStructurePath isMLProgramOperationPath];
-[MLModelStructurePath isNeuralNetworkLayerPath];
```
