# `_BKSHIDUniqueEventDeferringToken`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDeferringToken`
- 2 instance variables, 0 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSString" _label;
I _uniqueValue;
```

## Class methods

```
+[_BKSHIDUniqueEventDeferringToken supportsSecureCoding];
+[_BKSHIDUniqueEventDeferringToken protobufSchema];
```

## Instance methods

```
-[_BKSHIDUniqueEventDeferringToken _label];
-[_BKSHIDUniqueEventDeferringToken initForProtobufDecoding];
-[_BKSHIDUniqueEventDeferringToken init];
-[_BKSHIDUniqueEventDeferringToken _isUnique];
-[_BKSHIDUniqueEventDeferringToken _initWithLabel:];
-[_BKSHIDUniqueEventDeferringToken encodeWithCoder:];
-[_BKSHIDUniqueEventDeferringToken hash];
-[_BKSHIDUniqueEventDeferringToken description];
-[_BKSHIDUniqueEventDeferringToken initWithCoder:];
-[_BKSHIDUniqueEventDeferringToken appendDescriptionToStream:];
-[_BKSHIDUniqueEventDeferringToken isEqual:];
```
