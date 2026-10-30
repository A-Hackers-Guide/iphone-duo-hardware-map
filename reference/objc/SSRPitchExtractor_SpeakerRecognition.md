# `SSRPitchExtractor`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EARAudioResultsGeneratorDelegate`
- 2 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"EARAudioResultsGenerator" _resultsGenerator;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"EARAudioResultsGenerator",&,N,V_resultsGenerator) resultsGenerator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRPitchExtractor initWithDefaultParameters];
-[SSRPitchExtractor queue];
-[SSRPitchExtractor initWithAsset:];
-[SSRPitchExtractor setQueue:];
-[SSRPitchExtractor getPitchForUtteranceAudioFiles:];
-[SSRPitchExtractor _getPitchHzFromRawData:];
-[SSRPitchExtractor _getVoicingProbFromRawData:];
-[SSRPitchExtractor _getVoicingWeightedPitchForResultMatrix:];
-[SSRPitchExtractor _initWithConfigPath:];
-[SSRPitchExtractor _processAudioFileURL:];
-[SSRPitchExtractor resultsGenerator];
-[SSRPitchExtractor setResultsGenerator:];
```
