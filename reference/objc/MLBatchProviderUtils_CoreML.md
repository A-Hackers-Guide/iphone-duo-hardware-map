# `MLBatchProviderUtils`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 12 class methods

## Class methods

```
+[MLBatchProviderUtils batchFromConcatinatingBatches:];
+[MLBatchProviderUtils batchWithSubsetOfFeaturesNamed:fromBatch:];
+[MLBatchProviderUtils dictionaryFromBatch:];
+[MLBatchProviderUtils dictionaryFromBatch:featureNames:];
+[MLBatchProviderUtils featureDescriptionsByNameForBatch:error:];
+[MLBatchProviderUtils featureNamesInBatch:];
+[MLBatchProviderUtils featureProviderArrayFromBatch:];
+[MLBatchProviderUtils featureValueArrayForName:batch:error:];
+[MLBatchProviderUtils lazyBatchIndexIntoBatch:indices:error:];
+[MLBatchProviderUtils lazyBatchWindowIntoBatch:startIndex:windowLength:error:];
+[MLBatchProviderUtils lazyBatchWithFeaturesInBatch:addedToBatch:error:];
+[MLBatchProviderUtils vectorizeFeaturesNamed:fromBatch:intoRowsOfDoubleMatrix:error:];
```
