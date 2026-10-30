# `BWAudioFileSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFileSinkNode`
- 12 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"FigStateMachine" _stateMachine;
^{OpaqueFigFormatWriter=} _formatWriter;
^{OpaqueCMByteStream=} _byteStream;
i _trackID;
B _didBeginFileWriterSession;
* _parentPath;
@"FigCaptureAudioFileRecordingSettings" _settings;
{?="value"q"timescale"i"flags"I"epoch"q} _startPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _curFileDuration;
Q _curFileSize;
Q _adjustedMinFreeDiskSpace;
@"NSObject<OS_dispatch_queue>" _propertySyncQueue;
```

## Class methods

```
+[BWAudioFileSinkNode initialize];
```

## Instance methods

```
-[BWAudioFileSinkNode initWithSinkID:];
-[BWAudioFileSinkNode renderSampleBuffer:forInput:];
-[BWAudioFileSinkNode lastFileSize];
-[BWAudioFileSinkNode lastFileDuration];
-[BWAudioFileSinkNode dealloc];
-[BWAudioFileSinkNode nodeSubType];
-[BWAudioFileSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWAudioFileSinkNode didReachEndOfDataForInput:];
```
