# `SNNetworkActivityTracingInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkActivityTracing;
```

## Class methods

```
+[SNNetworkActivityTracingInternal shared];
```

## Instance methods

```
-[SNNetworkActivityTracingInternal init];
-[SNNetworkActivityTracingInternal activateWithLabel:completion:];
-[SNNetworkActivityTracingInternal currentNetworkActivityToken:];
-[SNNetworkActivityTracingInternal startWithLabel:activate:completion:];
-[SNNetworkActivityTracingInternal stopWithLabel:reason:error:completion:];
-[SNNetworkActivityTracingInternal tracingCancelWithCompletion:];
```
