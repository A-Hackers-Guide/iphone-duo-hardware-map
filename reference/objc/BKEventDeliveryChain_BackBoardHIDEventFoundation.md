# `BKEventDeliveryChain`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 8 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BKSEventDeferringChainIdentity" _identity;
@"BKEventDeferringEnvironmentGraph" _environmentGraph;
@"BKSHIDEventDispatchingTarget" _dispatchTarget;
@"BKSHIDEventSenderDescriptor" _senderDescriptor;
@"NSArray" _deferringPath;
@"NSSet" _modalities;
@"NSSet" _constraints;
q _generation;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKEventDeliveryChain hash];
-[BKEventDeliveryChain description];
-[BKEventDeliveryChain appendDescriptionToStream:];
-[BKEventDeliveryChain isEqual:];
```
