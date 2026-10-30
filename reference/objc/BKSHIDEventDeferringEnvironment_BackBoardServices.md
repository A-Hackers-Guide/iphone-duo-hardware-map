# `BKSHIDEventDeferringEnvironment`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `NSSecureCoding`, `NSCopying`, `BSXPCCoding`, `BSXPCSecureCoding`
- 1 instance variables, 4 properties, 14 instance methods, 6 class methods

## Instance variables

```
@"NSString" _identifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringEnvironment supportsBSXPCSecureCoding];
+[BKSHIDEventDeferringEnvironment supportsSecureCoding];
+[BKSHIDEventDeferringEnvironment protobufSchema];
+[BKSHIDEventDeferringEnvironment environmentWithIdentifier:];
+[BKSHIDEventDeferringEnvironment keyboardFocusEnvironment];
+[BKSHIDEventDeferringEnvironment systemEnvironment];
```

## Instance methods

```
-[BKSHIDEventDeferringEnvironment initForProtobufDecoding];
-[BKSHIDEventDeferringEnvironment init];
-[BKSHIDEventDeferringEnvironment initWithXPCDictionary:];
-[BKSHIDEventDeferringEnvironment _isSystemEnvironment];
-[BKSHIDEventDeferringEnvironment encodeWithXPCDictionary:];
-[BKSHIDEventDeferringEnvironment encodeWithCoder:];
-[BKSHIDEventDeferringEnvironment hash];
-[BKSHIDEventDeferringEnvironment description];
-[BKSHIDEventDeferringEnvironment initWithCoder:];
-[BKSHIDEventDeferringEnvironment encodeWithBSXPCCoder:];
-[BKSHIDEventDeferringEnvironment initWithBSXPCCoder:];
-[BKSHIDEventDeferringEnvironment copyWithZone:];
-[BKSHIDEventDeferringEnvironment _isKeyboardFocusEnvironment];
-[BKSHIDEventDeferringEnvironment isEqual:];
```
