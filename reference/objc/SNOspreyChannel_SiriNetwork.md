# `SNOspreyChannel`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OspreyChannel`
- 8 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionConfiguration;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 ospreyClientStreamingContext;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 ospreyRequestBuilder;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 ospreyConnectionMetrics;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionMetrics;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lock;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionIdentifier;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 configuration;
```

## Properties

```
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[SNOspreyChannel init];
-[SNOspreyChannel description];
-[SNOspreyChannel initWithURL:configuration:];
-[SNOspreyChannel bidirectionalStreamingRequestWithMethodName:requestBuilder:streamingResponseHandler:completion:];
-[SNOspreyChannel initWithURL:configuration:useCache:];
```
