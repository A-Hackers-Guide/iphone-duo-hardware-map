# `SRSpeechMetrics`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSCopying`, `NSSecureCoding`
- 8 instance variables, 12 properties, 20 instance methods, 3 class methods

## Instance variables

```
@"NSString" _sessionIdentifier;
Q _sessionFlags;
@"NSDate" _timestamp;
d _timeSinceAudioStart;
@"SRAudioLevel" _audioLevel;
@"SFSpeechRecognitionResult" _speechRecognition;
@"SNClassificationResult" _soundClassification;
@"SRSpeechExpression" _speechExpression;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sessionIdentifier) sessionIdentifier;
@property (TQ,R,N,V_sessionFlags) sessionFlags;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (Td,R,N,V_timeSinceAudioStart) timeSinceAudioStart;
@property (T@"SRAudioLevel",R,N,V_audioLevel) audioLevel;
@property (T@"SFSpeechRecognitionResult",R,N,V_speechRecognition) speechRecognition;
@property (T@"SNClassificationResult",R,N,V_soundClassification) soundClassification;
@property (T@"SRSpeechExpression",R,N,V_speechExpression) speechExpression;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRSpeechMetrics supportsSecureCoding];
+[SRSpeechMetrics initialize];
+[SRSpeechMetrics new];
```

## Instance methods

```
-[SRSpeechMetrics sessionIdentifier];
-[SRSpeechMetrics sessionFlags];
-[SRSpeechMetrics init];
-[SRSpeechMetrics dealloc];
-[SRSpeechMetrics timestamp];
-[SRSpeechMetrics encodeWithCoder:];
-[SRSpeechMetrics hash];
-[SRSpeechMetrics audioLevel];
-[SRSpeechMetrics description];
-[SRSpeechMetrics initWithCoder:];
-[SRSpeechMetrics copyWithZone:];
-[SRSpeechMetrics isEqual:];
-[SRSpeechMetrics binarySampleRepresentation];
-[SRSpeechMetrics initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRSpeechMetrics initWithSessionIdentifier:sessionFlags:timestamp:audioLevel:speechRecognition:soundClassification:speechExpression:];
-[SRSpeechMetrics initWithSessionIdentifier:sessionFlags:timestamp:timeSinceAudioStart:audioLevel:speechRecognition:soundClassification:speechExpression:];
-[SRSpeechMetrics soundClassification];
-[SRSpeechMetrics speechExpression];
-[SRSpeechMetrics speechRecognition];
-[SRSpeechMetrics timeSinceAudioStart];
```
