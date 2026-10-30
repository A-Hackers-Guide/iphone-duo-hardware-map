# `QSSShortcutFuzzyMatchResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ShortcutFuzzyMatchResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) utterance;
@property (T@"NSArray",R,N) shortcut_score_pairs;
@property (Ti,R,N) return_code;
```

## Instance methods

```
-[QSSShortcutFuzzyMatchResponse copyWithZone:];
-[QSSShortcutFuzzyMatchResponse utterance];
-[QSSShortcutFuzzyMatchResponse addObjectToBuffer:];
-[QSSShortcutFuzzyMatchResponse flatbuffData];
-[QSSShortcutFuzzyMatchResponse initAndVerifyWithFlatbuffData:];
-[QSSShortcutFuzzyMatchResponse initWithFlatbuffData:];
-[QSSShortcutFuzzyMatchResponse initWithFlatbuffData:root:];
-[QSSShortcutFuzzyMatchResponse initWithFlatbuffData:root:verify:];
-[QSSShortcutFuzzyMatchResponse return_code];
-[QSSShortcutFuzzyMatchResponse shortcut_score_pairs];
```
