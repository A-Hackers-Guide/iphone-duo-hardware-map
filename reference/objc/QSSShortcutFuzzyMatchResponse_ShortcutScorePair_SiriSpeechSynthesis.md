# `QSSShortcutFuzzyMatchResponse_ShortcutScorePair`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ShortcutScorePair=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) shortcut;
@property (Td,R,N) similarity_score;
```

## Instance methods

```
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair shortcut];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair copyWithZone:];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair addObjectToBuffer:];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair flatbuffData];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair initAndVerifyWithFlatbuffData:];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair initWithFlatbuffData:];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair initWithFlatbuffData:root:];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair initWithFlatbuffData:root:verify:];
-[QSSShortcutFuzzyMatchResponse_ShortcutScorePair similarity_score];
```
