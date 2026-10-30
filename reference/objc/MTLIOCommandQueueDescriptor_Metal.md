# `MTLIOCommandQueueDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _maxCommandBufferCount;
q _priority;
@"<MTLIOScratchBufferAllocator>" _scratchBufferAllocator;
q _type;
Q _maxWorkerThreads;
Q _maxCommandsInFlight;
```

## Properties

```
@property (TQ) maxWorkerThreads;
@property (TQ,N,V_maxCommandBufferCount) maxCommandBufferCount;
@property (Tq,N,V_priority) priority;
@property (Tq,N,V_type) type;
@property (TQ,N,V_maxCommandsInFlight) maxCommandsInFlight;
@property (T@"<MTLIOScratchBufferAllocator>",&,V_scratchBufferAllocator) scratchBufferAllocator;
```

## Instance methods

```
-[MTLIOCommandQueueDescriptor priority];
-[MTLIOCommandQueueDescriptor formattedDescription:];
-[MTLIOCommandQueueDescriptor init];
-[MTLIOCommandQueueDescriptor setPriority:];
-[MTLIOCommandQueueDescriptor dealloc];
-[MTLIOCommandQueueDescriptor maxCommandBufferCount];
-[MTLIOCommandQueueDescriptor setType:];
-[MTLIOCommandQueueDescriptor type];
-[MTLIOCommandQueueDescriptor setMaxCommandBufferCount:];
-[MTLIOCommandQueueDescriptor hash];
-[MTLIOCommandQueueDescriptor description];
-[MTLIOCommandQueueDescriptor copyWithZone:];
-[MTLIOCommandQueueDescriptor isEqual:];
-[MTLIOCommandQueueDescriptor maxCommandsInFlight];
-[MTLIOCommandQueueDescriptor maxWorkerThreads];
-[MTLIOCommandQueueDescriptor scratchBufferAllocator];
-[MTLIOCommandQueueDescriptor setMaxCommandsInFlight:];
-[MTLIOCommandQueueDescriptor setMaxWorkerThreads:];
-[MTLIOCommandQueueDescriptor setScratchBufferAllocator:];
```
