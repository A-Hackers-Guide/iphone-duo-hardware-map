# `CTCallForwardingValue`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _enabled;
i _reason;
i _clss;
@"NSString" _saveNumber;
@"NSNumber" _noReplyTime;
```

## Properties

```
@property (Ti,N,V_reason) reason;
@property (Ti,N,V_clss) clss;
@property (TB,N,V_enabled) enabled;
@property (T@"NSString",&,N,V_saveNumber) saveNumber;
@property (T@"NSNumber",&,N,V_noReplyTime) noReplyTime;
```

## Class methods

```
+[CTCallForwardingValue supportsSecureCoding];
```

## Instance methods

```
-[CTCallForwardingValue enabled];
-[CTCallForwardingValue setReason:];
-[CTCallForwardingValue setEnabled:];
-[CTCallForwardingValue encodeWithCoder:];
-[CTCallForwardingValue description];
-[CTCallForwardingValue initWithCoder:];
-[CTCallForwardingValue reason];
-[CTCallForwardingValue copyWithZone:];
-[CTCallForwardingValue setNoReplyTime:];
-[CTCallForwardingValue clss];
-[CTCallForwardingValue noReplyTime];
-[CTCallForwardingValue saveNumber];
-[CTCallForwardingValue setClss:];
-[CTCallForwardingValue setSaveNumber:];
```
