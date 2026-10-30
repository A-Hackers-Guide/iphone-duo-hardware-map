# `BKSHIDEventDeferringToken`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSProtobufSerializable`, `BSDescriptionStreaming`, `NSCopying`
- 0 instance variables, 5 properties, 18 instance methods, 9 class methods

## Properties

```
@property (T@"NSString",R,C,N) pithyDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringToken supportsSecureCoding];
+[BKSHIDEventDeferringToken protobufSchema];
+[BKSHIDEventDeferringToken new];
+[BKSHIDEventDeferringToken tokenForString:];
+[BKSHIDEventDeferringToken tokenForIdentifierOfCAContext:];
+[BKSHIDEventDeferringToken uniqueTokenWithLabel:];
+[BKSHIDEventDeferringToken tokenForIdentifierOfCAContext:andCGSWindow:];
+[BKSHIDEventDeferringToken tokenForIdentifierOfCGSConnection:];
+[BKSHIDEventDeferringToken tokenForIdentifierOfCGSWindow:];
```

## Instance methods

```
-[BKSHIDEventDeferringToken _label];
-[BKSHIDEventDeferringToken _isIdentifierOfCAContext];
-[BKSHIDEventDeferringToken init];
-[BKSHIDEventDeferringToken _isUnique];
-[BKSHIDEventDeferringToken _identifierOfCGSWindow];
-[BKSHIDEventDeferringToken _isIdentifierOfCAContextAndCGSWindow];
-[BKSHIDEventDeferringToken _init];
-[BKSHIDEventDeferringToken _identifierOfCGSConnection];
-[BKSHIDEventDeferringToken encodeWithCoder:];
-[BKSHIDEventDeferringToken pithyDescription];
-[BKSHIDEventDeferringToken initWithCoder:];
-[BKSHIDEventDeferringToken appendDescriptionToStream:];
-[BKSHIDEventDeferringToken _isString];
-[BKSHIDEventDeferringToken _isIdentifierOfCGSConnection];
-[BKSHIDEventDeferringToken copyWithZone:];
-[BKSHIDEventDeferringToken _string];
-[BKSHIDEventDeferringToken _identifierOfCAContext];
-[BKSHIDEventDeferringToken _isIdentifierOfCGSWindow];
```
