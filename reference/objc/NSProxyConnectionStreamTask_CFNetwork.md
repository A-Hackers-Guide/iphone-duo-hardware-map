# `NSProxyConnectionStreamTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSProxyConnection`
- Protocols: `NSStreamDelegate`, `NSURLSessionStreamDelegate`
- 8 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
B _isConnected;
@"NSString" _host;
i _port;
B _dataAvailableForReading;
@"NSInputStream" _inputStream;
@"NSOutputStream" _outputStream;
@"NSURLSessionStreamTask" _streamTask;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NSProxyConnectionStreamTask dealloc];
-[NSProxyConnectionStreamTask stream:handleEvent:];
-[NSProxyConnectionStreamTask cancel];
-[NSProxyConnectionStreamTask URLSession:streamTask:didBecomeInputStream:outputStream:];
-[NSProxyConnectionStreamTask initWithHost:port:queue:configuration:];
-[NSProxyConnectionStreamTask read:handler:];
-[NSProxyConnectionStreamTask write:handler:];
```
