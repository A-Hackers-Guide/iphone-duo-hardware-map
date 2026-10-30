# `AVOutputContextMonitor`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{weak_ptr<avas::client::SessionCore>="__ptr_"^{SessionCore}"__cntrl_"^{__shared_weak_count}} mSessionCore;
@"AVOutputContext" mAVOutputContext;
```

## Instance methods

```
-[AVOutputContextMonitor dealloc];
-[AVOutputContextMonitor handleAVOutputContextOutputDeviceChange:];
-[AVOutputContextMonitor handleAVOutputContextOutputDevicesChange:];
-[AVOutputContextMonitor initWithSessionCore:routingContextUID:];
```
