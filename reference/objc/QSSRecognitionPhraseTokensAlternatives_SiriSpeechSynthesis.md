# `QSSRecognitionPhraseTokensAlternatives`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionPhraseTokensAlternatives=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) tok_phrases;
@property (TB,R,N) has_unsuggested_alternatives;
```

## Instance methods

```
-[QSSRecognitionPhraseTokensAlternatives copyWithZone:];
-[QSSRecognitionPhraseTokensAlternatives addObjectToBuffer:];
-[QSSRecognitionPhraseTokensAlternatives flatbuffData];
-[QSSRecognitionPhraseTokensAlternatives initAndVerifyWithFlatbuffData:];
-[QSSRecognitionPhraseTokensAlternatives initWithFlatbuffData:];
-[QSSRecognitionPhraseTokensAlternatives initWithFlatbuffData:root:];
-[QSSRecognitionPhraseTokensAlternatives initWithFlatbuffData:root:verify:];
-[QSSRecognitionPhraseTokensAlternatives has_unsuggested_alternatives];
-[QSSRecognitionPhraseTokensAlternatives tok_phrases];
```
