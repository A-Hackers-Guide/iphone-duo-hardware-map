# `VTKeywordAnalyzerNDAPIResult`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _isEarlyWarning;
B _isRescoring;
f _bestScore;
Q _phId;
Q _samplesFed;
Q _bestPhrase;
Q _bestStart;
Q _bestEnd;
Q _samplesAtFire;
Q _startSampleCount;
```

## Properties

```
@property (TQ,N,V_phId) phId;
@property (TQ,N,V_samplesFed) samplesFed;
@property (TQ,N,V_bestPhrase) bestPhrase;
@property (TQ,N,V_bestStart) bestStart;
@property (TQ,N,V_bestEnd) bestEnd;
@property (Tf,N,V_bestScore) bestScore;
@property (TB,N,V_isEarlyWarning) isEarlyWarning;
@property (TB,N,V_isRescoring) isRescoring;
@property (TQ,N,V_samplesAtFire) samplesAtFire;
@property (TQ,N,V_startSampleCount) startSampleCount;
@property (T@"NSDictionary",R,N) dictionary;
```

## Instance methods

```
-[VTKeywordAnalyzerNDAPIResult bestScore];
-[VTKeywordAnalyzerNDAPIResult init];
-[VTKeywordAnalyzerNDAPIResult dictionary];
-[VTKeywordAnalyzerNDAPIResult copyWithZone:];
-[VTKeywordAnalyzerNDAPIResult setBestScore:];
-[VTKeywordAnalyzerNDAPIResult setStartSampleCount:];
-[VTKeywordAnalyzerNDAPIResult startSampleCount];
-[VTKeywordAnalyzerNDAPIResult bestEnd];
-[VTKeywordAnalyzerNDAPIResult setIsRescoring:];
-[VTKeywordAnalyzerNDAPIResult bestPhrase];
-[VTKeywordAnalyzerNDAPIResult bestStart];
-[VTKeywordAnalyzerNDAPIResult isEarlyWarning];
-[VTKeywordAnalyzerNDAPIResult isRescoring];
-[VTKeywordAnalyzerNDAPIResult phId];
-[VTKeywordAnalyzerNDAPIResult samplesAtFire];
-[VTKeywordAnalyzerNDAPIResult samplesFed];
-[VTKeywordAnalyzerNDAPIResult setBestEnd:];
-[VTKeywordAnalyzerNDAPIResult setBestPhrase:];
-[VTKeywordAnalyzerNDAPIResult setBestStart:];
-[VTKeywordAnalyzerNDAPIResult setIsEarlyWarning:];
-[VTKeywordAnalyzerNDAPIResult setPhId:];
-[VTKeywordAnalyzerNDAPIResult setSamplesAtFire:];
-[VTKeywordAnalyzerNDAPIResult setSamplesFed:];
```
