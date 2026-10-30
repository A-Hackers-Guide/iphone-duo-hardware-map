# `SSREnrollmentQualityMetrics`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
f _inSpeakerSimilarityScore;
@"NSURL" _utterancePath;
d _snr;
d _wer;
```

## Properties

```
@property (T@"NSURL",R,C,N,V_utterancePath) utterancePath;
@property (Td,R,N,V_snr) snr;
@property (Td,R,N,V_wer) wer;
@property (Tf,R,N,V_inSpeakerSimilarityScore) inSpeakerSimilarityScore;
```

## Class methods

```
+[SSREnrollmentQualityMetrics supportsSecureCoding];
```

## Instance methods

```
-[SSREnrollmentQualityMetrics snr];
-[SSREnrollmentQualityMetrics encodeWithCoder:];
-[SSREnrollmentQualityMetrics initWithCoder:];
-[SSREnrollmentQualityMetrics copyWithZone:];
-[SSREnrollmentQualityMetrics wer];
-[SSREnrollmentQualityMetrics inSpeakerSimilarityScore];
-[SSREnrollmentQualityMetrics initWithUtterancePath:snr:wer:inSpeakerSimilarityScores:];
-[SSREnrollmentQualityMetrics utterancePath];
```
