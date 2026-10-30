# `MTL4CommandQueueDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _lockParameterBufferSizeToMax;
B _supportMTLEvent;
@"NSString" _label;
@"NSObject<OS_dispatch_queue>" _feedbackQueue;
Q _qosLevel;
```

## Properties

```
@property (TB,N,V_lockParameterBufferSizeToMax) lockParameterBufferSizeToMax;
@property (TB,N,V_supportMTLEvent) supportMTLEvent;
@property (TQ,N,V_qosLevel) qosLevel;
@property (T@"NSString",C,N,V_label) label;
@property (T@"NSObject<OS_dispatch_queue>",N,V_feedbackQueue) feedbackQueue;
```

## Instance methods

```
-[MTL4CommandQueueDescriptor qosLevel];
-[MTL4CommandQueueDescriptor init];
-[MTL4CommandQueueDescriptor label];
-[MTL4CommandQueueDescriptor setLabel:];
-[MTL4CommandQueueDescriptor dealloc];
-[MTL4CommandQueueDescriptor lockParameterBufferSizeToMax];
-[MTL4CommandQueueDescriptor setLockParameterBufferSizeToMax:];
-[MTL4CommandQueueDescriptor hash];
-[MTL4CommandQueueDescriptor setQosLevel:];
-[MTL4CommandQueueDescriptor copyWithZone:];
-[MTL4CommandQueueDescriptor isEqual:];
-[MTL4CommandQueueDescriptor supportMTLEvent];
-[MTL4CommandQueueDescriptor feedbackQueue];
-[MTL4CommandQueueDescriptor setFeedbackQueue:];
-[MTL4CommandQueueDescriptor setSupportMTLEvent:];
```
