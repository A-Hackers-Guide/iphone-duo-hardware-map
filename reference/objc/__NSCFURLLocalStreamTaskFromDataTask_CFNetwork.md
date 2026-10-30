# `__NSCFURLLocalStreamTaskFromDataTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFURLLocalStreamTask`
- Protocols: `__NSCFURLSessionConnectionDelegate`
- 9 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
^{__CFReadStream=} _myReadToHisWrite;
B _myReadToHisWriteEOF;
B _myReadToHisWriteSignaled;
{?="domain"q"error"i} _myReadToHisWriteError;
^{__CFWriteStream=} _myWriteToHisRead;
B _myWriteToHisReadEOF;
B _myWriteToHisReadSignaled;
{?="domain"q"error"i} _myWriteToHisReadError;
@"NSMutableArray" _myWriteToHisReadWork;
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
-[__NSCFURLLocalStreamTaskFromDataTask connection:willCacheResponse:responseCallback:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveInformationalResponse:];
-[__NSCFURLLocalStreamTaskFromDataTask connectionWillFinishLoading:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:request:needsNewBodyStreamFromOffset:callback:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:alternatePathAvailable:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:didFinishLoadingWithError:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:_willSendRequestForEstablishedConnection:completion:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveResponse:completion:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:_conditionalRequirementsChanged:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:wasRedirected:newRequest:responseCallback:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveSocketInputStream:outputStream:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveData:completion:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:request:needsNewBodyStreamCallback:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:challenged:authCallback:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveTCPConnection:extraBytes:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:waitingWithReason:];
-[__NSCFURLLocalStreamTaskFromDataTask connection:sentBodyBytes:totalBytes:expectedBytes:];
-[__NSCFURLLocalStreamTaskFromDataTask dealloc];
-[__NSCFURLLocalStreamTaskFromDataTask copyWithZone:];
-[__NSCFURLLocalStreamTaskFromDataTask initWithTask:disavow:];
-[__NSCFURLLocalStreamTaskFromDataTask initWithTask:inputStream:ouptutStream:disavow:];
-[__NSCFURLLocalStreamTaskFromDataTask initWithTask:remainingInputStream:remainingOutputStream:disavow:];
```
