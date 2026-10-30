# `TCSummarizationModel`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NLTagger" _tagger;
^v _embeddingModel;
^{MontrealNeuralNetwork=} _decoderModel;
Q _sequenceLength;
Q _maxDecoderSteps;
```

## Instance methods

```
-[TCSummarizationModel dealloc];
-[TCSummarizationModel _decoderPredictions:];
-[TCSummarizationModel _tokensForString:];
-[TCSummarizationModel initWithModelPath:options:];
-[TCSummarizationModel summarizationForString:];
-[TCSummarizationModel useANEWithOptions:];
```
