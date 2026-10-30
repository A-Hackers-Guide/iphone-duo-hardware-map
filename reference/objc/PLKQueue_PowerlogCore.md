# `PLKQueue`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _enabled;
i _kQueue;
i _fileDescriptor;
^{__CFRunLoopSource=} _kqueueDescriptorSource;
^{__CFFileDescriptor=} _kqueueDescriptorRef;
@"NSString" _path;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _kQueueBlock;
```

## Properties

```
@property (Ti,V_kQueue) kQueue;
@property (Ti,V_fileDescriptor) fileDescriptor;
@property (T^{__CFRunLoopSource=},V_kqueueDescriptorSource) kqueueDescriptorSource;
@property (T^{__CFFileDescriptor=},V_kqueueDescriptorRef) kqueueDescriptorRef;
@property (T@"NSString",C,V_path) path;
@property (T@"NSObject<OS_dispatch_queue>",&,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_kQueueBlock) kQueueBlock;
@property (TB,N,V_enabled) enabled;
```

## Instance methods

```
-[PLKQueue dispatchQueue];
-[PLKQueue enabled];
-[PLKQueue setDispatchQueue:];
-[PLKQueue setEnabled:];
-[PLKQueue fileDescriptor];
-[PLKQueue setFileDescriptor:];
-[PLKQueue setPath:];
-[PLKQueue path];
-[PLKQueue setKQueueBlock:];
-[PLKQueue initWithPath:withDispatchQueue:withBlock:];
-[PLKQueue kQueue];
-[PLKQueue kQueueBlock];
-[PLKQueue kqueueDescriptorRef];
-[PLKQueue kqueueDescriptorSource];
-[PLKQueue setKQueue:];
-[PLKQueue setKqueueDescriptorRef:];
-[PLKQueue setKqueueDescriptorSource:];
```
