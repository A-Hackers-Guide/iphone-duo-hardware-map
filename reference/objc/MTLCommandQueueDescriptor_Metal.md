# `MTLCommandQueueDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 6 instance methods, 3 class methods

## Instance variables

```
Q _maxCommandBufferCount;
@"<MTLLogState>" _logState;
```

## Properties

```
@property (TQ,N,V_maxCommandBufferCount) maxCommandBufferCount;
@property (T@"<MTLLogState>",&,N,V_logState) logState;
```

## Class methods

```
+[MTLCommandQueueDescriptor allocWithZone:];
+[MTLCommandQueueDescriptor alloc];
+[MTLCommandQueueDescriptor commandQueueDescriptor];
```

## Instance methods

```
-[MTLCommandQueueDescriptor maxCommandBufferCount];
-[MTLCommandQueueDescriptor reset];
-[MTLCommandQueueDescriptor setMaxCommandBufferCount:];
-[MTLCommandQueueDescriptor copyWithZone:];
-[MTLCommandQueueDescriptor setLogState:];
-[MTLCommandQueueDescriptor logState];
```
