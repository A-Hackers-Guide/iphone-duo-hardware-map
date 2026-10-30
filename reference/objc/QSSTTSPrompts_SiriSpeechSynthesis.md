# `QSSTTSPrompts`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TTSPrompts=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) prompts;
@property (T@"NSData",R,N) prompts_v2;
```

## Instance methods

```
-[QSSTTSPrompts copyWithZone:];
-[QSSTTSPrompts prompts];
-[QSSTTSPrompts addObjectToBuffer:];
-[QSSTTSPrompts flatbuffData];
-[QSSTTSPrompts initAndVerifyWithFlatbuffData:];
-[QSSTTSPrompts initWithFlatbuffData:];
-[QSSTTSPrompts initWithFlatbuffData:root:];
-[QSSTTSPrompts initWithFlatbuffData:root:verify:];
-[QSSTTSPrompts prompts_v2];
-[QSSTTSPrompts prompts_v2:];
```
