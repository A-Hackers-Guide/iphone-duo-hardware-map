# `ANSignalParityChecker`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
d _timeout;
@"NSObject<OS_dispatch_queue>" _queue;
@? _getTimeIntervalSince1970;
@? _isEqual;
@"NSNumber" _overdueImplementation;
@"ANStackQueue" _eventQueueCL;
@"ANStackQueue" _eventQueueNonCL;
B _failedBeyondRecovery;
@? _onError;
```

## Properties

```
@property (TB,R,N,V_failedBeyondRecovery) failedBeyondRecovery;
@property (T@?,C,N,V_onError) onError;
```

## Instance methods

```
-[ANSignalParityChecker dealloc];
-[ANSignalParityChecker onError];
-[ANSignalParityChecker setOnError:];
-[ANSignalParityChecker checkForTimeout];
-[ANSignalParityChecker failedBeyondRecovery];
-[ANSignalParityChecker initWithIdentifier:timeout:queue:getTimeIntervalSince1970:isEqual:];
-[ANSignalParityChecker receivedSignalFromImplementation:content:];
```
