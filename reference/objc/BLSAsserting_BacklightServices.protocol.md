# `BLSAsserting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisAcquired) acquired;
@property (T@"BLSAssertionDescriptor",R,N) descriptor;
@property (T@"BLSAssertionIdentifier",&,N) identifier;
@property (TQ,R,N) acquisitionState;
@property (Td,R,N) activeDuration;
```

## Instance methods

```
-[BLSAsserting descriptor];
-[BLSAsserting identifier];
-[BLSAsserting activeDuration];
-[BLSAsserting setIdentifier:];
-[BLSAsserting isAcquired];
-[BLSAsserting acquisitionState];
```
