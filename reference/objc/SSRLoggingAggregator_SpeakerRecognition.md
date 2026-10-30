# `SSRLoggingAggregator`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSString" _eventString;
@"NSMutableDictionary" _eventContext;
Q explicitUtteranceIndex;
Q explicitFailedUtteranceIndex;
Q implicitUtteranceIndex;
Q implicitDiscardedUtteranceIndex;
f _voiceProfileUpdateScoreMSE;
Q _voiceProfilePruningFailureReasonCode;
Q _voiceProfileDiscardedUtteranceCount;
Q _voiceProfilePrunedUtteranceCount;
Q _voiceProfileRetainedUtteranceCount;
Q _voiceProfileRetrainingFailureReasonCode;
d _retrainingWaitTime;
Q _speakerRecognitionProcessingStatus;
d _speakerRecognitionWaitTime;
Q _speakerRecognitionPSRProcessingStatus;
Q _speakerRecognitionSATProcessingStatus;
```

## Properties

```
@property (TQ,N,V_voiceProfilePruningFailureReasonCode) voiceProfilePruningFailureReasonCode;
@property (Tf,N,V_voiceProfileUpdateScoreMSE) voiceProfileUpdateScoreMSE;
@property (TQ,N,V_voiceProfileDiscardedUtteranceCount) voiceProfileDiscardedUtteranceCount;
@property (TQ,N,V_voiceProfilePrunedUtteranceCount) voiceProfilePrunedUtteranceCount;
@property (TQ,N,V_voiceProfileRetainedUtteranceCount) voiceProfileRetainedUtteranceCount;
@property (TQ,N,V_voiceProfileRetrainingFailureReasonCode) voiceProfileRetrainingFailureReasonCode;
@property (Td,N,V_retrainingWaitTime) retrainingWaitTime;
@property (TQ,N,V_speakerRecognitionProcessingStatus) speakerRecognitionProcessingStatus;
@property (Td,N,V_speakerRecognitionWaitTime) speakerRecognitionWaitTime;
@property (TQ,N,V_speakerRecognitionPSRProcessingStatus) speakerRecognitionPSRProcessingStatus;
@property (TQ,N,V_speakerRecognitionSATProcessingStatus) speakerRecognitionSATProcessingStatus;
```

## Instance methods

```
-[SSRLoggingAggregator appendVoiceProfileDiscardedImplicitUtteranceScoreWith:];
-[SSRLoggingAggregator appendVoiceProfileExplicitUtteranceScoreWith:];
-[SSRLoggingAggregator appendVoiceProfileFailedExplicitUtteranceScoreWith:];
-[SSRLoggingAggregator appendVoiceProfileImplicitUtteranceScoreWith:];
-[SSRLoggingAggregator initWithEvent:locale:configVersion:];
-[SSRLoggingAggregator pushAnalytics];
-[SSRLoggingAggregator pushAnalyticsWithLazyBlock:];
-[SSRLoggingAggregator retrainingWaitTime];
-[SSRLoggingAggregator setRetrainingWaitTime:];
-[SSRLoggingAggregator setSpeakerRecognitionPSRProcessingStatus:];
-[SSRLoggingAggregator setSpeakerRecognitionProcessingStatus:];
-[SSRLoggingAggregator setSpeakerRecognitionSATProcessingStatus:];
-[SSRLoggingAggregator setSpeakerRecognitionWaitTime:];
-[SSRLoggingAggregator setVoiceProfileDiscardedUtteranceCount:];
-[SSRLoggingAggregator setVoiceProfilePrunedUtteranceCount:];
-[SSRLoggingAggregator setVoiceProfilePruningFailureReasonCode:];
-[SSRLoggingAggregator setVoiceProfileRetainedUtteranceCount:];
-[SSRLoggingAggregator setVoiceProfileRetrainingFailureReasonCode:];
-[SSRLoggingAggregator setVoiceProfileUpdateScoreMSE:];
-[SSRLoggingAggregator setvoiceProfilePrunedUtteranceCount:];
-[SSRLoggingAggregator speakerRecognitionPSRProcessingStatus];
-[SSRLoggingAggregator speakerRecognitionProcessingStatus];
-[SSRLoggingAggregator speakerRecognitionSATProcessingStatus];
-[SSRLoggingAggregator speakerRecognitionWaitTime];
-[SSRLoggingAggregator voiceProfileDiscardedUtteranceCount];
-[SSRLoggingAggregator voiceProfilePrunedUtteranceCount];
-[SSRLoggingAggregator voiceProfilePruningFailureReasonCode];
-[SSRLoggingAggregator voiceProfileRetainedUtteranceCount];
-[SSRLoggingAggregator voiceProfileRetrainingFailureReasonCode];
-[SSRLoggingAggregator voiceProfileUpdateScoreMSE];
```
