# `QSSTextToSpeechFeature`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechFeature=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) normalized_text;
@property (T@"NSArray",R,N) phoneme_sequence;
@property (T@"NSArray",R,N) prompts;
@property (T@"NSArray",R,N) replacement;
@property (T@"NSArray",R,N) neural_phoneme_sequence;
```

## Instance methods

```
-[QSSTextToSpeechFeature copyWithZone:];
-[QSSTextToSpeechFeature replacement];
-[QSSTextToSpeechFeature prompts];
-[QSSTextToSpeechFeature normalized_text];
-[QSSTextToSpeechFeature addObjectToBuffer:];
-[QSSTextToSpeechFeature flatbuffData];
-[QSSTextToSpeechFeature initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechFeature initWithFlatbuffData:];
-[QSSTextToSpeechFeature initWithFlatbuffData:root:];
-[QSSTextToSpeechFeature initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechFeature neural_phoneme_sequence];
-[QSSTextToSpeechFeature phoneme_sequence];
```
