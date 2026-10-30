# `FigPWDKeyExchangeSenderServerHelperProd`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigPWDKeyExchangeSenderServerHelper`, `NSURLSessionDelegate`, `AMSURLProtocolDelegate`
- 6 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"AMSURLSession" _urlSession;
@"AMSBag" _pwdBag;
@"AMSURLRequestEncoder" _requestEncoder;
@"NSOperationQueue" _opQueue;
@"NSURL" _endpointURL;
@"NSURL" _certURL;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigPWDKeyExchangeSenderServerHelperProd InitializeAMS];
```

## Instance methods

```
-[FigPWDKeyExchangeSenderServerHelperProd URLSession:didReceiveChallenge:completionHandler:];
-[FigPWDKeyExchangeSenderServerHelperProd init];
-[FigPWDKeyExchangeSenderServerHelperProd dealloc];
-[FigPWDKeyExchangeSenderServerHelperProd AMSURLSession:task:shouldFailWithServerError:];
-[FigPWDKeyExchangeSenderServerHelperProd requestCertDataFromServer:];
-[FigPWDKeyExchangeSenderServerHelperProd requestCertURL];
-[FigPWDKeyExchangeSenderServerHelperProd requestEndpointURL];
-[FigPWDKeyExchangeSenderServerHelperProd requestKeyDataFromServer:completionHandler:];
```
