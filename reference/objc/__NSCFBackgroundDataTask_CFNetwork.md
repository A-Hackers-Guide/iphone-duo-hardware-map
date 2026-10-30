# `__NSCFBackgroundDataTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFBackgroundSessionTask`
- 8 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<RequestBody>="__ptr_"^{RequestBody}"__cntrl_"^{__shared_weak_count}} _requestBody;
@"NSInputStream" _requestBodyStream;
@"NSInputStream" _initialStream;
@"NSFileHandle" _readHandle;
@"NSObject<OS_dispatch_io>" _pipeIO;
Q _numberOfOngoingWrites;
B _openedStreamDuringNeedNewBodyStream;
B _readingRequestBody;
```

## Instance methods

```
-[__NSCFBackgroundDataTask _onqueue_didFinishWithError:];
-[__NSCFBackgroundDataTask _onqueue_willSendRequestForEstablishedConnection:withCompletion:];
-[__NSCFBackgroundDataTask initWithOriginalRequest:ident:taskGroup:];
-[__NSCFBackgroundDataTask dealloc];
-[__NSCFBackgroundDataTask isKindOfClass:];
```
