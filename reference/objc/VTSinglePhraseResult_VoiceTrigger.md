# `VTSinglePhraseResult`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isSecondChance;
B _isSecondChanceCandidate;
B _isRunningQuasar;
f _combinedScore;
f _ndapiScore;
f _recognizerScore;
Q _phId;
Q _decision;
@"VTKeywordAnalyzerNDAPIResult" _ndapiResult;
```

## Properties

```
@property (TQ,R,N,V_phId) phId;
@property (TQ,R,N,V_decision) decision;
@property (Tf,R,N,V_combinedScore) combinedScore;
@property (Tf,R,N,V_ndapiScore) ndapiScore;
@property (T@"VTKeywordAnalyzerNDAPIResult",R,N,V_ndapiResult) ndapiResult;
@property (Tf,R,N,V_recognizerScore) recognizerScore;
@property (TB,R,N,V_isSecondChance) isSecondChance;
@property (TB,R,N,V_isSecondChanceCandidate) isSecondChanceCandidate;
@property (TB,R,N,V_isRunningQuasar) isRunningQuasar;
```

## Instance methods

```
-[VTSinglePhraseResult decision];
-[VTSinglePhraseResult copyWithZone:];
-[VTSinglePhraseResult combinedScore];
-[VTSinglePhraseResult recognizerScore];
-[VTSinglePhraseResult isSecondChance];
-[VTSinglePhraseResult isRunningQuasar];
-[VTSinglePhraseResult initWithPhId:keywordDetectorDecision:combinedScore:ndapiScore:ndapiResult:recognizerScore:isSecondChance:isSecondChanceCandidate:isRunningQuasar:];
-[VTSinglePhraseResult isSecondChanceCandidate];
-[VTSinglePhraseResult ndapiResult];
-[VTSinglePhraseResult ndapiScore];
-[VTSinglePhraseResult phId];
```
