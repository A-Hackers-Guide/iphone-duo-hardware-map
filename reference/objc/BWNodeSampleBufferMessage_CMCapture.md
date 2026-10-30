# `BWNodeSampleBufferMessage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNodeMessage`
- 3 instance variables, 3 properties, 5 instance methods, 3 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _sampleBuffer;
@"FigCaptureStillImageSettings" _stillImageSettings;
@"FigCaptureRecordingSettings" _recordingSettings;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R) sampleBuffer;
@property (T@"FigCaptureStillImageSettings",R) stillImageSettings;
@property (T@"FigCaptureRecordingSettings",R) recordingSettings;
```

## Class methods

```
+[BWNodeSampleBufferMessage newMessageWithSampleBuffer:];
+[BWNodeSampleBufferMessage newMessageWithSampleBuffer:recordingSettings:];
+[BWNodeSampleBufferMessage newMessageWithSampleBuffer:stillImageSettings:];
```

## Instance methods

```
-[BWNodeSampleBufferMessage stillImageSettings];
-[BWNodeSampleBufferMessage dealloc];
-[BWNodeSampleBufferMessage description];
-[BWNodeSampleBufferMessage sampleBuffer];
-[BWNodeSampleBufferMessage recordingSettings];
```
