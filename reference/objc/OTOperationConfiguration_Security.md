# `OTOperationConfiguration`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _discretionaryNetwork;
B _useCachedAccountStatus;
Q _timeoutWaitForCKAccount;
q _qualityOfService;
```

## Properties

```
@property (TQ,N,V_timeoutWaitForCKAccount) timeoutWaitForCKAccount;
@property (Tq,N,V_qualityOfService) qualityOfService;
@property (TB,N,V_discretionaryNetwork) discretionaryNetwork;
@property (TB,N,V_useCachedAccountStatus) useCachedAccountStatus;
```

## Class methods

```
+[OTOperationConfiguration supportsSecureCoding];
```

## Instance methods

```
-[OTOperationConfiguration setTimeoutWaitForCKAccount:];
-[OTOperationConfiguration init];
-[OTOperationConfiguration setUseCachedAccountStatus:];
-[OTOperationConfiguration timeoutWaitForCKAccount];
-[OTOperationConfiguration setQualityOfService:];
-[OTOperationConfiguration discretionaryNetwork];
-[OTOperationConfiguration qualityOfService];
-[OTOperationConfiguration useCachedAccountStatus];
-[OTOperationConfiguration encodeWithCoder:];
-[OTOperationConfiguration initWithCoder:];
-[OTOperationConfiguration setDiscretionaryNetwork:];
```
