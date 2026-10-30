# `BWRefinedCinematographyNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"PTCinematographyRefinement" _refinementSession;
B _isRefinementSessionActive;
i _numEODMessagesReceived;
{?="value"q"timescale"i"flags"I"epoch"q} _lastAudioPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _firstAudioPTS;
@"BWNodeInput" _videoInput;
@"BWNodeInput" _audioInput;
@"BWNodeOutput" _videoOutput;
@"BWNodeOutput" _audioOutput;
```

## Properties

```
@property (T@"BWNodeInput",R,N,V_videoInput) videoInput;
@property (T@"BWNodeInput",R,N,V_audioInput) audioInput;
@property (T@"BWNodeOutput",R,N,V_videoOutput) videoOutput;
@property (T@"BWNodeOutput",R,N,V_audioOutput) audioOutput;
```

## Class methods

```
+[BWRefinedCinematographyNode initialize];
```

## Instance methods

```
-[BWRefinedCinematographyNode renderSampleBuffer:forInput:];
-[BWRefinedCinematographyNode dealloc];
-[BWRefinedCinematographyNode audioOutput];
-[BWRefinedCinematographyNode videoOutput];
-[BWRefinedCinematographyNode nodeSubType];
-[BWRefinedCinematographyNode didSelectFormat:forInput:];
-[BWRefinedCinematographyNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWRefinedCinematographyNode nodeType];
-[BWRefinedCinematographyNode audioInput];
-[BWRefinedCinematographyNode didReachEndOfDataForInput:];
-[BWRefinedCinematographyNode initWithAudioEnabled:];
-[BWRefinedCinematographyNode videoInput];
```
