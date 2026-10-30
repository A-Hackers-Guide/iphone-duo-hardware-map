# `MLDataConversionUtils`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 12 class methods

## Class methods

```
+[MLDataConversionUtils batchProviderFromEspressoDataProvider:neuralNetworkEngine:options:error:];
+[MLDataConversionUtils batchProviderFromMLComputeDataProvider:neuralNetworkEngine:options:error:];
+[MLDataConversionUtils espressoDataProviderFromBatchProvider:forPrediction:neuralNetworkEngine:error:];
+[MLDataConversionUtils espressoDataProviderFromFeatureProvider:forPrediction:neuralNetworkEngine:error:];
+[MLDataConversionUtils featureProviderFomMLComputeDataProvider:neuralNetworkEngine:options:error:];
+[MLDataConversionUtils featureProviderFromEspressoDataProvider:neuralNetworkEngine:options:error:];
+[MLDataConversionUtils mlComputeDataProviderFromBatchProvider:batchSize:forPrediction:neuralNetworkEngine:error:];
+[MLDataConversionUtils mlComputeDataTypeSize:];
+[MLDataConversionUtils populateEspressoShapeAndStridesFromInputShape:ndRepresentation:espressoShape:espressoStrides:error:];
+[MLDataConversionUtils populateShapeAndStrideFor:inputShape:outputShape:outputStrides:error:];
+[MLDataConversionUtils sizeFromShape:];
+[MLDataConversionUtils stridesForShape:];
```
