# `BWSceneClassifierFrameGateNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _discardsBlurryFrames;
i _maxFrameRate;
{?="value"q"timescale"i"flags"I"epoch"q} _lastEmittedPTS;
i _inputFrameCount;
```

## Class methods

```
+[BWSceneClassifierFrameGateNode initialize];
```

## Instance methods

```
-[BWSceneClassifierFrameGateNode renderSampleBuffer:forInput:];
-[BWSceneClassifierFrameGateNode dealloc];
-[BWSceneClassifierFrameGateNode nodeSubType];
-[BWSceneClassifierFrameGateNode didSelectFormat:forInput:];
-[BWSceneClassifierFrameGateNode nodeType];
-[BWSceneClassifierFrameGateNode discardsBlurryFrames];
-[BWSceneClassifierFrameGateNode initWithMaxOutputFrameRate:];
-[BWSceneClassifierFrameGateNode setDiscardsBlurryFrames:];
```
