# `BWAudioRemixAnalysisMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 8 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"AudioRemixSessionManager" _movieRemixSessionManager;
B _shouldSendData;
@"BWNodeOutput" _metadataOutput;
B _multiCamClientCompositingEnabled;
B _expectsToRecordOnlyOnce;
{?="value"q"timescale"i"flags"I"epoch"q} _startRecordingPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _currentPTS;
^{opaqueCMFormatDescription=} _audioMetadataFormatDescription;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_metadataOutput) metadataOutput;
@property (TB,N,V_multiCamClientCompositingEnabled) multiCamClientCompositingEnabled;
@property (TB,N,V_expectsToRecordOnlyOnce) expectsToRecordOnlyOnce;
@property (T^{opaqueCMFormatDescription=},R,N,V_audioMetadataFormatDescription) audioMetadataFormatDescription;
```

## Class methods

```
+[BWAudioRemixAnalysisMetadataNode initialize];
```

## Instance methods

```
-[BWAudioRemixAnalysisMetadataNode metadataOutput];
-[BWAudioRemixAnalysisMetadataNode renderSampleBuffer:forInput:];
-[BWAudioRemixAnalysisMetadataNode init];
-[BWAudioRemixAnalysisMetadataNode dealloc];
-[BWAudioRemixAnalysisMetadataNode multiCamClientCompositingEnabled];
-[BWAudioRemixAnalysisMetadataNode hasNonLiveConfigurationChanges];
-[BWAudioRemixAnalysisMetadataNode setExpectsToRecordOnlyOnce:];
-[BWAudioRemixAnalysisMetadataNode setMultiCamClientCompositingEnabled:];
-[BWAudioRemixAnalysisMetadataNode resetAnalyzer];
-[BWAudioRemixAnalysisMetadataNode expectsToRecordOnlyOnce];
-[BWAudioRemixAnalysisMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWAudioRemixAnalysisMetadataNode audioMetadataFormatDescription];
-[BWAudioRemixAnalysisMetadataNode nodeSubType];
-[BWAudioRemixAnalysisMetadataNode didSelectFormat:forInput:];
-[BWAudioRemixAnalysisMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWAudioRemixAnalysisMetadataNode nodeType];
```
