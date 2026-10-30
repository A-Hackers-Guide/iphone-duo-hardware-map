# `QSSPronunciation`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{Pronunciation=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) phonemes;
```

## Instance methods

```
-[QSSPronunciation copyWithZone:];
-[QSSPronunciation phonemes];
-[QSSPronunciation addObjectToBuffer:];
-[QSSPronunciation flatbuffData];
-[QSSPronunciation initAndVerifyWithFlatbuffData:];
-[QSSPronunciation initWithFlatbuffData:];
-[QSSPronunciation initWithFlatbuffData:root:];
-[QSSPronunciation initWithFlatbuffData:root:verify:];
```
