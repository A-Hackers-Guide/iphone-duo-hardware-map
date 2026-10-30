# `QSSShortcutFuzzyMatchRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ShortcutFuzzyMatchRequest=[1C]} _root;
```

## Properties

```
@property (T@"QSSShortcutFuzzyMatchRequest_StringTokenPair",R,N) utterance;
@property (T@"NSArray",R,N) shortcuts;
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) interaction_id;
@property (T@"NSString",R,N) locale;
@property (T@"NSString",R,N) device_type;
@property (T@"NSString",R,N) context;
```

## Instance methods

```
-[QSSShortcutFuzzyMatchRequest device_type];
-[QSSShortcutFuzzyMatchRequest locale];
-[QSSShortcutFuzzyMatchRequest copyWithZone:];
-[QSSShortcutFuzzyMatchRequest context];
-[QSSShortcutFuzzyMatchRequest utterance];
-[QSSShortcutFuzzyMatchRequest shortcuts];
-[QSSShortcutFuzzyMatchRequest addObjectToBuffer:];
-[QSSShortcutFuzzyMatchRequest flatbuffData];
-[QSSShortcutFuzzyMatchRequest initAndVerifyWithFlatbuffData:];
-[QSSShortcutFuzzyMatchRequest initWithFlatbuffData:];
-[QSSShortcutFuzzyMatchRequest initWithFlatbuffData:root:];
-[QSSShortcutFuzzyMatchRequest initWithFlatbuffData:root:verify:];
-[QSSShortcutFuzzyMatchRequest session_id];
-[QSSShortcutFuzzyMatchRequest interaction_id];
-[QSSShortcutFuzzyMatchRequest request_id];
```
