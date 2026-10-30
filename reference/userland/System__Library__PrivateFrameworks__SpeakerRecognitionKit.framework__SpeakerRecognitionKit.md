# `/System/Library/PrivateFrameworks/SpeakerRecognitionKit.framework/SpeakerRecognitionKit`

iOS 27.2 dyld shared cache image. Version `3605.32.1.0.0`. **[DSC]**

## Linked libraries (14)

- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils`
- `/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`
- `/usr/lib/swift/libswiftsimd.dylib`

## Objective-C: 10 classes, 0 protocols, 15 methods, 3 properties

### Class pages

Every class and protocol, with its methods: [`SRKSpeakerIdentityScoreCard`](../objc/SRKSpeakerIdentityScoreCard_SpeakerRecognitionKit.md), [`SRKSpeakerProfileEmbedding`](../objc/SRKSpeakerProfileEmbedding_SpeakerRecognitionKit.md), [`SRKSpeakerRecognitionController`](../objc/SRKSpeakerRecognitionController_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit15SpeakerDetector`](../objc/_TtC21SpeakerRecognitionKit15SpeakerDetector_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit18SpeakerDetectorPSR`](../objc/_TtC21SpeakerRecognitionKit18SpeakerDetectorPSR_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit18SpeakerDetectorSAT`](../objc/_TtC21SpeakerRecognitionKit18SpeakerDetectorSAT_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit21SpeakerDetectorScorer`](../objc/_TtC21SpeakerRecognitionKit21SpeakerDetectorScorer_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit25SpeakerEmbeddingExtractor`](../objc/_TtC21SpeakerRecognitionKit25SpeakerEmbeddingExtractor_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit28SpeakerRecognitionController`](../objc/_TtC21SpeakerRecognitionKit28SpeakerRecognitionController_SpeakerRecognitionKit.md), [`_TtC21SpeakerRecognitionKit34SecureSpeakerRecognitionController`](../objc/_TtC21SpeakerRecognitionKit34SecureSpeakerRecognitionController_SpeakerRecognitionKit.md)

### Classes

`SRKSpeakerIdentityScoreCard`, `SRKSpeakerProfileEmbedding`, `SRKSpeakerRecognitionController`, `_TtC21SpeakerRecognitionKit15SpeakerDetector`, `_TtC21SpeakerRecognitionKit18SpeakerDetectorPSR`, `_TtC21SpeakerRecognitionKit18SpeakerDetectorSAT`, `_TtC21SpeakerRecognitionKit21SpeakerDetectorScorer`, `_TtC21SpeakerRecognitionKit25SpeakerEmbeddingExtractor`, `_TtC21SpeakerRecognitionKit28SpeakerRecognitionController`, `_TtC21SpeakerRecognitionKit34SecureSpeakerRecognitionController`

### Properties

```
@property (T@"NSArray",N,R) knownUserScores;
@property (TI,N,R,VaudioDurationProcessedInMillis) audioDurationProcessedInMillis;
@property (Tq,N) phraseType;
```

## Swift types (23)

`SpeakerRecognitionKit.PhraseType`, `SpeakerRecognitionKit.SRKPhraseType`, `SpeakerRecognitionKit.SRKSpeakerIdentityScoreCard:`, `SpeakerRecognitionKit.SRKSpeakerProfileEmbedding:`, `SpeakerRecognitionKit.SRKSpeakerRecognitionController:`, `SpeakerRecognitionKit.ScoringThreshold`, `SpeakerRecognitionKit.SecureSpeakerRecognitionController`, `SpeakerRecognitionKit.SecureVoiceIDScoreCard`, `SpeakerRecognitionKit.SpeakerDetector`, `SpeakerRecognitionKit.SpeakerDetectorPSR`, `SpeakerRecognitionKit.SpeakerDetectorProtocol`, `SpeakerRecognitionKit.SpeakerDetectorSAT`, `SpeakerRecognitionKit.SpeakerDetectorScorer`, `SpeakerRecognitionKit.SpeakerDetectorScorer.SpeakerDetectorType`, `SpeakerRecognitionKit.SpeakerEmbeddingExtractor`, `SpeakerRecognitionKit.SpeakerIdentityScoreCard`, `SpeakerRecognitionKit.SpeakerProfileEmbedding`, `SpeakerRecognitionKit.SpeakerRecognitionController`, `SpeakerRecognitionKit.SpeakerRecognitionController.AssetParams`, `SpeakerRecognitionKit.SpeakerRecognizerType`, `SpeakerRecognitionKit.UserClassification`, `SpeakerRecognitionKit.UserIdentityClassification`, `conformance`

## Strings (94)

```
[%s] [%ld] failed to get superVector in SpeakerDetectorSAT
[%s] [%ld] Profile Embedding does not exists
[%s] [%ld] #supervector [%s] SuperVector dimension: %ld
[%s] [%ld] #asset Unable to find phrase configurations
[%s] [%ld] SAT score is nil. Aborting speaker detection
[%s] [%ld] #profile embedding count is higher than expectation
[%s] [%ld] #analyze Score card: %s
[%s] [%ld] #analyze Unable to get score at index: %ld
[%s] [%ld] Resource URL path for locale %s is nil
[%s] [%ld] #asset Unable to decode the config
[%s] [%ld] SuperVector is nil. Failing to get the SAT score.
[%s] [%ld] falied to set SpeakerProfile Embedding in speakerDetectorPSR
[%s] [%ld] #profile numEmbedding is 0
[%s] [%ld] Ignoring audio because audio duration fed: %u is greater than max allowed duration: %ld
[%s] [%ld] #asset Unable to create scorer for embedding at index: %ld
[%s] [%ld] Unable to create SpeakerDetectorSAT
[%s] [%ld] #profile numEmbedding is higher than expectation
[%s] [%ld] #asset Unable to load the secure asset
[%s] [%ld] unable to handle speaker profile type :: only SAT is supported
[%s] [%ld] PSR score is nil. Aborting speaker detection
[%s] [%ld] #profile dimension is higher than expectation
[%s] [%ld] #analyze No scores available
[%s] [%ld] Using caller-provided OTA asset version %s
[%s] [%ld] #asset Unable to find \"Siri\" phrase configurations
[%s] [%ld] invalid embeddingType
[%s] [%ld] SuperVector is nil, unable to compute
[%s] [%ld] #asset Failed to decode asset params
[%s] [%ld] No scorers defined, unable to compute
[%s] [%ld] Using preinstalled asset version %s
[%s] [%ld] No OTA asset provided, falling back to preinstalled
[%s] [%ld] [%s] RawScore =%f, AbsoluteScore = %f
[%s] [%ld] [%s]  vtScoreScale: %f, vtScoreOffset: %f, logitCeilScore: %f, logitFloorScore: %f threshold: %s
[%s] [%ld] Resource Path: `%s`
[%s] [%ld] Unable to create SpeakerEmbeddingExtractor
[%s] [%ld] SpeakerEmbeddingExtractor endAudio
[%s] [%ld] #analyze Profile embedding and supervector dimensions do not match for scorer at index: %ld expected:%u actual:%ld
[%s] [%ld] Unable to find prinstalled asset bundle
[%s] [%ld] Unable to create SpeakerDetectorPSR
[%s] [%ld] [%s] Failed to add speaker file
[%s] [%ld] [%s] Created speaker profile scorer
[%s] [%ld] Unable to create SpeakerDetector
[%s] [%ld] falied to set SpeakerProfile Embedding in speakerDetectorSAT
[%s] [%ld] #profile does not match expected type: %s != %s
[%s] [%ld] initializing speakerIdEmbeddingExtractor
[%s] [%ld] #profile Unable to handle embedding at index: %ld
[%s] [%ld] #asset Unable to decode the asset
[%s] [%ld] Resource Path:`%s`
[%s] [%ld] #profile Unable to handle speaker profile
[%s] [%ld] Fetching the preinstalled Speaker Recognition Asset
[%s] [%ld] Profile embedding dim and supervector dim does not match
[%s] [%ld] #analyze audioDurationFedInMillis: %u, audioDurationProcessedInMillis: %u
[%s] [%ld] #analyze Unable to get scores
[%s] [%ld] [%s] Failed to create scorer. Aborting!
[%s] [%ld] #profile dimension is 0
[%s] [%ld] novDetector.getBestAnalyzedResult is nil
[%s] [%ld] #analyze Creating scorers with %ld Speaker Profile embeddings
[%s] [%ld] Fetching asset for locale %s
[%s] [%ld] Using SAT and PSR
[%s] [%ld] #supervector [%s] [%ld-%ld]: [%s]
[%s] [%ld] Using PSR only
[%s] [%ld] #asset Unable to create SpeakerEmbeddingExtractor
[%s] [%ld] #analyze endaudio() called
[%s] [%ld] #asset Unable to find \"Hey Siri\" phrase configurations
[%s] [%ld] [%s] Incorrect logitCeil %f and logitFloor %f - defaulting them to %f and %f
[%s] [%ld] #asset Unable to decode the resources
SpeakerRecognitionKit/SpeakerEmbeddingExtractor.swift
requestEmbeddings
SpeakerRecognitionKit/SpeakerDetectorScorer.swift
SpeakerRecognitionKit/SpeakerDetector.swift
SpeakerRecognitionKit/SpeakerRecognitionController.swift
SpeakerRecognitionKit.SRKSpeakerIdentityScoreCard
SpeakerRecognitionKit.SRKSpeakerRecognitionController
audioDurationProcessedInMillis: 
SpeakerRecognitionKit/AssetManagementUtils.swift
speakerDetectorSAT
logit_floor_score
SpeakerRecognitionKit
highScoreThreshold: 
SpeakerRecognitionKit/SpeakerDetectorSAT.swift
logit_ceil_score
init()
SpeakerIdentityScoreCard(
knownUserScores: 
confidentScoreThreshold: 
score_nonvt_scale
score_nonvt_offset
SpeakerRecognitionKit.SRKSpeakerProfileEmbedding
com.apple.speakerrecognition
SpeakerRecognitionKit/SpeakerDetectorPSR.swift
deltaScoreThreshold: 
speakerIdEmbeddingsExtractor
userIdentityClassification: 
SpeakerRecognitionKit/SpeakerProfileEmbeddingValidation.swift
lowScoreThreshold: 
```
