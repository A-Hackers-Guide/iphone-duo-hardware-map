# `CWFAutoJoinParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
q _trigger;
q _mode;
@"CWFNetworkProfile" _targetNetworkProfile;
@"NSArray" _preferredChannels;
```

## Properties

```
@property (Tq,N,V_trigger) trigger;
@property (Tq,N,V_mode) mode;
@property (T@"CWFNetworkProfile",C,N,V_targetNetworkProfile) targetNetworkProfile;
@property (T@"NSArray",C,N,V_preferredChannels) preferredChannels;
```

## Class methods

```
+[CWFAutoJoinParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFAutoJoinParameters trigger];
-[CWFAutoJoinParameters setPreferredChannels:];
-[CWFAutoJoinParameters setMode:];
-[CWFAutoJoinParameters encodeWithCoder:];
-[CWFAutoJoinParameters mode];
-[CWFAutoJoinParameters hash];
-[CWFAutoJoinParameters description];
-[CWFAutoJoinParameters initWithCoder:];
-[CWFAutoJoinParameters targetNetworkProfile];
-[CWFAutoJoinParameters setTargetNetworkProfile:];
-[CWFAutoJoinParameters copyWithZone:];
-[CWFAutoJoinParameters isEqualToAutoJoinParameters:];
-[CWFAutoJoinParameters preferredChannels];
-[CWFAutoJoinParameters isEqual:];
-[CWFAutoJoinParameters setTrigger:];
```
