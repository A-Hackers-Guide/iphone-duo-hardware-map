# `URLSessionDelegate`

- Image: [`/usr/lib/libTelephonyUtilDynamic.dylib`](../userland/usr__lib__libTelephonyUtilDynamic.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLSessionTaskDelegate`, `NSURLSessionDataDelegate`
- 1 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
{map<unsigned long, std::shared_ptr<SessionTaskContext>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<SessionTaskContext>>>>="__tree_"{__tree<std::__value_type<unsigned long, std::shared_ptr<SessionTaskContext>>, std::__map_value_compare<unsigned long, std::pair<const unsigned long, std::shared_ptr<SessionTaskContext>>, std::less<unsigned long>>, std::allocator<std::pair<const unsigned long, std::shared_ptr<SessionTaskContext>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} fTaskHandlers;
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
-[URLSessionDelegate URLSession:dataTask:didReceiveData:];
-[URLSessionDelegate URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:];
-[URLSessionDelegate URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:];
-[URLSessionDelegate URLSession:task:didReceiveChallenge:completionHandler:];
-[URLSessionDelegate URLSession:task:didCompleteWithError:];
-[URLSessionDelegate dealloc];
-[URLSessionDelegate URLSession:dataTask:didReceiveResponse:completionHandler:];
-[URLSessionDelegate addCallbackHandler:for:];
-[URLSessionDelegate getContext:];
-[URLSessionDelegate removeCallbackFor:];
```
