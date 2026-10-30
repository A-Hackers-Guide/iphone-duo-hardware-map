# `MTLCommandBufferDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 3 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"<MTLLogState>" _logState;
```

## Properties

```
@property (TB,D,N) retainedReferences;
@property (TQ,D,N) errorOptions;
@property (T@"<MTLLogState>",&,N,V_logState) logState;
```

## Class methods

```
+[MTLCommandBufferDescriptor allocWithZone:];
+[MTLCommandBufferDescriptor alloc];
```

## Instance methods

```
-[MTLCommandBufferDescriptor copyWithZone:];
-[MTLCommandBufferDescriptor setLogState:];
-[MTLCommandBufferDescriptor logState];
```
