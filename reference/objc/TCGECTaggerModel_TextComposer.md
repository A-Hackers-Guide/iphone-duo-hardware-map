# `TCGECTaggerModel`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCGECModel`
- 10 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _modelPath;
^v _embeddings;
^{MontrealNeuralNetwork=} _gecClassifier;
^{MontrealNeuralNetwork=} _vscClassifier;
@"NSArray" _gecClassifierLabels;
@"NSDictionary" _labelsToIssueType;
@"NSDictionary" _indicationThresholds;
@"NSDictionary" _autocorrectionThresholds;
@"NSDictionary" _detailedIssueTypes;
Q _keepLabelIndex;
```

## Properties

```
@property (TQ,R,N) numCategories;
@property (TQ,R,N) embeddingDimension;
```

## Instance methods

```
-[TCGECTaggerModel dealloc];
-[TCGECTaggerModel embeddingDimension];
-[TCGECTaggerModel embeddingsForTokenizedSentence:];
-[TCGECTaggerModel classifierPrediction:labelCount:input:tokenCount:];
-[TCGECTaggerModel classifierPredictions:tokenCount:];
-[TCGECTaggerModel correctionForPredictedClass:withProbability:];
-[TCGECTaggerModel enumerateIssuesForSentence:checkTermination:withBlock:];
-[TCGECTaggerModel initWithModelPath:OTABundlePath:options:];
-[TCGECTaggerModel isTerminatedSentence:embeddings:];
-[TCGECTaggerModel loadAutocorrectionThresholdsFromURL:];
-[TCGECTaggerModel loadDetailedIssueTypesFromURL:];
-[TCGECTaggerModel loadErrorClassesFromURL:];
-[TCGECTaggerModel loadIndicationThresholdsFromURL:];
-[TCGECTaggerModel numCategories];
-[TCGECTaggerModel useANEWithOptions:];
```
