# `MLProgramTrainer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
d _learningRate;
@"<MLProgramInternal>" _program;
@"MLProgramContext" _context;
@"MLProgramEvaluator" _evaluator;
@"<MLFeatureProvider>" _currentUpdatedWeights;
```

## Properties

```
@property (T@"<MLProgramInternal>",&,N,V_program) program;
@property (T@"MLProgramContext",&,N,V_context) context;
@property (T@"MLProgramEvaluator",&,N,V_evaluator) evaluator;
@property (T@"<MLFeatureProvider>",&,N,V_currentUpdatedWeights) currentUpdatedWeights;
@property (Td,N,V_learningRate) learningRate;
@property (T@"<MLModeling>",R,C) inferenceModel;
```

## Instance methods

```
-[MLProgramTrainer setContext:];
-[MLProgramTrainer program];
-[MLProgramTrainer context];
-[MLProgramTrainer setProgram:];
-[MLProgramTrainer evaluator];
-[MLProgramTrainer setEvaluator:];
-[MLProgramTrainer inferenceModel];
-[MLProgramTrainer setLearningRate:];
-[MLProgramTrainer attachLearningRateToFeatures:];
-[MLProgramTrainer copyCurrentTrainingDelta];
-[MLProgramTrainer currentUpdatedWeights];
-[MLProgramTrainer evaluateUsingTestData:error:];
-[MLProgramTrainer evaluateUsingTestData:evaluationMetricNames:error:];
-[MLProgramTrainer evaluateUsingTestData:evaluationMetricNames:evaluateOnTrainFunction:error:];
-[MLProgramTrainer flattenFeatures:orderedFeatures:];
-[MLProgramTrainer initWithProgram:learningRate:error:];
-[MLProgramTrainer learningRate];
-[MLProgramTrainer orderedTrainableWeightsNames];
-[MLProgramTrainer setCurrentUpdatedWeights:];
-[MLProgramTrainer trainUsingTrainingData:error:];
-[MLProgramTrainer trainUsingTrainingData:evaluationMetricNames:error:];
```
