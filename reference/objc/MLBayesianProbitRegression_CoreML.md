# `MLBayesianProbitRegression`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLRegressor`
- Protocols: `MLSupervisedOnlineUpdatable`, `MLModelSpecificationLoader`, `MLModelSpecificationSaver`
- 9 instance variables, 4 properties, 25 instance methods, 4 class methods

## Instance variables

```
{shared_ptr<CoreML::BayesianProbitRegression::BayesianProbitRegression>="__ptr_"^{BayesianProbitRegression}"__cntrl_"^{__shared_weak_count}} _model;
@"NSString" _regressionInputFeatureName;
@"NSString" _optimismInputFeatureName;
@"NSString" _meanOutputFeatureName;
@"NSString" _varianceOutputFeatureName;
@"NSString" _pessimisticProbabilityOutputFeatureName;
@"NSString" _sampledProbabilityOutputFeatureName;
@"NSString" _samplingScaleInputFeatureName;
@"NSString" _samplingTruncationInputFeatureName;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLBayesianProbitRegression setFeatureName:to:descriptions:];
+[MLBayesianProbitRegression loadModelFromSpecification:configuration:error:];
+[MLBayesianProbitRegression modelWithContentsOfURL:error:];
+[MLBayesianProbitRegression validateModelDescription:];
```

## Instance methods

```
-[MLBayesianProbitRegression model];
-[MLBayesianProbitRegression regress:options:error:];
-[MLBayesianProbitRegression reset];
-[MLBayesianProbitRegression isEqual:];
-[MLBayesianProbitRegression FeatureCount];
-[MLBayesianProbitRegression convertOutputFeatureToPredictionValues:event:importance:error:];
-[MLBayesianProbitRegression createCheckpoint];
-[MLBayesianProbitRegression createRegressorResult:];
-[MLBayesianProbitRegression getArrayFeatureValue:];
-[MLBayesianProbitRegression getFeatureValue:forName:withType:];
-[MLBayesianProbitRegression getOneHotFeatureValues:error:];
-[MLBayesianProbitRegression getOptimism:];
-[MLBayesianProbitRegression getSamplingScale:];
-[MLBayesianProbitRegression getSamplingTruncation:];
-[MLBayesianProbitRegression initWithDescription:numberOfFeatures:priorMean:];
-[MLBayesianProbitRegression initWithDescription:numberOfFeatures:priorMean:regressionInputName:optimismInputName:samplingScaleInputName:samplingTruncationInputName:meanOutputName:varianceOutputName:pessimisticProbabilityOutputName:sampledProbabilityOutputName:];
-[MLBayesianProbitRegression initWithSpecification:configuration:error:];
-[MLBayesianProbitRegression isEqualToBopr:];
-[MLBayesianProbitRegression resetToLastCheckpointBeforeDate:];
-[MLBayesianProbitRegression saveModelToSpecification:];
-[MLBayesianProbitRegression setFeatureCount:];
-[MLBayesianProbitRegression setInputFeatureName:to:];
-[MLBayesianProbitRegression setOutputFeatureName:to:];
-[MLBayesianProbitRegression updateModelFromFeatures:toTarget:error:];
-[MLBayesianProbitRegression updateModelFromFeatures:toTarget:options:error:];
```
