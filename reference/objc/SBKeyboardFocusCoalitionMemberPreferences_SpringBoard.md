# `SBKeyboardFocusCoalitionMemberPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 2 instance variables, 6 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"SBKeyboardFocusPolicy" _policy;
@"NSSet" _lockReasons;
```

## Properties

```
@property (T@"SBKeyboardFocusPolicy",R,N) policy;
@property (T@"NSSet",R,N) lockReasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBKeyboardFocusCoalitionMemberPreferences build:];
+[SBKeyboardFocusCoalitionMemberPreferences new];
+[SBKeyboardFocusCoalitionMemberPreferences preferencesWithPolicy:lockReasons:];
```

## Instance methods

```
-[SBKeyboardFocusCoalitionMemberPreferences mutableCopyWithZone:];
-[SBKeyboardFocusCoalitionMemberPreferences init];
-[SBKeyboardFocusCoalitionMemberPreferences _init];
-[SBKeyboardFocusCoalitionMemberPreferences hash];
-[SBKeyboardFocusCoalitionMemberPreferences lockReasons];
-[SBKeyboardFocusCoalitionMemberPreferences description];
-[SBKeyboardFocusCoalitionMemberPreferences appendDescriptionToStream:];
-[SBKeyboardFocusCoalitionMemberPreferences copyWithZone:];
-[SBKeyboardFocusCoalitionMemberPreferences isEqual:];
-[SBKeyboardFocusCoalitionMemberPreferences policy];
-[SBKeyboardFocusCoalitionMemberPreferences _initWithCopyOf:];
-[SBKeyboardFocusCoalitionMemberPreferences focusLockReasonStrength];
```
