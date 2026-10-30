# `BWAttachedMediaTimeMachineSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- Protocols: `BWAttachedMediaTimeMachineDelegate`
- 5 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _timeMachineFrames;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _timeMachineLock;
i _timeMachineCapacity;
@"NSArray" _attachedMediaKeys;
@"NSArray" _metadataKeys;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWAttachedMediaTimeMachineSinkNode initialize];
```

## Instance methods

```
-[BWAttachedMediaTimeMachineSinkNode renderSampleBuffer:forInput:];
-[BWAttachedMediaTimeMachineSinkNode dealloc];
-[BWAttachedMediaTimeMachineSinkNode initWithTimeMachineCapacity:attachedMediaKeys:metadataKeys:sinkID:];
-[BWAttachedMediaTimeMachineSinkNode getMetadataDictionaryForPts:];
-[BWAttachedMediaTimeMachineSinkNode copyAttachedMediaSampleBufferForPts:attachedMediaKey:];
-[BWAttachedMediaTimeMachineSinkNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWAttachedMediaTimeMachineSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWAttachedMediaTimeMachineSinkNode nodeSubType];
```
