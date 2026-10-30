# `IOThreadXPCMappedMemoryTransporter`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _serverMemory;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N,V_serverMemory) serverMemory;
```

## Class methods

```
+[IOThreadXPCMappedMemoryTransporter supportsSecureCoding];
+[IOThreadXPCMappedMemoryTransporter memory:];
```

## Instance methods

```
-[IOThreadXPCMappedMemoryTransporter initWithObject:];
-[IOThreadXPCMappedMemoryTransporter dealloc];
-[IOThreadXPCMappedMemoryTransporter encodeWithCoder:];
-[IOThreadXPCMappedMemoryTransporter initWithCoder:];
-[IOThreadXPCMappedMemoryTransporter isEqual:];
-[IOThreadXPCMappedMemoryTransporter getMappedMemory];
-[IOThreadXPCMappedMemoryTransporter serverMemory];
-[IOThreadXPCMappedMemoryTransporter setServerMemory:];
```
