# `NSURLConnectionInternal`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLConnectionRequired`, `NSURLAuthenticationChallengeSender`
- 8 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSURLConnection" _connection;
@"NSOperationQueue" _delegateQueue;
@"NSURL" _url;
@"NSURLRequest" _originalRequest;
@"NSURLRequest" _currentRequest;
@ _delegate;
@"NSDictionary" _connectionProperties;
B _connectionActive;
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
-[NSURLConnectionInternal _invalidate];
-[NSURLConnectionInternal dealloc];
-[NSURLConnectionInternal continueWithoutCredentialForAuthenticationChallenge:];
-[NSURLConnectionInternal initWithInfo:];
-[NSURLConnectionInternal useCredential:forAuthenticationChallenge:];
-[NSURLConnectionInternal cancelAuthenticationChallenge:];
-[NSURLConnectionInternal _timingData];
-[NSURLConnectionInternal performDefaultHandlingForAuthenticationChallenge:];
-[NSURLConnectionInternal rejectProtectionSpaceAndContinueWithChallenge:];
-[NSURLConnectionInternal _setDelegateQueue:];
-[NSURLConnectionInternal invokeForDelegate:];
```
