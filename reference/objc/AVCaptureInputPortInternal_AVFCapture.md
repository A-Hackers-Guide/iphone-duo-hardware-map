# `AVCaptureInputPortInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureInput" input;
@"NSString" mediaType;
^{opaqueCMFormatDescription=} formatDescription;
^{OpaqueCMClock=} clock;
B enabled;
i changeSeed;
@"NSString" sourceID;
@"NSString" sourceDeviceType;
q sourceDevicePosition;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} internalLock;
```

## Instance methods

```
-[AVCaptureInputPortInternal init];
-[AVCaptureInputPortInternal dealloc];
```
