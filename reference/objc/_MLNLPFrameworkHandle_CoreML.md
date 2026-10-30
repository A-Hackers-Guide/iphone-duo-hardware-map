# `_MLNLPFrameworkHandle`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 21 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _valid;
^? _NLPSequenceModelCopyPredictedTokensAndLabelsForTextImpl;
^? _NLPSequenceModelCreateWithDataImpl;
^? _NLPSequenceModelGetRevisionImpl;
^? _NLPSequenceModelIsRevisionSupportedImpl;
^? _NLPSequenceModelGetCurrentRevisionImpl;
^? _NLPClassifierModelCopyPredictedLabelForTextImpl;
^? _NLPClassifierModelCreateWithDataImpl;
^? _NLPClassifierModelGetRevisionImpl;
^? _NLPClassifierModelIsRevisionSupportedImpl;
^? _NLPClassifierModelGetCurrentRevisionImpl;
^? _NLPGazetteerModelCopyLabelForStringImpl;
^? _NLPGazetteerModelCreateWithDataImpl;
^? _NLPGazetteerModelGetRevisionImpl;
^? _NLPGazetteerModelIsRevisionSupportedImpl;
^? _NLPGazetteerModelGetCurrentRevisionImpl;
^? _NLPEmbeddingModelCopyVectorForStringImpl;
^? _NLPEmbeddingModelCreateWithDataImpl;
^? _NLPEmbeddingModelGetRevisionImpl;
^? _NLPEmbeddingModelIsRevisionSupportedImpl;
^? _NLPEmbeddingModelGetCurrentRevisionImpl;
```

## Properties

```
@property (T^?,R,N,V_NLPSequenceModelCopyPredictedTokensAndLabelsForTextImpl) NLPSequenceModelCopyPredictedTokensAndLabelsForTextImpl;
@property (T^?,R,N,V_NLPSequenceModelCreateWithDataImpl) NLPSequenceModelCreateWithDataImpl;
@property (T^?,R,N,V_NLPSequenceModelGetRevisionImpl) NLPSequenceModelGetRevisionImpl;
@property (T^?,R,N,V_NLPSequenceModelIsRevisionSupportedImpl) NLPSequenceModelIsRevisionSupportedImpl;
@property (T^?,R,N,V_NLPSequenceModelGetCurrentRevisionImpl) NLPSequenceModelGetCurrentRevisionImpl;
@property (T^?,R,N,V_NLPClassifierModelCopyPredictedLabelForTextImpl) NLPClassifierModelCopyPredictedLabelForTextImpl;
@property (T^?,R,N,V_NLPClassifierModelCreateWithDataImpl) NLPClassifierModelCreateWithDataImpl;
@property (T^?,R,N,V_NLPClassifierModelGetRevisionImpl) NLPClassifierModelGetRevisionImpl;
@property (T^?,R,N,V_NLPClassifierModelIsRevisionSupportedImpl) NLPClassifierModelIsRevisionSupportedImpl;
@property (T^?,R,N,V_NLPClassifierModelGetCurrentRevisionImpl) NLPClassifierModelGetCurrentRevisionImpl;
@property (T^?,R,N,V_NLPGazetteerModelCopyLabelForStringImpl) NLPGazetteerModelCopyLabelForStringImpl;
@property (T^?,R,N,V_NLPGazetteerModelCreateWithDataImpl) NLPGazetteerModelCreateWithDataImpl;
@property (T^?,R,N,V_NLPGazetteerModelGetRevisionImpl) NLPGazetteerModelGetRevisionImpl;
@property (T^?,R,N,V_NLPGazetteerModelIsRevisionSupportedImpl) NLPGazetteerModelIsRevisionSupportedImpl;
@property (T^?,R,N,V_NLPGazetteerModelGetCurrentRevisionImpl) NLPGazetteerModelGetCurrentRevisionImpl;
@property (T^?,R,N,V_NLPEmbeddingModelCopyVectorForStringImpl) NLPEmbeddingModelCopyVectorForStringImpl;
@property (T^?,R,N,V_NLPEmbeddingModelCreateWithDataImpl) NLPEmbeddingModelCreateWithDataImpl;
@property (T^?,R,N,V_NLPEmbeddingModelGetRevisionImpl) NLPEmbeddingModelGetRevisionImpl;
@property (T^?,R,N,V_NLPEmbeddingModelIsRevisionSupportedImpl) NLPEmbeddingModelIsRevisionSupportedImpl;
@property (T^?,R,N,V_NLPEmbeddingModelGetCurrentRevisionImpl) NLPEmbeddingModelGetCurrentRevisionImpl;
@property (TB,R,N,GisValid,V_valid) valid;
```

## Class methods

```
+[_MLNLPFrameworkHandle sharedHandle];
```

## Instance methods

```
-[_MLNLPFrameworkHandle init];
-[_MLNLPFrameworkHandle isValid];
-[_MLNLPFrameworkHandle NLPSequenceModelGetRevisionImpl];
-[_MLNLPFrameworkHandle NLPClassifierModelCreateWithDataImpl];
-[_MLNLPFrameworkHandle NLPClassifierModelGetRevisionImpl];
-[_MLNLPFrameworkHandle NLPEmbeddingModelCopyVectorForStringImpl];
-[_MLNLPFrameworkHandle NLPEmbeddingModelGetCurrentRevisionImpl];
-[_MLNLPFrameworkHandle NLPEmbeddingModelIsRevisionSupportedImpl];
-[_MLNLPFrameworkHandle NLPGazetteerModelCreateWithDataImpl];
-[_MLNLPFrameworkHandle NLPGazetteerModelGetRevisionImpl];
-[_MLNLPFrameworkHandle NLPSequenceModelCopyPredictedTokensAndLabelsForTextImpl];
-[_MLNLPFrameworkHandle NLPSequenceModelGetCurrentRevisionImpl];
-[_MLNLPFrameworkHandle NLPClassifierModelCopyPredictedLabelForTextImpl];
-[_MLNLPFrameworkHandle NLPClassifierModelGetCurrentRevisionImpl];
-[_MLNLPFrameworkHandle NLPClassifierModelIsRevisionSupportedImpl];
-[_MLNLPFrameworkHandle NLPEmbeddingModelCreateWithDataImpl];
-[_MLNLPFrameworkHandle NLPEmbeddingModelGetRevisionImpl];
-[_MLNLPFrameworkHandle NLPGazetteerModelCopyLabelForStringImpl];
-[_MLNLPFrameworkHandle NLPGazetteerModelGetCurrentRevisionImpl];
-[_MLNLPFrameworkHandle NLPGazetteerModelIsRevisionSupportedImpl];
-[_MLNLPFrameworkHandle NLPSequenceModelCreateWithDataImpl];
-[_MLNLPFrameworkHandle NLPSequenceModelIsRevisionSupportedImpl];
-[_MLNLPFrameworkHandle predictTokensLabelsLocationsLengthsForString:inputString:error:];
-[_MLNLPFrameworkHandle initializeEmbeddingModelWithData:error:];
-[_MLNLPFrameworkHandle initializeGazetteerModelWithData:error:];
-[_MLNLPFrameworkHandle initializeSentenceClassifierModelWithData:error:];
-[_MLNLPFrameworkHandle initializeWordTaggingModelWithData:error:];
-[_MLNLPFrameworkHandle predictLabelForWordString:inputString:error:];
-[_MLNLPFrameworkHandle predictLabelsForSentenceString:inputString:error:];
-[_MLNLPFrameworkHandle predictVectorForString:inputString:error:];
```
