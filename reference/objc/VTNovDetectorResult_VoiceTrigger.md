# `VTNovDetectorResult`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _earlyWarning;
B _isRescoring;
f _bestScore;
Q _sampleFed;
Q _bestPhrase;
Q _bestStart;
Q _bestEnd;
```

## Properties

```
@property (TQ,N,V_sampleFed) sampleFed;
@property (TQ,N,V_bestPhrase) bestPhrase;
@property (TQ,N,V_bestStart) bestStart;
@property (TQ,N,V_bestEnd) bestEnd;
@property (Tf,N,V_bestScore) bestScore;
@property (TB,N,V_earlyWarning) earlyWarning;
@property (TB,N,V_isRescoring) isRescoring;
@property (T@"NSDictionary",R,N) dictionary;
```

## Instance methods

```
-[VTNovDetectorResult bestScore];
-[VTNovDetectorResult dictionary];
-[VTNovDetectorResult initWithResult:];
-[VTNovDetectorResult setBestScore:];
-[VTNovDetectorResult bestEnd];
-[VTNovDetectorResult setIsRescoring:];
-[VTNovDetectorResult bestPhrase];
-[VTNovDetectorResult bestStart];
-[VTNovDetectorResult earlyWarning];
-[VTNovDetectorResult isRescoring];
-[VTNovDetectorResult sampleFed];
-[VTNovDetectorResult setBestEnd:];
-[VTNovDetectorResult setBestPhrase:];
-[VTNovDetectorResult setBestStart:];
-[VTNovDetectorResult setEarlyWarning:];
-[VTNovDetectorResult setSampleFed:];
```
