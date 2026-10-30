# `CTAutoReconnectionDetails`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _success;
B _skipped;
Q _duration;
```

## Properties

```
@property (TB,V_success) success;
@property (TB,V_skipped) skipped;
@property (TQ,V_duration) duration;
```

## Class methods

```
+[CTAutoReconnectionDetails supportsSecureCoding];
```

## Instance methods

```
-[CTAutoReconnectionDetails setSuccess:];
-[CTAutoReconnectionDetails success];
-[CTAutoReconnectionDetails duration];
-[CTAutoReconnectionDetails encodeWithCoder:];
-[CTAutoReconnectionDetails description];
-[CTAutoReconnectionDetails initWithCoder:];
-[CTAutoReconnectionDetails setDuration:];
-[CTAutoReconnectionDetails isEqual:];
-[CTAutoReconnectionDetails skipped];
-[CTAutoReconnectionDetails initWithSuccess:skipped:duration:];
-[CTAutoReconnectionDetails setSkipped:];
```
