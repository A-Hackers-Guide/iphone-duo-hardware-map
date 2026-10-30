# `QSSGraphemeToPhonemeRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{GraphemeToPhonemeRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) orthography;
@property (T@"QSSContextWithPronHints",R,N) context_with_pron_hints;
```

## Instance methods

```
-[QSSGraphemeToPhonemeRequest language];
-[QSSGraphemeToPhonemeRequest copyWithZone:];
-[QSSGraphemeToPhonemeRequest orthography];
-[QSSGraphemeToPhonemeRequest addObjectToBuffer:];
-[QSSGraphemeToPhonemeRequest flatbuffData];
-[QSSGraphemeToPhonemeRequest initAndVerifyWithFlatbuffData:];
-[QSSGraphemeToPhonemeRequest initWithFlatbuffData:];
-[QSSGraphemeToPhonemeRequest initWithFlatbuffData:root:];
-[QSSGraphemeToPhonemeRequest initWithFlatbuffData:root:verify:];
-[QSSGraphemeToPhonemeRequest session_id];
-[QSSGraphemeToPhonemeRequest context_with_pron_hints];
```
