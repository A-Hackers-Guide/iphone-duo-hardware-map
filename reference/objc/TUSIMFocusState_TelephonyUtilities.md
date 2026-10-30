# `TUSIMFocusState`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCoding`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
? identifier;
? name;
? phNumber;
B focusAllowCalls;
```

## Properties

```
@property (T@"NSString",N,R) identifier;
@property (T@"NSString",N,R) name;
@property (T@"NSString",N,R) phNumber;
@property (TB,N,R,VfocusAllowCalls) focusAllowCalls;
```

## Class methods

```
+[TUSIMFocusState supportsSecureCoding];
```

## Instance methods

```
-[TUSIMFocusState identifier];
-[TUSIMFocusState init];
-[TUSIMFocusState encodeWithCoder:];
-[TUSIMFocusState initWithCoder:];
-[TUSIMFocusState name];
-[TUSIMFocusState focusAllowCalls];
-[TUSIMFocusState initWithIdentifier:name:phNumber:focusAllowCalls:];
-[TUSIMFocusState phNumber];
```
