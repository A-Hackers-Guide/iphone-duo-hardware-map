# `AVMetricMediaResourceRequestEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _url;
@"NSString" _serverAddress;
@"NSDate" _requestStartTime;
@"NSDate" _requestEndTime;
@"NSDate" _responseStartTime;
@"NSDate" _responseEndTime;
{_NSRange="location"Q"length"Q} _byteRange;
B _readFromCache;
@"AVMetricErrorEvent" _errorEvent;
@"NSURLSessionTaskMetrics" _networkTransactionMetrics;
```

## Properties

```
@property (T@"NSURL",R) url;
@property (T@"NSString",R) serverAddress;
@property (T@"NSDate",R) requestStartTime;
@property (T@"NSDate",R) requestEndTime;
@property (T@"NSDate",R) responseStartTime;
@property (T@"NSDate",R) responseEndTime;
@property (T{_NSRange=QQ},R) byteRange;
@property (TB,R,GwasReadFromCache) readFromCache;
@property (T@"AVMetricErrorEvent",R) errorEvent;
@property (T@"NSURLSessionTaskMetrics",R) networkTransactionMetrics;
```

## Class methods

```
+[AVMetricMediaResourceRequestEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricMediaResourceRequestEvent requestStartTime];
-[AVMetricMediaResourceRequestEvent debugDescription];
-[AVMetricMediaResourceRequestEvent dealloc];
-[AVMetricMediaResourceRequestEvent responseStartTime];
-[AVMetricMediaResourceRequestEvent requestEndTime];
-[AVMetricMediaResourceRequestEvent responseEndTime];
-[AVMetricMediaResourceRequestEvent serverAddress];
-[AVMetricMediaResourceRequestEvent encodeWithCoder:];
-[AVMetricMediaResourceRequestEvent initWithCoder:];
-[AVMetricMediaResourceRequestEvent url];
-[AVMetricMediaResourceRequestEvent byteRange];
-[AVMetricMediaResourceRequestEvent errorEvent];
-[AVMetricMediaResourceRequestEvent initWithDate:mediaTime:sessionID:figMetricEvent:url:serverAddress:requestStartTime:requestEndTime:responseStartTime:responseEndTime:byteRange:readFromCache:errorEvent:networkTransactionMetrics:];
-[AVMetricMediaResourceRequestEvent networkTransactionMetrics];
-[AVMetricMediaResourceRequestEvent wasReadFromCache];
```
