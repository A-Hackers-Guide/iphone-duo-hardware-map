# `NSProxyConnection`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _doCleanupWhenWritesCompleted;
@"NSObject<OS_tcp_connection>" _connection;
@"<NSProxyConnectionDelegate>" _delegate;
q _pendingWrites;
```

## Instance methods

```
-[NSProxyConnection dealloc];
-[NSProxyConnection cancel];
-[NSProxyConnection initWithHost:port:queue:configuration:];
-[NSProxyConnection read:handler:];
-[NSProxyConnection write:handler:];
```
