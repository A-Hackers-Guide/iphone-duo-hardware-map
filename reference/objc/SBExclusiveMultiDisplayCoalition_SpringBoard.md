# `SBExclusiveMultiDisplayCoalition`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBKeyboardFocusCoalition`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBKeyboardFocusCoalitionMember" _embeddedMember;
@"SBKeyboardFocusCoalitionMember" _externalMember;
@"SBKeyboardFocusCoalitionMember" _enforcedMember;
@"SBKeyboardFocusCoalitionMemberPreferences" _enforcedPreferences;
```

## Properties

```
@property (T@"SBKeyboardFocusCoalitionMember",R,N,V_embeddedMember) embeddedMember;
@property (T@"SBKeyboardFocusCoalitionMember",R,N,V_externalMember) externalMember;
@property (T@"SBKeyboardFocusCoalitionMember",R,N) initiallyFocusedMember;
```

## Instance methods

```
-[SBExclusiveMultiDisplayCoalition invalidate];
-[SBExclusiveMultiDisplayCoalition _arbitrateWithRequestingMember:reason:];
-[SBExclusiveMultiDisplayCoalition _performInitialArbitrationWithReason:];
-[SBExclusiveMultiDisplayCoalition _selectMemberPolicy:];
-[SBExclusiveMultiDisplayCoalition addedMember:];
-[SBExclusiveMultiDisplayCoalition embeddedMember];
-[SBExclusiveMultiDisplayCoalition externalMember];
-[SBExclusiveMultiDisplayCoalition initiallyFocusedMember];
-[SBExclusiveMultiDisplayCoalition memberRequestsArbitration:forReason:];
-[SBExclusiveMultiDisplayCoalition setNeedsArbitrationForReason:];
-[SBExclusiveMultiDisplayCoalition updatePolicyForArbitrationRequestFromMember:reason:];
```
