# `BWAudioConverterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 1 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _settings;
^{OpaqueFigSampleBufferProcessor=} _audioCompressionSBP;
B _cinematicAudioCapture;
B _multiCamClientCompositingEnabled;
B _expectsToRecordOnlyOnce;
i _movieRecordingEndOfDataBehavior;
```

## Properties

```
@property (T@"NSDictionary",R,N) gaplessPlaybackInfo;
```

## Class methods

```
+[BWAudioConverterNode initialize];
```

## Instance methods

```
-[BWAudioConverterNode setCinematicAudioCapture:];
-[BWAudioConverterNode renderSampleBuffer:forInput:];
-[BWAudioConverterNode isMultiCamClientCompositingEnabled];
-[BWAudioConverterNode setSettings:];
-[BWAudioConverterNode init];
-[BWAudioConverterNode settings];
-[BWAudioConverterNode dealloc];
-[BWAudioConverterNode setExpectsToRecordOnlyOnce:];
-[BWAudioConverterNode movieRecordingEndOfDataBehavior];
-[BWAudioConverterNode setMultiCamClientCompositingEnabled:];
-[BWAudioConverterNode acquireHardware];
-[BWAudioConverterNode setMovieRecordingEndOfDataBehavior:];
-[BWAudioConverterNode expectsToRecordOnlyOnce];
-[BWAudioConverterNode didReachEndOfDataForConfigurationID:input:];
-[BWAudioConverterNode isCinematicAudioCapture];
-[BWAudioConverterNode nodeSubType];
-[BWAudioConverterNode didSelectFormat:forInput:];
-[BWAudioConverterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWAudioConverterNode nodeType];
-[BWAudioConverterNode gaplessPlaybackInfo];
-[BWAudioConverterNode relinquishHardware];
```
