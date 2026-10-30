# `QSSMultiUserStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{MultiUserStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSFinalSpeechRecognitionResponse",R,N) contentAsQSSFinalSpeechRecognitionResponse;
@property (T@"QSSPartialSpeechRecognitionResponse",R,N) contentAsQSSPartialSpeechRecognitionResponse;
@property (T@"QSSRecognitionProgress",R,N) contentAsQSSRecognitionProgress;
@property (T@"QSSRecognitionCandidate",R,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",R,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSServerEndpointFeatures",R,N) contentAsQSSServerEndpointFeatures;
@property (T@"QSSClientSetupInfo",R,N) contentAsQSSClientSetupInfo;
@property (T@"QSSAudioLimitExceeded",R,N) contentAsQSSAudioLimitExceeded;
@property (T@"QSSFinalBlazarResponse",R,N) contentAsQSSFinalBlazarResponse;
```

## Instance methods

```
-[QSSMultiUserStreamingResponse copyWithZone:];
-[QSSMultiUserStreamingResponse addObjectToBuffer:];
-[QSSMultiUserStreamingResponse content_type];
-[QSSMultiUserStreamingResponse flatbuffData];
-[QSSMultiUserStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSMultiUserStreamingResponse initWithFlatbuffData:];
-[QSSMultiUserStreamingResponse initWithFlatbuffData:root:];
-[QSSMultiUserStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSMultiUserStreamingResponse contentAsQSSRecognitionProgress];
-[QSSMultiUserStreamingResponse contentAsQSSFinalBlazarResponse];
-[QSSMultiUserStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSMultiUserStreamingResponse contentAsQSSClientSetupInfo];
-[QSSMultiUserStreamingResponse contentAsQSSFinalSpeechRecognitionResponse];
-[QSSMultiUserStreamingResponse contentAsQSSPartialSpeechRecognitionResponse];
-[QSSMultiUserStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSMultiUserStreamingResponse contentAsQSSRequestStatsResponse];
-[QSSMultiUserStreamingResponse contentAsQSSServerEndpointFeatures];
```
