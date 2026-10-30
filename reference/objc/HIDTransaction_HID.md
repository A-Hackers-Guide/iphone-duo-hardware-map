# `HIDTransaction`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDTransaction=} _transaction;
```

## Properties

```
@property (Tq) direction;
```

## Instance methods

```
-[HIDTransaction initWithDevice:];
-[HIDTransaction dealloc];
-[HIDTransaction setDirection:];
-[HIDTransaction direction];
-[HIDTransaction description];
-[HIDTransaction commitElements:error:];
-[HIDTransaction commitElements:error:timeout:callback:];
```
