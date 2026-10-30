# `QSSMutableMultilingualStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSMultilingualStreamingResponse`
- 0 instance variables, 7 properties, 16 instance methods, 0 class methods

## Properties

```
@property (Tq,N) content_type;
@property (T@"QSSFinalSpeechRecognitionResponse",C,N) contentAsQSSFinalSpeechRecognitionResponse;
@property (T@"QSSPartialSpeechRecognitionResponse",C,N) contentAsQSSPartialSpeechRecognitionResponse;
@property (T@"QSSRecognitionCandidate",C,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",C,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSAudioLimitExceeded",C,N) contentAsQSSAudioLimitExceeded;
@property (T@"QSSFinalBlazarResponse",C,N) contentAsQSSFinalBlazarResponse;
```

## Instance methods

```
-[QSSMutableMultilingualStreamingResponse init];
-[QSSMutableMultilingualStreamingResponse copyWithZone:];
-[QSSMutableMultilingualStreamingResponse content_type];
-[QSSMutableMultilingualStreamingResponse setContent_type:];
-[QSSMutableMultilingualStreamingResponse contentAsQSSFinalBlazarResponse];
-[QSSMutableMultilingualStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSMutableMultilingualStreamingResponse contentAsQSSFinalSpeechRecognitionResponse];
-[QSSMutableMultilingualStreamingResponse contentAsQSSPartialSpeechRecognitionResponse];
-[QSSMutableMultilingualStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSMutableMultilingualStreamingResponse contentAsQSSRequestStatsResponse];
-[QSSMutableMultilingualStreamingResponse setContentAsQSSAudioLimitExceeded:];
-[QSSMutableMultilingualStreamingResponse setContentAsQSSFinalBlazarResponse:];
-[QSSMutableMultilingualStreamingResponse setContentAsQSSFinalSpeechRecognitionResponse:];
-[QSSMutableMultilingualStreamingResponse setContentAsQSSPartialSpeechRecognitionResponse:];
-[QSSMutableMultilingualStreamingResponse setContentAsQSSRecognitionCandidate:];
-[QSSMutableMultilingualStreamingResponse setContentAsQSSRequestStatsResponse:];
```
