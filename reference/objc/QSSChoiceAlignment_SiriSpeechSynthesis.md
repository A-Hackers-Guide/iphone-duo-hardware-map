# `QSSChoiceAlignment`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ChoiceAlignment=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) post_itn_choice_indices;
@property (T@"NSArray",R,N) pre_itn_token_to_post_itn_char_alignments;
```

## Instance methods

```
-[QSSChoiceAlignment copyWithZone:];
-[QSSChoiceAlignment addObjectToBuffer:];
-[QSSChoiceAlignment flatbuffData];
-[QSSChoiceAlignment initAndVerifyWithFlatbuffData:];
-[QSSChoiceAlignment initWithFlatbuffData:];
-[QSSChoiceAlignment initWithFlatbuffData:root:];
-[QSSChoiceAlignment initWithFlatbuffData:root:verify:];
-[QSSChoiceAlignment post_itn_choice_indices];
-[QSSChoiceAlignment pre_itn_token_to_post_itn_char_alignments];
```
