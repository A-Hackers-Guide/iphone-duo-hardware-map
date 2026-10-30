# `MLLocalOutlierFactor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- 5 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<MLNearestNeighborsIndex>" _index;
Q _numberOfDimensions;
Q _numberOfNeighbors;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} _cachedKDistances;
@"MLParameterContainer" _parameterContainer;
```

## Instance methods

```
-[MLLocalOutlierFactor parameterValueForKey:error:];
-[MLLocalOutlierFactor predictionFromFeatures:options:error:];
-[MLLocalOutlierFactor computeLOFForQueryPoint:];
-[MLLocalOutlierFactor findNearestNeighborsToIndex:];
-[MLLocalOutlierFactor findNearestNeighborsToQueryPoint:];
-[MLLocalOutlierFactor initWithKNearestNeighborsModelAtURL:configuration:error:];
-[MLLocalOutlierFactor inputMultiArray:error:];
-[MLLocalOutlierFactor kDistanceToIndex:];
-[MLLocalOutlierFactor localReachabilityDensityForIndex:];
-[MLLocalOutlierFactor localReachabilityDensityForQeuryPoint:];
-[MLLocalOutlierFactor localReachabilityDensityOfNeighbors:];
-[MLLocalOutlierFactor updateToValidDistance:];
```
