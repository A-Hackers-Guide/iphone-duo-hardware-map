# `QSSMutableRecognitionStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSRecognitionStreamingResponse`
- 0 instance variables, 13 properties, 28 instance methods, 0 class methods

## Properties

```
@property (Tq,N) content_type;
@property (T@"QSSFinalSpeechRecognitionResponse",C,N) contentAsQSSFinalSpeechRecognitionResponse;
@property (T@"QSSPartialSpeechRecognitionResponse",C,N) contentAsQSSPartialSpeechRecognitionResponse;
@property (T@"QSSUpdatedAcousticProfile",C,N) contentAsQSSUpdatedAcousticProfile;
@property (T@"QSSEndPointLikelihood",C,N) contentAsQSSEndPointLikelihood;
@property (T@"QSSEndPointCandidate",C,N) contentAsQSSEndPointCandidate;
@property (T@"QSSRecognitionProgress",C,N) contentAsQSSRecognitionProgress;
@property (T@"QSSCheckForSpeechResponse",C,N) contentAsQSSCheckForSpeechResponse;
@property (T@"QSSRecognitionCandidate",C,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",C,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSServerEndpointFeatures",C,N) contentAsQSSServerEndpointFeatures;
@property (T@"QSSClientSetupInfo",C,N) contentAsQSSClientSetupInfo;
@property (T@"QSSAudioLimitExceeded",C,N) contentAsQSSAudioLimitExceeded;
```

## Instance methods

```
-[QSSMutableRecognitionStreamingResponse init];
-[QSSMutableRecognitionStreamingResponse copyWithZone:];
-[QSSMutableRecognitionStreamingResponse content_type];
-[QSSMutableRecognitionStreamingResponse setContent_type:];
-[QSSMutableRecognitionStreamingResponse contentAsQSSRecognitionProgress];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSClientSetupInfo:];
-[QSSMutableRecognitionStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSMutableRecognitionStreamingResponse contentAsQSSCheckForSpeechResponse];
-[QSSMutableRecognitionStreamingResponse contentAsQSSClientSetupInfo];
-[QSSMutableRecognitionStreamingResponse contentAsQSSEndPointCandidate];
-[QSSMutableRecognitionStreamingResponse contentAsQSSEndPointLikelihood];
-[QSSMutableRecognitionStreamingResponse contentAsQSSFinalSpeechRecognitionResponse];
-[QSSMutableRecognitionStreamingResponse contentAsQSSPartialSpeechRecognitionResponse];
-[QSSMutableRecognitionStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSMutableRecognitionStreamingResponse contentAsQSSRequestStatsResponse];
-[QSSMutableRecognitionStreamingResponse contentAsQSSServerEndpointFeatures];
-[QSSMutableRecognitionStreamingResponse contentAsQSSUpdatedAcousticProfile];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSAudioLimitExceeded:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSCheckForSpeechResponse:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSEndPointCandidate:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSEndPointLikelihood:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSFinalSpeechRecognitionResponse:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSPartialSpeechRecognitionResponse:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSRecognitionCandidate:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSRecognitionProgress:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSRequestStatsResponse:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSServerEndpointFeatures:];
-[QSSMutableRecognitionStreamingResponse setContentAsQSSUpdatedAcousticProfile:];
```
