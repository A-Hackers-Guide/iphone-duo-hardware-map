# `IOThreadXPCSemaphoreTransporter`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _clientListenableSemaphore;
@"NSObject<OS_xpc_object>" _clientPingableSemaphore;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N,V_clientListenableSemaphore) clientListenableSemaphore;
@property (T@"NSObject<OS_xpc_object>",&,N,V_clientPingableSemaphore) clientPingableSemaphore;
```

## Class methods

```
+[IOThreadXPCSemaphoreTransporter supportsSecureCoding];
+[IOThreadXPCSemaphoreTransporter semaphores:];
```

## Instance methods

```
-[IOThreadXPCSemaphoreTransporter dealloc];
-[IOThreadXPCSemaphoreTransporter encodeWithCoder:];
-[IOThreadXPCSemaphoreTransporter initWithCoder:];
-[IOThreadXPCSemaphoreTransporter isEqual:];
-[IOThreadXPCSemaphoreTransporter clientListenableSemaphore];
-[IOThreadXPCSemaphoreTransporter clientPingableSemaphore];
-[IOThreadXPCSemaphoreTransporter getSemaphores];
-[IOThreadXPCSemaphoreTransporter initWithSemaphores::];
-[IOThreadXPCSemaphoreTransporter setClientListenableSemaphore:];
-[IOThreadXPCSemaphoreTransporter setClientPingableSemaphore:];
```
