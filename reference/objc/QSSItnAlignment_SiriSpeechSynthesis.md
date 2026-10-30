# `QSSItnAlignment`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ItnAlignment=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) first_pre_itn_token_index;
@property (Ti,R,N) last_pre_itn_token_index;
@property (Ti,R,N) first_post_itn_char_pos;
@property (Ti,R,N) last_post_itn_char_pos;
```

## Instance methods

```
-[QSSItnAlignment copyWithZone:];
-[QSSItnAlignment addObjectToBuffer:];
-[QSSItnAlignment flatbuffData];
-[QSSItnAlignment initAndVerifyWithFlatbuffData:];
-[QSSItnAlignment initWithFlatbuffData:];
-[QSSItnAlignment initWithFlatbuffData:root:];
-[QSSItnAlignment initWithFlatbuffData:root:verify:];
-[QSSItnAlignment first_post_itn_char_pos];
-[QSSItnAlignment first_pre_itn_token_index];
-[QSSItnAlignment last_post_itn_char_pos];
-[QSSItnAlignment last_pre_itn_token_index];
```
