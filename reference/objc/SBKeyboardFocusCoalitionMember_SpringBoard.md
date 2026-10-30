# `SBKeyboardFocusCoalitionMember`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `BSInvalidatable`
- 7 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBKeyboardFocusCoalition" _coalition;
@"SBKeyboardFocusCoalitionMemberPreferences" _preferences;
B _invalidated;
B _hasFocus;
@"SBWindowScene" _sbWindowScene;
@"NSString" _uniqueIdentifier;
@"<SBKeyboardFocusCoalitionMemberDelegate>" _delegate;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_sbWindowScene) sbWindowScene;
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"<SBKeyboardFocusCoalitionMemberDelegate>",W,N,V_delegate) delegate;
@property (T@"SBKeyboardFocusCoalitionMemberPreferences",R,N) preferences;
@property (TB,N,V_hasFocus) hasFocus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBKeyboardFocusCoalitionMember debugDescription];
-[SBKeyboardFocusCoalitionMember preferences];
-[SBKeyboardFocusCoalitionMember dealloc];
-[SBKeyboardFocusCoalitionMember setUniqueIdentifier:];
-[SBKeyboardFocusCoalitionMember uniqueIdentifier];
-[SBKeyboardFocusCoalitionMember succinctDescription];
-[SBKeyboardFocusCoalitionMember invalidate];
-[SBKeyboardFocusCoalitionMember setDelegate:];
-[SBKeyboardFocusCoalitionMember delegate];
-[SBKeyboardFocusCoalitionMember description];
-[SBKeyboardFocusCoalitionMember hasFocus];
-[SBKeyboardFocusCoalitionMember appendDescriptionToStream:];
-[SBKeyboardFocusCoalitionMember copyWithZone:];
-[SBKeyboardFocusCoalitionMember setHasFocus:];
-[SBKeyboardFocusCoalitionMember focusPolicyDidChange];
-[SBKeyboardFocusCoalitionMember initWithUniqueIdentifier:windowScene:delegate:coalition:];
-[SBKeyboardFocusCoalitionMember requestArbitration:];
-[SBKeyboardFocusCoalitionMember sbWindowScene];
-[SBKeyboardFocusCoalitionMember setSbWindowScene:];
-[SBKeyboardFocusCoalitionMember updateCoalitionPreferencesWithReason:];
```
