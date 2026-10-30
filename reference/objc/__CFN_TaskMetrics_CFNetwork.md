# `__CFN_TaskMetrics`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 15 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _resumableUploadSupported;
C _schedulingTier;
B _ignoreNextRedirection;
i _pidForHAR;
@"NSUUID" _UUID;
Q _identifier;
@"NSMutableArray" _transactionMetrics;
d _createTime;
d _firstResumeTime;
d _completeTime;
q _options;
@"NSString" _sourceApplicationBundleIdentifier;
@"__CFN_TransactionMetrics" _currentTransactionMetrics;
@"NSURLSessionTaskTransactionMetrics" _currentStaticTransactionMetrics;
```

## Properties

```
@property (T@"NSMutableArray",R,N) _daemon_transactionMetrics;
@property (T@"__CFN_TransactionMetrics",R) _daemon_currentTransactionMetrics;
```

## Class methods

```
+[__CFN_TaskMetrics supportsSecureCoding];
```

## Instance methods

```
-[__CFN_TaskMetrics _daemon_currentTransactionMetrics];
-[__CFN_TaskMetrics encodeWithCoder:];
-[__CFN_TaskMetrics initWithCoder:];
-[__CFN_TaskMetrics _daemon_transactionMetrics];
```
