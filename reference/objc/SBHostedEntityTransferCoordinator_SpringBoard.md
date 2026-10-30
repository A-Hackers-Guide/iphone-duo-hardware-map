# `SBHostedEntityTransferCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSHostedEntityTransferCoordinating`
- 2 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _assertion;
@"NSHashTable" _observers;
```

## Properties

```
@property (TB,R,N,GisEntityLive) entityLive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHostedEntityTransferCoordinator removeObserver:];
-[SBHostedEntityTransferCoordinator init];
-[SBHostedEntityTransferCoordinator addObserver:];
-[SBHostedEntityTransferCoordinator _assertion];
-[SBHostedEntityTransferCoordinator acquireKeepAliveAssertionForReason:];
-[SBHostedEntityTransferCoordinator _notifyPreservationDidEnd];
-[SBHostedEntityTransferCoordinator isEntityLive];
```
