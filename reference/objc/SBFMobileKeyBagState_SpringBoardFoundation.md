# `SBFMobileKeyBagState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`, `NSMutableCopying`
- 2 instance variables, 13 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _state;
B _extended;
```

## Properties

```
@property (Tq,R,N) lockState;
@property (Td,R,N) backOffTime;
@property (TQ,R,N) failedAttemptCount;
@property (TB,R,N) permanentlyBlocked;
@property (TB,R,N) shouldWipe;
@property (TB,R,N) recoveryEnabled;
@property (TB,R,N) recoveryRequired;
@property (TB,R,N) recoveryPossible;
@property (Tq,R,N) escrowCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFMobileKeyBagState shouldWipe];
-[SBFMobileKeyBagState escrowCount];
-[SBFMobileKeyBagState isEffectivelyLocked];
-[SBFMobileKeyBagState backOffTime];
-[SBFMobileKeyBagState recoveryPossible];
-[SBFMobileKeyBagState lockState];
-[SBFMobileKeyBagState recoveryEnabled];
-[SBFMobileKeyBagState publicDescription];
-[SBFMobileKeyBagState mutableCopyWithZone:];
-[SBFMobileKeyBagState succinctDescriptionBuilder];
-[SBFMobileKeyBagState init];
-[SBFMobileKeyBagState descriptionWithMultilinePrefix:];
-[SBFMobileKeyBagState permanentlyBlocked];
-[SBFMobileKeyBagState initWithKeyBagInfo:extended:];
-[SBFMobileKeyBagState succinctDescription];
-[SBFMobileKeyBagState recoveryRequired];
-[SBFMobileKeyBagState hash];
-[SBFMobileKeyBagState description];
-[SBFMobileKeyBagState failedAttemptCount];
-[SBFMobileKeyBagState copyWithZone:];
-[SBFMobileKeyBagState isEqual:];
-[SBFMobileKeyBagState descriptionBuilderWithMultilinePrefix:];
```
