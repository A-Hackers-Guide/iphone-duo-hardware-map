# `SSRVoiceActivityDetector`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EARCaesuraSilencePosteriorGeneratorDelegate`
- 11 instance variables, 14 properties, 26 instance methods, 0 class methods

## Instance variables

```
Q _numConsecutiveNonSilenceFrames;
B _endpointReported;
B _startpointReported;
@"SSRSpeakerRecognitionContext" _context;
@"<SSRVoiceActivityDetectorDelegate>" _delegate;
@"EARCaesuraSilencePosteriorGenerator" _earSpg;
@"_EAREndpointer" _hybridClassifier;
@"_EARDefaultServerEndpointFeatures" _defSepFeats;
q _segmentStartPointSampleCount;
Q _numSamplesProcessed;
@"NSObject<OS_dispatch_queue>" _spgQueue;
```

## Properties

```
@property (T@"SSRSpeakerRecognitionContext",&,N,V_context) context;
@property (T@"<SSRVoiceActivityDetectorDelegate>",W,N,V_delegate) delegate;
@property (T@"EARCaesuraSilencePosteriorGenerator",&,N,V_earSpg) earSpg;
@property (T@"_EAREndpointer",&,N,V_hybridClassifier) hybridClassifier;
@property (T@"_EARDefaultServerEndpointFeatures",&,N,V_defSepFeats) defSepFeats;
@property (Tq,N,V_segmentStartPointSampleCount) segmentStartPointSampleCount;
@property (TQ,N,V_numSamplesProcessed) numSamplesProcessed;
@property (TB,N,V_endpointReported) endpointReported;
@property (TB,N,V_startpointReported) startpointReported;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_spgQueue) spgQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRVoiceActivityDetector initWithContext:delegate:];
-[SSRVoiceActivityDetector setDelegate:];
-[SSRVoiceActivityDetector setContext:];
-[SSRVoiceActivityDetector delegate];
-[SSRVoiceActivityDetector context];
-[SSRVoiceActivityDetector endAudio];
-[SSRVoiceActivityDetector numSamplesProcessed];
-[SSRVoiceActivityDetector setNumSamplesProcessed:];
-[SSRVoiceActivityDetector clientSilenceFeaturesAvailable:];
-[SSRVoiceActivityDetector hybridClassifier];
-[SSRVoiceActivityDetector resetWithContext:];
-[SSRVoiceActivityDetector setHybridClassifier:];
-[SSRVoiceActivityDetector setSpgQueue:];
-[SSRVoiceActivityDetector spgQueue];
-[SSRVoiceActivityDetector setDefSepFeats:];
-[SSRVoiceActivityDetector _initializeSPGWithContext:];
-[SSRVoiceActivityDetector defSepFeats];
-[SSRVoiceActivityDetector earSpg];
-[SSRVoiceActivityDetector endpointReported];
-[SSRVoiceActivityDetector processAudioData:numSamples:];
-[SSRVoiceActivityDetector segmentStartPointSampleCount];
-[SSRVoiceActivityDetector setEarSpg:];
-[SSRVoiceActivityDetector setEndpointReported:];
-[SSRVoiceActivityDetector setSegmentStartPointSampleCount:];
-[SSRVoiceActivityDetector setStartpointReported:];
-[SSRVoiceActivityDetector startpointReported];
```
