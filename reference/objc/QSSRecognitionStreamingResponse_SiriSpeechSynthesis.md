# `QSSRecognitionStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 13 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSFinalSpeechRecognitionResponse",R,N) contentAsQSSFinalSpeechRecognitionResponse;
@property (T@"QSSPartialSpeechRecognitionResponse",R,N) contentAsQSSPartialSpeechRecognitionResponse;
@property (T@"QSSUpdatedAcousticProfile",R,N) contentAsQSSUpdatedAcousticProfile;
@property (T@"QSSEndPointLikelihood",R,N) contentAsQSSEndPointLikelihood;
@property (T@"QSSEndPointCandidate",R,N) contentAsQSSEndPointCandidate;
@property (T@"QSSRecognitionProgress",R,N) contentAsQSSRecognitionProgress;
@property (T@"QSSCheckForSpeechResponse",R,N) contentAsQSSCheckForSpeechResponse;
@property (T@"QSSRecognitionCandidate",R,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",R,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSServerEndpointFeatures",R,N) contentAsQSSServerEndpointFeatures;
@property (T@"QSSClientSetupInfo",R,N) contentAsQSSClientSetupInfo;
@property (T@"QSSAudioLimitExceeded",R,N) contentAsQSSAudioLimitExceeded;
```

## Instance methods

```
-[QSSRecognitionStreamingResponse copyWithZone:];
-[QSSRecognitionStreamingResponse addObjectToBuffer:];
-[QSSRecognitionStreamingResponse content_type];
-[QSSRecognitionStreamingResponse flatbuffData];
-[QSSRecognitionStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSRecognitionStreamingResponse initWithFlatbuffData:];
-[QSSRecognitionStreamingResponse initWithFlatbuffData:root:];
-[QSSRecognitionStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSRecognitionStreamingResponse contentAsQSSRecognitionProgress];
-[QSSRecognitionStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSRecognitionStreamingResponse contentAsQSSCheckForSpeechResponse];
-[QSSRecognitionStreamingResponse contentAsQSSClientSetupInfo];
-[QSSRecognitionStreamingResponse contentAsQSSEndPointCandidate];
-[QSSRecognitionStreamingResponse contentAsQSSEndPointLikelihood];
-[QSSRecognitionStreamingResponse contentAsQSSFinalSpeechRecognitionResponse];
-[QSSRecognitionStreamingResponse contentAsQSSPartialSpeechRecognitionResponse];
-[QSSRecognitionStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSRecognitionStreamingResponse contentAsQSSRequestStatsResponse];
-[QSSRecognitionStreamingResponse contentAsQSSServerEndpointFeatures];
-[QSSRecognitionStreamingResponse contentAsQSSUpdatedAcousticProfile];
```
