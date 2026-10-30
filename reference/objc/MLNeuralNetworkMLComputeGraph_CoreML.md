# `MLNeuralNetworkMLComputeGraph`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 39 instance methods, 1 class methods

## Instance variables

```
B _classifierOutputIsSigmoidOutput;
B _layerFusedToLoss;
@"MLCGraph" _graph;
@"MLCTrainingGraph" _trainingGraph;
@"MLCInferenceGraph" _inferenceGraph;
@"NSDictionary" _mlcInputs;
@"NSDictionary" _mlcLabels;
@"NSDictionary" _outputNameToLayerMap;
Q _executionOptions;
@"MLModelDescription" _modelDescription;
@"NSDictionary" _layersMap;
@"NSString" _fusedLayerInputName;
@"MLCDevice" _device;
```

## Properties

```
@property (T@"MLCGraph",&,N,V_graph) graph;
@property (T@"MLCTrainingGraph",&,N,V_trainingGraph) trainingGraph;
@property (T@"MLCInferenceGraph",&,N,V_inferenceGraph) inferenceGraph;
@property (T@"MLModelDescription",&,N,V_modelDescription) modelDescription;
@property (T@"NSDictionary",&,N,V_mlcInputs) mlcInputs;
@property (T@"NSDictionary",&,N,V_mlcLabels) mlcLabels;
@property (TQ,N,V_executionOptions) executionOptions;
@property (T@"NSDictionary",&,N,V_layersMap) layersMap;
@property (TB,N,V_layerFusedToLoss) layerFusedToLoss;
@property (T@"NSString",&,N,V_fusedLayerInputName) fusedLayerInputName;
@property (T@"MLCDevice",&,N,V_device) device;
@property (T@"NSDictionary",R,N,V_outputNameToLayerMap) outputNameToLayerMap;
@property (TB,N,V_classifierOutputIsSigmoidOutput) classifierOutputIsSigmoidOutput;
```

## Class methods

```
+[MLNeuralNetworkMLComputeGraph graphFromCompiledArchive:modelDescription:batchSize:numberOfClasses:computeUnits:error:];
```

## Instance methods

```
-[MLNeuralNetworkMLComputeGraph graph];
-[MLNeuralNetworkMLComputeGraph setDevice:];
-[MLNeuralNetworkMLComputeGraph executionOptions];
-[MLNeuralNetworkMLComputeGraph device];
-[MLNeuralNetworkMLComputeGraph setGraph:];
-[MLNeuralNetworkMLComputeGraph setExecutionOptions:];
-[MLNeuralNetworkMLComputeGraph modelDescription];
-[MLNeuralNetworkMLComputeGraph setClassifierOutputIsSigmoidOutput:];
-[MLNeuralNetworkMLComputeGraph classifierOutputIsSigmoidOutput];
-[MLNeuralNetworkMLComputeGraph buildGraphsFor:batchSize:numberOfClasses:error:];
-[MLNeuralNetworkMLComputeGraph buildInferenceGraph:updateParams:layers:mlcTensorByName:outputNameToLayerMap:error:];
-[MLNeuralNetworkMLComputeGraph buildMLComputeTensorDescriptorWith:featureName:batchSize:numberOfClasses:error:];
-[MLNeuralNetworkMLComputeGraph buildTrainingGraphFrom:updateParams:numberOfClasses:mlcTensorByName:error:];
-[MLNeuralNetworkMLComputeGraph copyWeightsFrom:to:error:];
-[MLNeuralNetworkMLComputeGraph createMultiArrayFromTensor:error:];
-[MLNeuralNetworkMLComputeGraph fusedLayerInputName];
-[MLNeuralNetworkMLComputeGraph getBiasesForLayerNamed:error:];
-[MLNeuralNetworkMLComputeGraph getWeightsForLayerNamed:error:];
-[MLNeuralNetworkMLComputeGraph inferenceGraph];
-[MLNeuralNetworkMLComputeGraph initWithCompiledArchive:modelDescription:batchSize:numberOfClasses:computeUnits:error:];
-[MLNeuralNetworkMLComputeGraph inputTensorMapWithBatchSize:numberOfClasses:error:];
-[MLNeuralNetworkMLComputeGraph labelTensorMapWithBatchSize:numberOfClasses:error:];
-[MLNeuralNetworkMLComputeGraph layerFusedToLoss];
-[MLNeuralNetworkMLComputeGraph layersMap];
-[MLNeuralNetworkMLComputeGraph lossInputsFromUpdateParams:];
-[MLNeuralNetworkMLComputeGraph mlcDeviceTypeForComputeUnit:];
-[MLNeuralNetworkMLComputeGraph mlcInputs];
-[MLNeuralNetworkMLComputeGraph mlcLabels];
-[MLNeuralNetworkMLComputeGraph outputNameToLayerMap];
-[MLNeuralNetworkMLComputeGraph saveUpdatedWeightsTo:error:];
-[MLNeuralNetworkMLComputeGraph setFusedLayerInputName:];
-[MLNeuralNetworkMLComputeGraph setInferenceGraph:];
-[MLNeuralNetworkMLComputeGraph setLayerFusedToLoss:];
-[MLNeuralNetworkMLComputeGraph setLayersMap:];
-[MLNeuralNetworkMLComputeGraph setMlcInputs:];
-[MLNeuralNetworkMLComputeGraph setMlcLabels:];
-[MLNeuralNetworkMLComputeGraph setModelDescription:];
-[MLNeuralNetworkMLComputeGraph setTrainingGraph:];
-[MLNeuralNetworkMLComputeGraph trainingGraph];
```
