# `QSSPostItnHammerRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PostItnHammerRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) post_itn_string;
@property (T@"NSArray",R,N) tokens;
```

## Instance methods

```
-[QSSPostItnHammerRequest language];
-[QSSPostItnHammerRequest tokens];
-[QSSPostItnHammerRequest copyWithZone:];
-[QSSPostItnHammerRequest addObjectToBuffer:];
-[QSSPostItnHammerRequest flatbuffData];
-[QSSPostItnHammerRequest initAndVerifyWithFlatbuffData:];
-[QSSPostItnHammerRequest initWithFlatbuffData:];
-[QSSPostItnHammerRequest initWithFlatbuffData:root:];
-[QSSPostItnHammerRequest initWithFlatbuffData:root:verify:];
-[QSSPostItnHammerRequest session_id];
-[QSSPostItnHammerRequest speech_id];
-[QSSPostItnHammerRequest post_itn_string];
```
