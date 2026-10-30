# `SBTraitsSwitcherPolicySpecifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractTraitsSwitcherPolicySpecifier`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _resolutionPolicy;
@"NSString" _primaryElementParticipantIdentifier;
```

## Properties

```
@property (Tq,N,V_resolutionPolicy) resolutionPolicy;
@property (T@"NSString",C,N,V_primaryElementParticipantIdentifier) primaryElementParticipantIdentifier;
```

## Instance methods

```
-[SBTraitsSwitcherPolicySpecifier resolutionPolicy];
-[SBTraitsSwitcherPolicySpecifier initWithComponentOrder:arbiter:];
-[SBTraitsSwitcherPolicySpecifier _specifierDescription];
-[SBTraitsSwitcherPolicySpecifier _updateAcquiredParticipantsPolicies:context:];
-[SBTraitsSwitcherPolicySpecifier primaryElementParticipantIdentifier];
-[SBTraitsSwitcherPolicySpecifier setPrimaryElementParticipantIdentifier:];
-[SBTraitsSwitcherPolicySpecifier setResolutionPolicy:];
```
