# `CTStewieMessageAck`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _success;
@"NSError" _error;
q _transportType;
```

## Properties

```
@property (TB,N,V_success) success;
@property (T@"NSError",&,N,V_error) error;
@property (Tq,N,V_transportType) transportType;
```

## Class methods

```
+[CTStewieMessageAck supportsSecureCoding];
```

## Instance methods

```
-[CTStewieMessageAck setError:];
-[CTStewieMessageAck setSuccess:];
-[CTStewieMessageAck success];
-[CTStewieMessageAck setTransportType:];
-[CTStewieMessageAck init];
-[CTStewieMessageAck initWithError:];
-[CTStewieMessageAck transportType];
-[CTStewieMessageAck error];
-[CTStewieMessageAck encodeWithCoder:];
-[CTStewieMessageAck description];
-[CTStewieMessageAck initWithCoder:];
-[CTStewieMessageAck copyWithZone:];
-[CTStewieMessageAck isEqual:];
-[CTStewieMessageAck isEqualToMessageAck:];
```
