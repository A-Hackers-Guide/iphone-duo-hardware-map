# `TCGECDecoderModel`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCGECModel`
- 6 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^v _embeddings;
^{MontrealNeuralNetwork=} _spanDetector;
^{MontrealNeuralNetwork=} _gecDecoder;
Q _kNumFragments;
Q _embeddingDimension;
Q _spanCategories;
```

## Instance methods

```
-[TCGECDecoderModel dealloc];
-[TCGECDecoderModel embeddingsForTokenizedSentence:];
-[TCGECDecoderModel classifierPredictions:tokenCount:];
-[TCGECDecoderModel decoderPredictions:fragmentCount:];
-[TCGECDecoderModel enumerateIssuesForSentence:checkTermination:withBlock:];
-[TCGECDecoderModel initWithModelPath:OTABundlePath:options:];
-[TCGECDecoderModel useANEWithOptions:];
```
