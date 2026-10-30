# `QSSMultilingualStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{MultilingualStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSFinalSpeechRecognitionResponse",R,N) contentAsQSSFinalSpeechRecognitionResponse;
@property (T@"QSSPartialSpeechRecognitionResponse",R,N) contentAsQSSPartialSpeechRecognitionResponse;
@property (T@"QSSRecognitionCandidate",R,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",R,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSAudioLimitExceeded",R,N) contentAsQSSAudioLimitExceeded;
@property (T@"QSSFinalBlazarResponse",R,N) contentAsQSSFinalBlazarResponse;
```

## Instance methods

```
-[QSSMultilingualStreamingResponse copyWithZone:];
-[QSSMultilingualStreamingResponse addObjectToBuffer:];
-[QSSMultilingualStreamingResponse content_type];
-[QSSMultilingualStreamingResponse flatbuffData];
-[QSSMultilingualStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSMultilingualStreamingResponse initWithFlatbuffData:];
-[QSSMultilingualStreamingResponse initWithFlatbuffData:root:];
-[QSSMultilingualStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSMultilingualStreamingResponse contentAsQSSFinalBlazarResponse];
-[QSSMultilingualStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSMultilingualStreamingResponse contentAsQSSFinalSpeechRecognitionResponse];
-[QSSMultilingualStreamingResponse contentAsQSSPartialSpeechRecognitionResponse];
-[QSSMultilingualStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSMultilingualStreamingResponse contentAsQSSRequestStatsResponse];
```
