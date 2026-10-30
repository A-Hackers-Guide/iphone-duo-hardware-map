# `QSSTTSPhonemeSequence`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TTSPhonemeSequence=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) word_phonemes;
```

## Instance methods

```
-[QSSTTSPhonemeSequence copyWithZone:];
-[QSSTTSPhonemeSequence addObjectToBuffer:];
-[QSSTTSPhonemeSequence flatbuffData];
-[QSSTTSPhonemeSequence initAndVerifyWithFlatbuffData:];
-[QSSTTSPhonemeSequence initWithFlatbuffData:];
-[QSSTTSPhonemeSequence initWithFlatbuffData:root:];
-[QSSTTSPhonemeSequence initWithFlatbuffData:root:verify:];
-[QSSTTSPhonemeSequence word_phonemes];
```
