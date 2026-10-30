# `HIDUserDevice`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDUserDevice=} _device;
@? _getReportHandler;
@? _setReportHandler;
I _service;
@? _cancelHandler;
```

## Properties

```
@property (TI,R) service;
```

## Instance methods

```
-[HIDUserDevice propertyForKey:];
-[HIDUserDevice setProperty:forKey:];
-[HIDUserDevice initWithProperties:];
-[HIDUserDevice dealloc];
-[HIDUserDevice setDispatchQueue:];
-[HIDUserDevice setCancelHandler:];
-[HIDUserDevice service];
-[HIDUserDevice activate];
-[HIDUserDevice description];
-[HIDUserDevice cancel];
-[HIDUserDevice handleReport:error:];
-[HIDUserDevice handleReport:withTimestamp:error:];
-[HIDUserDevice setSetReportHandler:];
-[HIDUserDevice setGetReportHandler:];
```
