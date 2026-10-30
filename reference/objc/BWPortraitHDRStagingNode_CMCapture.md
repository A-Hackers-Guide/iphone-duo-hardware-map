# `BWPortraitHDRStagingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _settingsID;
B _passthroughBuffer;
^{opaqueCMSampleBuffer=} _stagedBuffer;
```

## Class methods

```
+[BWPortraitHDRStagingNode initialize];
```

## Instance methods

```
-[BWPortraitHDRStagingNode renderSampleBuffer:forInput:];
-[BWPortraitHDRStagingNode init];
-[BWPortraitHDRStagingNode dealloc];
-[BWPortraitHDRStagingNode nodeSubType];
-[BWPortraitHDRStagingNode didSelectFormat:forInput:];
-[BWPortraitHDRStagingNode handleNodeError:forInput:];
-[BWPortraitHDRStagingNode nodeType];
-[BWPortraitHDRStagingNode bufferReceivedWithFlags:error:];
```
