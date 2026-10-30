# `NSURLSessionTaskMetrics`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 5 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"__CFN_TaskMetrics" __metrics;
```

## Properties

```
@property (T@"__CFN_TaskMetrics",R,N) _cfnMetricsDaemon;
@property (T@"NSURLSessionTaskTransactionMetrics",R,N) currentTransactionMetrics;
@property (T@"NSArray",R,C) transactionMetrics;
@property (T@"NSDateInterval",R,C) taskInterval;
@property (TQ,R) redirectCount;
```

## Class methods

```
+[NSURLSessionTaskMetrics supportsSecureCoding];
+[NSURLSessionTaskMetrics new];
```

## Instance methods

```
-[NSURLSessionTaskMetrics redirectCount];
-[NSURLSessionTaskMetrics init];
-[NSURLSessionTaskMetrics taskInterval];
-[NSURLSessionTaskMetrics transactionMetrics];
-[NSURLSessionTaskMetrics encodeWithCoder:];
-[NSURLSessionTaskMetrics description];
-[NSURLSessionTaskMetrics initWithCoder:];
-[NSURLSessionTaskMetrics currentTransactionMetrics];
-[NSURLSessionTaskMetrics _cfnMetricsDaemon];
```
