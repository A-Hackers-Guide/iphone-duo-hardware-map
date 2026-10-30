# `SBRebootContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reason;
B _isDark;
B _fromOTASoftwareUpdate;
```

## Properties

```
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TB,N,GisDark,V_isDark) dark;
```

## Instance methods

```
-[SBRebootContext initWithReason:];
-[SBRebootContext description];
-[SBRebootContext reason];
-[SBRebootContext copyWithZone:];
-[SBRebootContext isEqual:];
-[SBRebootContext isDark];
-[SBRebootContext setDark:];
```
