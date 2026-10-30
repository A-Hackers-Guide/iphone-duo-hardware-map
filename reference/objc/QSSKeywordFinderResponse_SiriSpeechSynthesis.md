# `QSSKeywordFinderResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{KeywordFinderResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"QSSRecognitionSausage",R,N) corrected_sausage;
@property (T@"NSArray",R,N) n_best_list;
```

## Instance methods

```
-[QSSKeywordFinderResponse language];
-[QSSKeywordFinderResponse copyWithZone:];
-[QSSKeywordFinderResponse addObjectToBuffer:];
-[QSSKeywordFinderResponse flatbuffData];
-[QSSKeywordFinderResponse initAndVerifyWithFlatbuffData:];
-[QSSKeywordFinderResponse initWithFlatbuffData:];
-[QSSKeywordFinderResponse initWithFlatbuffData:root:];
-[QSSKeywordFinderResponse initWithFlatbuffData:root:verify:];
-[QSSKeywordFinderResponse session_id];
-[QSSKeywordFinderResponse speech_id];
-[QSSKeywordFinderResponse corrected_sausage];
-[QSSKeywordFinderResponse n_best_list];
-[QSSKeywordFinderResponse return_code];
-[QSSKeywordFinderResponse return_str];
```
