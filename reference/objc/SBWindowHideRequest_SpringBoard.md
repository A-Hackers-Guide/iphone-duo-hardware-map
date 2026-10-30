# `SBWindowHideRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _reason;
{SBWindowLevelRange_struct="start"d"end"d} _windowLevelRange;
```

## Properties

```
@property (T{SBWindowLevelRange_struct=dd},V_windowLevelRange) windowLevelRange;
@property (T@"NSString",C,V_reason) reason;
```

## Class methods

```
+[SBWindowHideRequest hideRequestWithWindowLevelRange:reason:];
```

## Instance methods

```
-[SBWindowHideRequest setReason:];
-[SBWindowHideRequest description];
-[SBWindowHideRequest reason];
-[SBWindowHideRequest setWindowLevelRange:];
-[SBWindowHideRequest windowLevelRange];
```
