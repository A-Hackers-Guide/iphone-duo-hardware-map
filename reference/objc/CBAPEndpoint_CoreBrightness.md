# `CBAPEndpoint`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"AFKEndpointInterface" _endpoint;
@"NSObject<OS_dispatch_queue>" _epQueue;
I _service;
@"NSObject<OS_os_log>" _logHandle;
```

## Class methods

```
+[CBAPEndpoint endpointForRole:];
```

## Instance methods

```
-[CBAPEndpoint dealloc];
-[CBAPEndpoint setProperty:property:];
-[CBAPEndpoint copyProperty:];
-[CBAPEndpoint enqueueCommandSync:inputBuffer:inputBufferSize:responseObj:options:];
-[CBAPEndpoint findDCPServiceWithName:role:];
-[CBAPEndpoint initWithServiceName:role:];
-[CBAPEndpoint sendCommand:inputBuffer:inputBufferSize:];
-[CBAPEndpoint sendOOBCommand:inputBuffer:inputBufferSize:];
```
