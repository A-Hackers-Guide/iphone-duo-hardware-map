# `IOGPUMTLFence`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
^{__IOGPUDevice={__CFRuntimeBase=QAQ}II^I^^IiIIII{os_unfair_lock_s=I}QQQQ^{IOGPUDeviceCommPage}^{IOGPUClientSharedGlobalRO}@?{os_unfair_lock_s=I}{shmemlog_list=^{_s_shmemlog_}}QQQ{IOGPUDeviceConfigData=IIQQIIQQQII}} _deviceRef;
I _fenceName;
```

## Instance methods

```
-[IOGPUMTLFence initWithDevice:];
-[IOGPUMTLFence dealloc];
```
