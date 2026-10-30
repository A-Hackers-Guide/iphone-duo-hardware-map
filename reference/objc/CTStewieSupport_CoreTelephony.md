# `CTStewieSupport`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _status;
B _hwSupport;
```

## Properties

```
@property (TB,N,V_status) status;
@property (TB,N,V_hwSupport) hwSupport;
```

## Class methods

```
+[CTStewieSupport supportsSecureCoding];
```

## Instance methods

```
-[CTStewieSupport hwSupport];
-[CTStewieSupport status];
-[CTStewieSupport isEqualToSupport:];
-[CTStewieSupport encodeWithCoder:];
-[CTStewieSupport description];
-[CTStewieSupport initWithCoder:];
-[CTStewieSupport setHwSupport:];
-[CTStewieSupport setStatus:];
-[CTStewieSupport copyWithZone:];
-[CTStewieSupport isEqual:];
```
