# `QSSSetSpeechContext`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SetSpeechContext=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) contextual_text;
@property (T@"NSString",R,N) left_context;
@property (T@"NSString",R,N) right_context;
@property (T@"NSArray",R,N) context_with_pron_hints;
```

## Instance methods

```
-[QSSSetSpeechContext copyWithZone:];
-[QSSSetSpeechContext addObjectToBuffer:];
-[QSSSetSpeechContext flatbuffData];
-[QSSSetSpeechContext initAndVerifyWithFlatbuffData:];
-[QSSSetSpeechContext initWithFlatbuffData:];
-[QSSSetSpeechContext initWithFlatbuffData:root:];
-[QSSSetSpeechContext initWithFlatbuffData:root:verify:];
-[QSSSetSpeechContext contextual_text];
-[QSSSetSpeechContext context_with_pron_hints];
-[QSSSetSpeechContext left_context];
-[QSSSetSpeechContext right_context];
```
