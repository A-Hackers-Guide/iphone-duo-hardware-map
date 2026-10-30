# `AVAssetCustomURLRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
Q _requestID;
^{__CFDictionary=} _customURLRequest;
^{__CFDictionary=} _customURLResponse;
@"NSURLSessionTaskMetrics" _metrics;
```

## Properties

```
@property (TQ,R,N,V_requestID) requestID;
@property (T@"NSURLSessionTaskMetrics",&,N,V_metrics) metrics;
```

## Class methods

```
+[AVAssetCustomURLRequest requestWithRequest:id:];
```

## Instance methods

```
-[AVAssetCustomURLRequest setMetrics:];
-[AVAssetCustomURLRequest requestID];
-[AVAssetCustomURLRequest init];
-[AVAssetCustomURLRequest dealloc];
-[AVAssetCustomURLRequest metrics];
-[AVAssetCustomURLRequest customURLRequest];
-[AVAssetCustomURLRequest customURLResponse];
-[AVAssetCustomURLRequest initWithRequest:id:];
-[AVAssetCustomURLRequest setCustomURLRequest:];
-[AVAssetCustomURLRequest setCustomURLResponse:];
```
