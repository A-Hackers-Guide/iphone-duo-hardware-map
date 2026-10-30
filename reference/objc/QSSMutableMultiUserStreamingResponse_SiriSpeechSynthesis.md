# `QSSMutableMultiUserStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSMultiUserStreamingResponse`
- 0 instance variables, 10 properties, 22 instance methods, 0 class methods

## Properties

```
@property (Tq,N) content_type;
@property (T@"QSSFinalSpeechRecognitionResponse",C,N) contentAsQSSFinalSpeechRecognitionResponse;
@property (T@"QSSPartialSpeechRecognitionResponse",C,N) contentAsQSSPartialSpeechRecognitionResponse;
@property (T@"QSSRecognitionProgress",C,N) contentAsQSSRecognitionProgress;
@property (T@"QSSRecognitionCandidate",C,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",C,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSServerEndpointFeatures",C,N) contentAsQSSServerEndpointFeatures;
@property (T@"QSSClientSetupInfo",C,N) contentAsQSSClientSetupInfo;
@property (T@"QSSAudioLimitExceeded",C,N) contentAsQSSAudioLimitExceeded;
@property (T@"QSSFinalBlazarResponse",C,N) contentAsQSSFinalBlazarResponse;
```

## Instance methods

```
-[QSSMutableMultiUserStreamingResponse init];
-[QSSMutableMultiUserStreamingResponse copyWithZone:];
-[QSSMutableMultiUserStreamingResponse content_type];
-[QSSMutableMultiUserStreamingResponse setContent_type:];
-[QSSMutableMultiUserStreamingResponse contentAsQSSRecognitionProgress];
-[QSSMutableMultiUserStreamingResponse contentAsQSSFinalBlazarResponse];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSClientSetupInfo:];
-[QSSMutableMultiUserStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSMutableMultiUserStreamingResponse contentAsQSSClientSetupInfo];
-[QSSMutableMultiUserStreamingResponse contentAsQSSFinalSpeechRecognitionResponse];
-[QSSMutableMultiUserStreamingResponse contentAsQSSPartialSpeechRecognitionResponse];
-[QSSMutableMultiUserStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSMutableMultiUserStreamingResponse contentAsQSSRequestStatsResponse];
-[QSSMutableMultiUserStreamingResponse contentAsQSSServerEndpointFeatures];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSAudioLimitExceeded:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSFinalBlazarResponse:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSFinalSpeechRecognitionResponse:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSPartialSpeechRecognitionResponse:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSRecognitionCandidate:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSRecognitionProgress:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSRequestStatsResponse:];
-[QSSMutableMultiUserStreamingResponse setContentAsQSSServerEndpointFeatures:];
```
