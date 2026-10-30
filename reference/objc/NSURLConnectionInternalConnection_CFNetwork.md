# `NSURLConnectionInternalConnection`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLConnectionInternal`
- Protocols: `NSURLConnectionRequired`
- 8 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _cfConnLock;
^{_CFURLConnection=} _cfConn;
^{_CFURLAuthChallenge=} _currCFChallenge;
@"NSURLAuthenticationChallenge" _currNSChallenge;
^{__CFString=} _fileName;
B _shouldSkipCancelOnRelease;
q _totalBytes;
q _expectedTotalBytes;
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
-[NSURLConnectionInternalConnection _invalidate];
-[NSURLConnectionInternalConnection dealloc];
-[NSURLConnectionInternalConnection continueWithoutCredentialForAuthenticationChallenge:];
-[NSURLConnectionInternalConnection start];
-[NSURLConnectionInternalConnection initWithInfo:];
-[NSURLConnectionInternalConnection useCredential:forAuthenticationChallenge:];
-[NSURLConnectionInternalConnection cancelAuthenticationChallenge:];
-[NSURLConnectionInternalConnection scheduleInRunLoop:forMode:];
-[NSURLConnectionInternalConnection cancel];
-[NSURLConnectionInternalConnection _timingData];
-[NSURLConnectionInternalConnection performDefaultHandlingForAuthenticationChallenge:];
-[NSURLConnectionInternalConnection rejectProtectionSpaceAndContinueWithChallenge:];
-[NSURLConnectionInternalConnection _suspendLoading];
-[NSURLConnectionInternalConnection _resumeLoading];
-[NSURLConnectionInternalConnection _setDelegateQueue:];
-[NSURLConnectionInternalConnection _setShouldSkipCancelOnRelease:];
-[NSURLConnectionInternalConnection invokeForDelegate:];
-[NSURLConnectionInternalConnection unscheduleFromRunLoop:forMode:];
```
