# `BKEnrollPearlOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKEnrollOperation`
- 4 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _clientToComplete;
q _enrollmentType;
@"BKIdentity" _augmentedIdentity;
q _periocularGlassesRequirement;
```

## Properties

```
@property (T@"<BKEnrollPearlOperationDelegate>",W,D,N) delegate;
@property (Tq,N,V_enrollmentType) enrollmentType;
@property (TB,N,V_clientToComplete) clientToComplete;
@property (T@"BKIdentity",&,N,V_augmentedIdentity) augmentedIdentity;
@property (Tq,N,V_periocularGlassesRequirement) periocularGlassesRequirement;
```

## Instance methods

```
-[BKEnrollPearlOperation startWithError:];
-[BKEnrollPearlOperation statusMessage:client:];
-[BKEnrollPearlOperation initWithDevice:];
-[BKEnrollPearlOperation completeWithError:];
-[BKEnrollPearlOperation enrollUpdate:client:];
-[BKEnrollPearlOperation resumeWithError:];
-[BKEnrollPearlOperation suspendWithError:];
-[BKEnrollPearlOperation enrollFeedback:client:];
-[BKEnrollPearlOperation augmentedIdentity];
-[BKEnrollPearlOperation clientToComplete];
-[BKEnrollPearlOperation enrollResultInfoWithServerIdentity:details:];
-[BKEnrollPearlOperation enrollmentType];
-[BKEnrollPearlOperation optionsDictionaryWithError:];
-[BKEnrollPearlOperation periocularGlassesRequirement];
-[BKEnrollPearlOperation setAugmentedIdentity:];
-[BKEnrollPearlOperation setClientToComplete:];
-[BKEnrollPearlOperation setEnrollmentType:];
-[BKEnrollPearlOperation setPeriocularGlassesRequirement:];
```
