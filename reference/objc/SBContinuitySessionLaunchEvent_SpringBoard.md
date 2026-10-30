# `SBContinuitySessionLaunchEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _type;
@"NSData" _payload;
@"NSUUID" _identifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_type) type;
@property (T@"NSData",R,N,V_payload) payload;
@property (T@"NSUUID",R,N,V_identifier) identifier;
```

## Instance methods

```
-[SBContinuitySessionLaunchEvent identifier];
-[SBContinuitySessionLaunchEvent payload];
-[SBContinuitySessionLaunchEvent type];
-[SBContinuitySessionLaunchEvent description];
-[SBContinuitySessionLaunchEvent initWithType:payload:];
```
