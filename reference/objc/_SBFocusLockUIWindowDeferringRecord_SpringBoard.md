# `_SBFocusLockUIWindowDeferringRecord`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _references;
@"<BSInvalidatable>" _rule;
@"BKSHIDEventDeferringPredicate" _predicate;
@"BKSHIDEventDeferringTarget" _target;
@"NSString" _reason;
@"SBKeyboardFocusTarget" _keyboardTarget;
```

## Properties

```
@property (T@"BSCompoundAssertion",&,N,V_references) references;
@property (T@"<BSInvalidatable>",&,N,V_rule) rule;
@property (T@"BKSHIDEventDeferringPredicate",&,N,V_predicate) predicate;
@property (T@"BKSHIDEventDeferringTarget",&,N,V_target) target;
@property (T@"NSString",&,N,V_reason) reason;
@property (T@"SBKeyboardFocusTarget",&,N,V_keyboardTarget) keyboardTarget;
```

## Instance methods

```
-[_SBFocusLockUIWindowDeferringRecord rule];
-[_SBFocusLockUIWindowDeferringRecord setReason:];
-[_SBFocusLockUIWindowDeferringRecord setPredicate:];
-[_SBFocusLockUIWindowDeferringRecord setTarget:];
-[_SBFocusLockUIWindowDeferringRecord predicate];
-[_SBFocusLockUIWindowDeferringRecord reason];
-[_SBFocusLockUIWindowDeferringRecord target];
-[_SBFocusLockUIWindowDeferringRecord setRule:];
-[_SBFocusLockUIWindowDeferringRecord references];
-[_SBFocusLockUIWindowDeferringRecord setReferences:];
-[_SBFocusLockUIWindowDeferringRecord keyboardTarget];
-[_SBFocusLockUIWindowDeferringRecord setKeyboardTarget:];
```
