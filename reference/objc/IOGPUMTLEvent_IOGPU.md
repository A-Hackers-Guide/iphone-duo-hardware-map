# `IOGPUMTLEvent`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
^{__IOGPUDevice={__CFRuntimeBase=QAQ}II^I^^IiIIII{os_unfair_lock_s=I}QQQQ^{IOGPUDeviceCommPage}^{IOGPUClientSharedGlobalRO}@?{os_unfair_lock_s=I}{shmemlog_list=^{_s_shmemlog_}}QQQ{IOGPUDeviceConfigData=IIQQIIQQQII}} _deviceRef;
I _eventName;
Q _globalTraceObjectID;
Q _eventOptions;
B _enableBarrier;
```

## Properties

```
@property (TB,N,V_enableBarrier) enableBarrier;
@property (TB,R,N) supportsRollback;
@property (TI,R,N,V_eventName) eventName;
```

## Instance methods

```
-[IOGPUMTLEvent dealloc];
-[IOGPUMTLEvent eventName];
-[IOGPUMTLEvent supportsRollback];
-[IOGPUMTLEvent enableBarrier];
-[IOGPUMTLEvent setEnableBarrier:];
-[IOGPUMTLEvent _encodeIOGPUKernelConditionalEventAbortCommandArgs:];
-[IOGPUMTLEvent _encodeIOGPUKernelSignalEventAgentCommandArgs:value:agentMask:];
-[IOGPUMTLEvent _encodeIOGPUKernelSignalEventCommandArgs:value:];
-[IOGPUMTLEvent _encodeIOGPUKernelSignalEventScheduledCommandArgs:value:];
-[IOGPUMTLEvent _encodeIOGPUKernelWaitEventCommandArgs:value:timeout:];
-[IOGPUMTLEvent _isSharedEvent];
-[IOGPUMTLEvent initWithDeviceRef:];
-[IOGPUMTLEvent initWithDeviceRef:options:];
```
