# `FigHTTPRequestSessionDataDelegate`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLSessionDataDelegate`
- 3 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _taskToFigHTTPRequest;
^{OpaqueFigReentrantMutex=} _taskToFigHTTPRequestMutex;
C _doesIgnoreDidReceiveResponseDisposition;
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
-[FigHTTPRequestSessionDataDelegate URLSession:dataTask:didReceiveData:];
-[FigHTTPRequestSessionDataDelegate URLSession:didReceiveChallenge:completionHandler:];
-[FigHTTPRequestSessionDataDelegate initWithResponseDispositionOption:];
-[FigHTTPRequestSessionDataDelegate URLSession:task:didFinishCollectingMetrics:];
-[FigHTTPRequestSessionDataDelegate URLSession:task:didReceiveChallenge:completionHandler:];
-[FigHTTPRequestSessionDataDelegate init];
-[FigHTTPRequestSessionDataDelegate URLSession:task:didCompleteWithError:];
-[FigHTTPRequestSessionDataDelegate dealloc];
-[FigHTTPRequestSessionDataDelegate URLSession:dataTask:didReceiveResponse:completionHandler:];
-[FigHTTPRequestSessionDataDelegate adoptVoucherFromRetainProxy:];
-[FigHTTPRequestSessionDataDelegate URLSession:dataTask:willCacheResponse:completionHandler:];
-[FigHTTPRequestSessionDataDelegate restoreVoucher:];
-[FigHTTPRequestSessionDataDelegate _copyAndLockRequestForTask:];
-[FigHTTPRequestSessionDataDelegate _deregisterFigHTTPRequestForDataTask:];
-[FigHTTPRequestSessionDataDelegate _registerFigHTTPRequest:forDataTask:];
```
