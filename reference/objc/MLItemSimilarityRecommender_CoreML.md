# `MLItemSimilarityRecommender`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`, `MLModeling`, `MLCompiledModelLoader`, `MLSpecificationCompiler`
- 18 instance variables, 11 properties, 4 instance methods, 5 class methods

## Instance variables

```
{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}} m_cached_model;
@"NSData" m_model_data;
Q m_num_items;
@"NSString" m_item_data_feature_name;
@"NSString" m_num_recommendations_feature_name;
@"NSString" m_item_restriction_feature_name;
@"NSString" m_item_exclusion_feature_name;
@"NSString" m_item_list_output_feature_name;
@"NSString" m_item_score_output_feature_name;
@"NSDictionary" m_item_mapping;
@"NSArray" m_item_string_list;
@"NSArray" m_item_integer_list;
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} _m_scores;
{vector<unsigned long long, std::allocator<unsigned long long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _m_items;
{vector<unsigned long long, std::allocator<unsigned long long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _m_item_buffer;
{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}} _m_item_invalid_mask;
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} _m_item_predictions;
{vector<std::pair<unsigned long long, double>, std::allocator<std::pair<unsigned long long, double>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _m_item_heap;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
```

## Class methods

```
+[MLItemSimilarityRecommender loadModelFromSpecificationWithCompilationOptions:options:error:];
+[MLItemSimilarityRecommender compileSpecification:toArchive:options:error:];
+[MLItemSimilarityRecommender compiledVersionForSpecification:options:error:];
+[MLItemSimilarityRecommender loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLItemSimilarityRecommender loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLItemSimilarityRecommender modelData];
-[MLItemSimilarityRecommender predictionFromFeatures:options:error:];
-[MLItemSimilarityRecommender _itemForIndex:error:];
-[MLItemSimilarityRecommender _mapItemSequence:dest:error:];
```
