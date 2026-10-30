# `SBKeyboardFocusLockReason`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 8 instance variables, 11 properties, 12 instance methods, 23 class methods

## Instance variables

```
Q _creationOrder;
B _avoidOverridingAppFocusOnOtherDisplays;
B _ignoreModalitiesOnSelectionChange;
B _imposesConstraint;
q _strength;
@"NSDate" _timestamp;
@"NSString" _name;
@"NSSet" _blocksFocusRequestsForReasons;
```

## Properties

```
@property (Tq,R,N,V_strength) strength;
@property (TB,R,N,V_avoidOverridingAppFocusOnOtherDisplays) avoidOverridingAppFocusOnOtherDisplays;
@property (TB,R,N,V_ignoreModalitiesOnSelectionChange) ignoreModalitiesOnSelectionChange;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSString",R,C,N,V_name) name;
@property (TB,R,N,V_imposesConstraint) imposesConstraint;
@property (T@"NSSet",R,C,N,V_blocksFocusRequestsForReasons) blocksFocusRequestsForReasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBKeyboardFocusLockReason assistant];
+[SBKeyboardFocusLockReason screenIsDim];
+[SBKeyboardFocusLockReason menuBar];
+[SBKeyboardFocusLockReason accessibility:];
+[SBKeyboardFocusLockReason modalAppLibrary];
+[SBKeyboardFocusLockReason mostRecentReasonInSet:strength:];
+[SBKeyboardFocusLockReason standBy];
+[SBKeyboardFocusLockReason activeTransientOverlay];
+[SBKeyboardFocusLockReason addWidgetSheet];
+[SBKeyboardFocusLockReason appSwitcher];
+[SBKeyboardFocusLockReason commandTab];
+[SBKeyboardFocusLockReason controlCenter];
+[SBKeyboardFocusLockReason coverSheet];
+[SBKeyboardFocusLockReason coverSheetHostingApp];
+[SBKeyboardFocusLockReason floatingDockPresentedFromKeyboard];
+[SBKeyboardFocusLockReason floatingDockPresentedFromTouch];
+[SBKeyboardFocusLockReason loginWindowReason];
+[SBKeyboardFocusLockReason maximumStrengthInSet:];
+[SBKeyboardFocusLockReason modalBannerInLongLook];
+[SBKeyboardFocusLockReason spotlight];
+[SBKeyboardFocusLockReason systemModalAlert];
+[SBKeyboardFocusLockReason transientOverlayOwningKeyboard];
+[SBKeyboardFocusLockReason universalControl];
```

## Instance methods

```
-[SBKeyboardFocusLockReason strength];
-[SBKeyboardFocusLockReason timestamp];
-[SBKeyboardFocusLockReason hash];
-[SBKeyboardFocusLockReason description];
-[SBKeyboardFocusLockReason appendDescriptionToStream:];
-[SBKeyboardFocusLockReason isEqual:];
-[SBKeyboardFocusLockReason name];
-[SBKeyboardFocusLockReason avoidOverridingAppFocusOnOtherDisplays];
-[SBKeyboardFocusLockReason blocksFocusRequestsForReasons];
-[SBKeyboardFocusLockReason ignoreModalitiesOnSelectionChange];
-[SBKeyboardFocusLockReason imposesConstraint];
-[SBKeyboardFocusLockReason isMoreRecentThanReason:];
```
