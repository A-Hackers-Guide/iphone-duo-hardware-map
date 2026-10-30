# `QSSKeywordFinderRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{KeywordFinderRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSArray",R,N) keywords;
@property (T@"QSSRecognitionResult",R,N) recognition_result;
@property (TB,R,N) enable_sanitization;
```

## Instance methods

```
-[QSSKeywordFinderRequest language];
-[QSSKeywordFinderRequest keywords];
-[QSSKeywordFinderRequest copyWithZone:];
-[QSSKeywordFinderRequest addObjectToBuffer:];
-[QSSKeywordFinderRequest flatbuffData];
-[QSSKeywordFinderRequest initAndVerifyWithFlatbuffData:];
-[QSSKeywordFinderRequest initWithFlatbuffData:];
-[QSSKeywordFinderRequest initWithFlatbuffData:root:];
-[QSSKeywordFinderRequest initWithFlatbuffData:root:verify:];
-[QSSKeywordFinderRequest session_id];
-[QSSKeywordFinderRequest speech_id];
-[QSSKeywordFinderRequest enable_sanitization];
-[QSSKeywordFinderRequest recognition_result];
```
