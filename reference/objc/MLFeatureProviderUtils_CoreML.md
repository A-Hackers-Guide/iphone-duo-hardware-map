# `MLFeatureProviderUtils`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 9 class methods

## Class methods

```
+[MLFeatureProviderUtils _vectorizeWithoutSizeCheckFeatureValues:intoDoubleVector:stride:error:];
+[MLFeatureProviderUtils _vectorizedSizeOfFeatureValues:error:];
+[MLFeatureProviderUtils canVectorizeAllFeaturesWithDescriptions:];
+[MLFeatureProviderUtils lazyProviderWithFeaturesProvidedBy:addedToFeaturesProvidedBy:];
+[MLFeatureProviderUtils _featureValuesForNames:providedBy:error:];
+[MLFeatureProviderUtils canVectorizeFeatureWithDescription:];
+[MLFeatureProviderUtils vectorizeFeaturesProvidedBy:featureNames:intoDoubleVector:length:stride:error:];
+[MLFeatureProviderUtils vectorizeFeaturesProvidedBy:featureNames:error:];
+[MLFeatureProviderUtils providerWithSubsetOfFeaturesNamed:providedBy:];
```
