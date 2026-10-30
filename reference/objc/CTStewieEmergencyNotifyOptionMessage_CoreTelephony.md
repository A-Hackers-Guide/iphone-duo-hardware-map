# `CTStewieEmergencyNotifyOptionMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageOutgoing`
- 1 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _notifyOption;
```

## Properties

```
@property (Tq,N,V_notifyOption) notifyOption;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieEmergencyNotifyOptionMessage supportsSecureCoding];
```

## Instance methods

```
-[CTStewieEmergencyNotifyOptionMessage encodeWithCoder:];
-[CTStewieEmergencyNotifyOptionMessage description];
-[CTStewieEmergencyNotifyOptionMessage initWithCoder:];
-[CTStewieEmergencyNotifyOptionMessage copyWithZone:];
-[CTStewieEmergencyNotifyOptionMessage isEqual:];
-[CTStewieEmergencyNotifyOptionMessage initWithNotifyOption:error:];
-[CTStewieEmergencyNotifyOptionMessage isEqualToEmergencyUpdateNotifyOptionMessage:];
-[CTStewieEmergencyNotifyOptionMessage notifyOption];
-[CTStewieEmergencyNotifyOptionMessage setNotifyOption:];
```
