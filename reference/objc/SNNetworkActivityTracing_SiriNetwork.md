# `SNNetworkActivityTracing`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"SNNetworkActivityTracingInternal" _underlyingNetworkActivityTracingInternal;
```

## Properties

```
@property (T@"SNNetworkActivityTracingInternal",&,N,V_underlyingNetworkActivityTracingInternal) underlyingNetworkActivityTracingInternal;
```

## Class methods

```
+[SNNetworkActivityTracing sharedInstance];
```

## Instance methods

```
-[SNNetworkActivityTracing _init];
-[SNNetworkActivityTracing currentNetworkActivityTokenWithCompletion:];
-[SNNetworkActivityTracing networkActivityActivate:completion:];
-[SNNetworkActivityTracing networkActivityStart:activate:completion:];
-[SNNetworkActivityTracing networkActivityStop:withReason:andError:completion:];
-[SNNetworkActivityTracing networkActivityTracingCancel:];
-[SNNetworkActivityTracing setUnderlyingNetworkActivityTracingInternal:];
-[SNNetworkActivityTracing underlyingNetworkActivityTracingInternal];
```
