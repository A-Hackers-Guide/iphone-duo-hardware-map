# `SBTraitsSwitcherLiveOverlayPolicySpecifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractTraitsSwitcherPolicySpecifier`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _primaryElementResolutionPolicy;
@"NSString" _primaryElementParticipantIdentifier;
q _nonPrimaryResolutionPolicy;
```

## Properties

```
@property (Tq,N,V_primaryElementResolutionPolicy) primaryElementResolutionPolicy;
@property (T@"NSString",C,N,V_primaryElementParticipantIdentifier) primaryElementParticipantIdentifier;
@property (Tq,N,V_nonPrimaryResolutionPolicy) nonPrimaryResolutionPolicy;
```

## Instance methods

```
-[SBTraitsSwitcherLiveOverlayPolicySpecifier initWithComponentOrder:arbiter:];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier _specifierDescription];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier _updateAcquiredParticipantsPolicies:context:];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier _updateParticipant:withPolicy:context:];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier nonPrimaryResolutionPolicy];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier primaryElementParticipantIdentifier];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier primaryElementResolutionPolicy];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier setNonPrimaryResolutionPolicy:];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier setPrimaryElementParticipantIdentifier:];
-[SBTraitsSwitcherLiveOverlayPolicySpecifier setPrimaryElementResolutionPolicy:];
```
