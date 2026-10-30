# `QSSRecognitionPhraseTokens`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionPhraseTokens=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) tokens;
```

## Instance methods

```
-[QSSRecognitionPhraseTokens tokens];
-[QSSRecognitionPhraseTokens copyWithZone:];
-[QSSRecognitionPhraseTokens addObjectToBuffer:];
-[QSSRecognitionPhraseTokens flatbuffData];
-[QSSRecognitionPhraseTokens initAndVerifyWithFlatbuffData:];
-[QSSRecognitionPhraseTokens initWithFlatbuffData:];
-[QSSRecognitionPhraseTokens initWithFlatbuffData:root:];
-[QSSRecognitionPhraseTokens initWithFlatbuffData:root:verify:];
```
