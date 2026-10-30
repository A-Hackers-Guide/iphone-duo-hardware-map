# `SSRSpeakerRecognizer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",R,N) lastScoreCard;
```

## Instance methods

```
-[SSRSpeakerRecognizer initWithContext:delegate:];
-[SSRSpeakerRecognizer endAudio];
-[SSRSpeakerRecognizer resetWithContext:];
-[SSRSpeakerRecognizer getSpeakerRecognizerProcessingTime];
-[SSRSpeakerRecognizer lastScoreCard];
-[SSRSpeakerRecognizer processAudioData:numSamples:];
```
