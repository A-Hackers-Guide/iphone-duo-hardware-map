# `MLKNearestNeighborsClassifierParameters`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _numberOfDimensions;
q _weightingScheme;
q _indexType;
Q _leafSize;
@"NSObject" _defaultLabel;
@"NSString" _nearestLabelsFeatureName;
@"NSString" _nearestDistancesFeatureName;
```

## Properties

```
@property (TQ,V_numberOfDimensions) numberOfDimensions;
@property (Tq,V_weightingScheme) weightingScheme;
@property (Tq,V_indexType) indexType;
@property (TQ,V_leafSize) leafSize;
@property (T@"NSObject",&,V_defaultLabel) defaultLabel;
@property (T@"NSString",&,V_nearestLabelsFeatureName) nearestLabelsFeatureName;
@property (T@"NSString",&,V_nearestDistancesFeatureName) nearestDistancesFeatureName;
```

## Instance methods

```
-[MLKNearestNeighborsClassifierParameters indexType];
-[MLKNearestNeighborsClassifierParameters setIndexType:];
-[MLKNearestNeighborsClassifierParameters setWeightingScheme:];
-[MLKNearestNeighborsClassifierParameters weightingScheme];
-[MLKNearestNeighborsClassifierParameters setNearestDistancesFeatureName:];
-[MLKNearestNeighborsClassifierParameters defaultLabel];
-[MLKNearestNeighborsClassifierParameters leafSize];
-[MLKNearestNeighborsClassifierParameters nearestDistancesFeatureName];
-[MLKNearestNeighborsClassifierParameters nearestLabelsFeatureName];
-[MLKNearestNeighborsClassifierParameters numberOfDimensions];
-[MLKNearestNeighborsClassifierParameters setDefaultLabel:];
-[MLKNearestNeighborsClassifierParameters setLeafSize:];
-[MLKNearestNeighborsClassifierParameters setNearestLabelsFeatureName:];
-[MLKNearestNeighborsClassifierParameters setNumberOfDimensions:];
```
