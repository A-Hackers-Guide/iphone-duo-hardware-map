# `SBShutdownContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reason;
B _fromUserPowerDown;
```

## Properties

```
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TB,N,V_fromUserPowerDown) fromUserPowerDown;
```

## Instance methods

```
-[SBShutdownContext initWithReason:];
-[SBShutdownContext description];
-[SBShutdownContext reason];
-[SBShutdownContext copyWithZone:];
-[SBShutdownContext isEqual:];
-[SBShutdownContext fromUserPowerDown];
-[SBShutdownContext setFromUserPowerDown:];
```
