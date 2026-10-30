# `NWURLSessionTaskMetrics`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionTaskMetrics`
- Protocols: `NSSecureCoding`
- 1 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_nw_protocol_metadata>" _clientMetadata;
```

## Properties

```
@property (T@"NSArray",R,C,N) transactionMetrics;
@property (T@"NWURLSessionTaskTransactionMetrics",R,N) currentTransactionMetrics;
@property (T@"NSDateInterval",R,C,N) taskInterval;
@property (TQ,R,N) redirectCount;
```

## Class methods

```
+[NWURLSessionTaskMetrics supportsSecureCoding];
```

## Instance methods

```
-[NWURLSessionTaskMetrics redirectCount];
-[NWURLSessionTaskMetrics taskInterval];
-[NWURLSessionTaskMetrics transactionMetrics];
-[NWURLSessionTaskMetrics encodeWithCoder:];
-[NWURLSessionTaskMetrics initWithCoder:];
-[NWURLSessionTaskMetrics currentTransactionMetrics];
```
