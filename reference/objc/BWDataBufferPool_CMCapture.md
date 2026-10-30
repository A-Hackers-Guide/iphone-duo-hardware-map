# `BWDataBufferPool`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"<BWDataBufferBackedFormat>" _format;
Q _capacity;
@"NSString" _name;
B _clientProvidesPool;
@"NSDictionary" _additionalDataBufferAttributes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _dataBufferPoolConfigurationLock;
^{__CVDataBufferPool=} _dataBufferPool;
@"NSDictionary" _dataBufferPoolAuxAttributes;
i _dataBufferPoolCreateError;
```

## Properties

```
@property (T@"NSString",R) name;
@property (TQ,R,N) capacity;
@property (TI,R,N) dataFormat;
@property (T^{__CVDataBufferPool=},R,N) cvDataBufferPool;
@property (T^{__CFDictionary=},R,N) cvDataBufferPoolAuxAttributes;
@property (T@"<BWDataBufferBackedFormat>",R,N) format;
```

## Class methods

```
+[BWDataBufferPool initialize];
```

## Instance methods

```
-[BWDataBufferPool setCapacity:];
-[BWDataBufferPool capacity];
-[BWDataBufferPool flushToMinimumCapacity:];
-[BWDataBufferPool dealloc];
-[BWDataBufferPool enumerateSurfacesUsingBlock:];
-[BWDataBufferPool prefetchWithCompletionHandler:];
-[BWDataBufferPool dataFormat];
-[BWDataBufferPool format];
-[BWDataBufferPool name];
-[BWDataBufferPool setCVDataBufferPool:attributes:];
-[BWDataBufferPool cvDataBufferPool];
-[BWDataBufferPool cvDataBufferPoolAuxAttributes];
-[BWDataBufferPool initWithFormat:capacity:name:clientProvidesPool:];
-[BWDataBufferPool newDataBuffer];
```
