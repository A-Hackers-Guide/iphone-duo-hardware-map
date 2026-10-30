# `AVCDOSDataOutputStorage`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureOutput<AVCaptureDataOutputDelegateOverride>" _dataOutput;
@"NSMutableArray" _synchronizedDataQueue;
@"NSObject<OS_dispatch_queue>" _delegateOverrideCallbackQueue;
@"NSMutableArray" _timestampAdjustmentsDataQueue;
```

## Properties

```
@property (T@"AVCaptureOutput<AVCaptureDataOutputDelegateOverride>",R,N,V_dataOutput) dataOutput;
@property (T@"NSMutableArray",R,N,V_synchronizedDataQueue) synchronizedDataQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_delegateOverrideCallbackQueue) delegateOverrideCallbackQueue;
@property (TB,R,N,GisLive) live;
@property (T@"NSMutableArray",&,N,V_timestampAdjustmentsDataQueue) timestampAdjustmentsDataQueue;
```

## Instance methods

```
-[AVCDOSDataOutputStorage dealloc];
-[AVCDOSDataOutputStorage isLive];
-[AVCDOSDataOutputStorage delegateOverrideCallbackQueue];
-[AVCDOSDataOutputStorage dataOutput];
-[AVCDOSDataOutputStorage hasAllExpectedSynchronizedDataForLeaderTimestamp:];
-[AVCDOSDataOutputStorage initWithDataOutput:];
-[AVCDOSDataOutputStorage setTimestampAdjustmentsDataQueue:];
-[AVCDOSDataOutputStorage synchronizedDataQueue];
-[AVCDOSDataOutputStorage timestampAdjustmentsDataQueue];
-[AVCDOSDataOutputStorage updateDelegateOverrideCallbackQueueQOSClass:];
```
