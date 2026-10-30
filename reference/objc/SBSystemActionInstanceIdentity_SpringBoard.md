# `SBSystemActionInstanceIdentity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `SBSystemActionInstanceIdentifying`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _hostIdentifier;
@"NSString" _configurationIdentifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_hostIdentifier) hostIdentifier;
@property (T@"NSString",R,C,N,V_configurationIdentifier) configurationIdentifier;
```

## Instance methods

```
-[SBSystemActionInstanceIdentity hostIdentifier];
-[SBSystemActionInstanceIdentity appendDescriptionToFormatter:];
-[SBSystemActionInstanceIdentity configurationIdentifier];
-[SBSystemActionInstanceIdentity hash];
-[SBSystemActionInstanceIdentity description];
-[SBSystemActionInstanceIdentity copyWithZone:];
-[SBSystemActionInstanceIdentity isEqual:];
```
