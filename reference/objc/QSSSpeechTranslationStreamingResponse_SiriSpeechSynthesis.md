# `QSSSpeechTranslationStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 13 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSSpeechTranslationPartialRecognitionResponse",R,N) contentAsQSSSpeechTranslationPartialRecognitionResponse;
@property (T@"QSSSpeechTranslationFinalRecognitionResponse",R,N) contentAsQSSSpeechTranslationFinalRecognitionResponse;
@property (T@"QSSAudioLimitExceeded",R,N) contentAsQSSAudioLimitExceeded;
@property (T@"QSSSpeechTranslationMtResponse",R,N) contentAsQSSSpeechTranslationMtResponse;
@property (T@"QSSSpeechTranslationTextToSpeechResponse",R,N) contentAsQSSSpeechTranslationTextToSpeechResponse;
@property (T@"QSSFinalBlazarResponse",R,N) contentAsQSSFinalBlazarResponse;
@property (T@"QSSRecognitionProgress",R,N) contentAsQSSRecognitionProgress;
@property (T@"QSSRecognitionCandidate",R,N) contentAsQSSRecognitionCandidate;
@property (T@"QSSRequestStatsResponse",R,N) contentAsQSSRequestStatsResponse;
@property (T@"QSSServerEndpointFeatures",R,N) contentAsQSSServerEndpointFeatures;
@property (T@"QSSClientSetupInfo",R,N) contentAsQSSClientSetupInfo;
@property (T@"QSSSpeechTranslationServerEndpointFeatures",R,N) contentAsQSSSpeechTranslationServerEndpointFeatures;
```

## Instance methods

```
-[QSSSpeechTranslationStreamingResponse copyWithZone:];
-[QSSSpeechTranslationStreamingResponse addObjectToBuffer:];
-[QSSSpeechTranslationStreamingResponse content_type];
-[QSSSpeechTranslationStreamingResponse flatbuffData];
-[QSSSpeechTranslationStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationStreamingResponse initWithFlatbuffData:];
-[QSSSpeechTranslationStreamingResponse initWithFlatbuffData:root:];
-[QSSSpeechTranslationStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationStreamingResponse contentAsQSSRecognitionProgress];
-[QSSSpeechTranslationStreamingResponse contentAsQSSFinalBlazarResponse];
-[QSSSpeechTranslationStreamingResponse contentAsQSSAudioLimitExceeded];
-[QSSSpeechTranslationStreamingResponse contentAsQSSClientSetupInfo];
-[QSSSpeechTranslationStreamingResponse contentAsQSSRecognitionCandidate];
-[QSSSpeechTranslationStreamingResponse contentAsQSSRequestStatsResponse];
-[QSSSpeechTranslationStreamingResponse contentAsQSSServerEndpointFeatures];
-[QSSSpeechTranslationStreamingResponse contentAsQSSSpeechTranslationFinalRecognitionResponse];
-[QSSSpeechTranslationStreamingResponse contentAsQSSSpeechTranslationMtResponse];
-[QSSSpeechTranslationStreamingResponse contentAsQSSSpeechTranslationPartialRecognitionResponse];
-[QSSSpeechTranslationStreamingResponse contentAsQSSSpeechTranslationServerEndpointFeatures];
-[QSSSpeechTranslationStreamingResponse contentAsQSSSpeechTranslationTextToSpeechResponse];
```
