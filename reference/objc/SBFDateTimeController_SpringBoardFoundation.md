# `SBFDateTimeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _overrideDate;
@"NSHashTable" _observers;
d _overrideDateOffset;
@"NSDate" _overrideDateWithAutoupdatingSeconds;
```

## Properties

```
@property (T@"NSDate",R,C,N) currentDate;
@property (T@"NSDate",C,N,V_overrideDate) overrideDate;
@property (Td,N,V_overrideDateOffset) overrideDateOffset;
@property (T@"NSDate",C,N,V_overrideDateWithAutoupdatingSeconds) overrideDateWithAutoupdatingSeconds;
@property (TB,R,N) hasDateOverride;
```

## Class methods

```
+[SBFDateTimeController sharedInstance];
```

## Instance methods

```
-[SBFDateTimeController overrideDate];
-[SBFDateTimeController currentDate];
-[SBFDateTimeController removeObserver:];
-[SBFDateTimeController addObserver:];
-[SBFDateTimeController setOverrideDateOffset:];
-[SBFDateTimeController setOverrideDate:];
-[SBFDateTimeController overrideDateOffset];
-[SBFDateTimeController hasDateOverride];
-[SBFDateTimeController overrideDateWithAutoupdatingSeconds];
-[SBFDateTimeController setOverrideDateWithAutoupdatingSeconds:];
```
