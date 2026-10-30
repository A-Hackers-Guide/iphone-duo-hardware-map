# `BWAudioSplitNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 1 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _splitAtIndex;
I _inputNumberOfChannels;
I _inputChannelLayoutTag;
I _output1ChannelLayoutTag;
I _output2ChannelLayoutTag;
I _cinematicAudioIngestDomain;
@"BWNodeInput" _input;
@"BWNodeOutput" _output1;
@"BWNodeOutput" _output2;
```

## Properties

```
@property (TI,N,V_cinematicAudioIngestDomain) cinematicAudioIngestDomain;
```

## Class methods

```
+[BWAudioSplitNode initialize];
```

## Instance methods

```
-[BWAudioSplitNode renderSampleBuffer:forInput:];
-[BWAudioSplitNode cinematicAudioIngestDomain];
-[BWAudioSplitNode dealloc];
-[BWAudioSplitNode hasNonLiveConfigurationChanges];
-[BWAudioSplitNode initWithInputChannelLayoutTag:output1ChannelLayoutTag:output2ChannelLayoutTag:];
-[BWAudioSplitNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWAudioSplitNode didReachEndOfDataForConfigurationID:input:];
-[BWAudioSplitNode setCinematicAudioIngestDomain:];
-[BWAudioSplitNode nodeSubType];
-[BWAudioSplitNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWAudioSplitNode nodeType];
```
