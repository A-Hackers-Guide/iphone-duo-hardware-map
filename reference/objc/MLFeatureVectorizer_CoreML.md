# `MLFeatureVectorizer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 4 instance variables, 6 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _output_array_shape;
{vector<std::pair<unsigned long, unsigned long>, std::allocator<std::pair<unsigned long, unsigned long>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} index_mapping;
@"NSArray" _columnNameEncoding;
@"NSArray" _dimensionEncoding;
```

## Properties

```
@property (T@"NSArray",R,N,V_columnNameEncoding) columnNameEncoding;
@property (T@"NSArray",R,N,V_dimensionEncoding) dimensionEncoding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLFeatureVectorizer loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLFeatureVectorizer predictionTypeForKTrace];
-[MLFeatureVectorizer vectorizeOneHotEncoderDict:index:error:];
-[MLFeatureVectorizer initWith:dimensionEncoding:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
-[MLFeatureVectorizer columnNameEncoding];
-[MLFeatureVectorizer dimensionEncoding];
-[MLFeatureVectorizer predictionFromFeatures:options:error:];
```
