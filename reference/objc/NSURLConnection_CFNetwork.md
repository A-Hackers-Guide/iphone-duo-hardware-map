# `NSURLConnection`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLAuthenticationChallengeSender`
- 1 instance variables, 6 properties, 25 instance methods, 13 class methods

## Instance variables

```
@"NSURLConnectionInternal" _internal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSURLRequest",R,C) originalRequest;
@property (T@"NSURLRequest",R,C) currentRequest;
```

## Class methods

```
+[NSURLConnection canHandleRequest:];
+[NSURLConnection sendSynchronousRequest:returningResponse:error:];
+[NSURLConnection resourceLoaderRunLoop];
+[NSURLConnection connectionWithRequest:delegate:];
+[NSURLConnection _collectTimingDataWithOptions:];
+[NSURLConnection _collectsTimingData];
+[NSURLConnection _setCollectsTimingData:];
+[NSURLConnection _setLoaderThreadPriority:];
+[NSURLConnection _setMIMETypesWithNoSizeLimit:];
+[NSURLConnection _setSweeperInterval:];
+[NSURLConnection _sweeperInterval];
+[NSURLConnection _timingDataOptions];
+[NSURLConnection sendAsynchronousRequest:queue:completionHandler:];
```

## Instance methods

```
-[NSURLConnection currentRequest];
-[NSURLConnection dealloc];
-[NSURLConnection continueWithoutCredentialForAuthenticationChallenge:];
-[NSURLConnection originalRequest];
-[NSURLConnection start];
-[NSURLConnection download];
-[NSURLConnection useCredential:forAuthenticationChallenge:];
-[NSURLConnection setDelegateQueue:];
-[NSURLConnection cancelAuthenticationChallenge:];
-[NSURLConnection scheduleInRunLoop:forMode:];
-[NSURLConnection description];
-[NSURLConnection cancel];
-[NSURLConnection _timingData];
-[NSURLConnection performDefaultHandlingForAuthenticationChallenge:];
-[NSURLConnection rejectProtectionSpaceAndContinueWithChallenge:];
-[NSURLConnection defersCallbacks];
-[NSURLConnection setDefersCallbacks:];
-[NSURLConnection _suspendLoading];
-[NSURLConnection _cfInternal];
-[NSURLConnection _initWithRequest:delegate:usesCache:maxContentLength:startImmediately:connectionProperties:];
-[NSURLConnection _resumeLoading];
-[NSURLConnection connectionProperties];
-[NSURLConnection initWithRequest:delegate:];
-[NSURLConnection initWithRequest:delegate:startImmediately:];
-[NSURLConnection unscheduleFromRunLoop:forMode:];
```
