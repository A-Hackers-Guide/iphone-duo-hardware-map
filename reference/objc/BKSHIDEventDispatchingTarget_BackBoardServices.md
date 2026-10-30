# `BKSHIDEventDispatchingTarget`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreamable`, `NSCopying`
- 4 instance variables, 8 properties, 13 instance methods, 11 class methods

## Instance variables

```
@"BKSHIDEventDeferringEnvironment" _environment;
@"BKSHIDEventDeferringToken" _deferringToken;
@"BKSHIDEventDeferringSelectionPathIdentifier" _selectionPathIdentifier;
i _pid;
```

## Properties

```
@property (Ti,R,N,V_pid) pid;
@property (T@"BKSHIDEventDeferringEnvironment",R,C,N,V_environment) deferringEnvironment;
@property (T@"BKSHIDEventDeferringToken",R,C,N,V_deferringToken) deferringToken;
@property (T@"BKSHIDEventDeferringSelectionPathIdentifier",R,C,N,V_selectionPathIdentifier) selectionPathIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDispatchingTarget supportsSecureCoding];
+[BKSHIDEventDispatchingTarget keyboardFocusTarget];
+[BKSHIDEventDispatchingTarget systemTarget];
+[BKSHIDEventDispatchingTarget systemTargetWithDeferringToken:];
+[BKSHIDEventDispatchingTarget focusTargetForPID:];
+[BKSHIDEventDispatchingTarget keyboardFocusTargetWithDeferringToken:];
+[BKSHIDEventDispatchingTarget targetForDeferringEnvironment:];
+[BKSHIDEventDispatchingTarget targetForDeferringEnvironment:deferringToken:];
+[BKSHIDEventDispatchingTarget targetForDeferringEnvironment:selectionPath:];
+[BKSHIDEventDispatchingTarget targetForPID:environment:];
+[BKSHIDEventDispatchingTarget targetForPID:environment:selectionPath:];
```

## Instance methods

```
-[BKSHIDEventDispatchingTarget selectionPathIdentifier];
-[BKSHIDEventDispatchingTarget deferringEnvironment];
-[BKSHIDEventDispatchingTarget deferringToken];
-[BKSHIDEventDispatchingTarget init];
-[BKSHIDEventDispatchingTarget appendDescriptionToFormatter:];
-[BKSHIDEventDispatchingTarget _initWithEnvironment:token:selectionPath:pid:];
-[BKSHIDEventDispatchingTarget pid];
-[BKSHIDEventDispatchingTarget encodeWithCoder:];
-[BKSHIDEventDispatchingTarget hash];
-[BKSHIDEventDispatchingTarget description];
-[BKSHIDEventDispatchingTarget initWithCoder:];
-[BKSHIDEventDispatchingTarget copyWithZone:];
-[BKSHIDEventDispatchingTarget isEqual:];
```
