# `QSSRequestStatsResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RequestStatsResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) bool_stats;
@property (T@"NSArray",R,N) int32_stats;
@property (T@"NSArray",R,N) double_stats;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) request_locale;
```

## Instance methods

```
-[QSSRequestStatsResponse language];
-[QSSRequestStatsResponse copyWithZone:];
-[QSSRequestStatsResponse addObjectToBuffer:];
-[QSSRequestStatsResponse flatbuffData];
-[QSSRequestStatsResponse initAndVerifyWithFlatbuffData:];
-[QSSRequestStatsResponse initWithFlatbuffData:];
-[QSSRequestStatsResponse initWithFlatbuffData:root:];
-[QSSRequestStatsResponse initWithFlatbuffData:root:verify:];
-[QSSRequestStatsResponse speech_id];
-[QSSRequestStatsResponse bool_stats];
-[QSSRequestStatsResponse double_stats];
-[QSSRequestStatsResponse int32_stats];
-[QSSRequestStatsResponse request_locale];
```
