# `QSSStartPronGuessRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartPronGuessRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) orthography;
@property (T@"NSString",R,N) language;
@property (Tq,R,N) codec;
```

## Instance methods

```
-[QSSStartPronGuessRequest language];
-[QSSStartPronGuessRequest codec];
-[QSSStartPronGuessRequest copyWithZone:];
-[QSSStartPronGuessRequest orthography];
-[QSSStartPronGuessRequest addObjectToBuffer:];
-[QSSStartPronGuessRequest flatbuffData];
-[QSSStartPronGuessRequest initAndVerifyWithFlatbuffData:];
-[QSSStartPronGuessRequest initWithFlatbuffData:];
-[QSSStartPronGuessRequest initWithFlatbuffData:root:];
-[QSSStartPronGuessRequest initWithFlatbuffData:root:verify:];
-[QSSStartPronGuessRequest session_id];
-[QSSStartPronGuessRequest speech_id];
```
