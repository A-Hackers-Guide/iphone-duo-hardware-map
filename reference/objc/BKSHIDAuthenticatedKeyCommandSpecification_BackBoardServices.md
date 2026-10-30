# `BKSHIDAuthenticatedKeyCommandSpecification`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSProtobufSerializable`, `BSDescriptionStreamable`
- 2 instance variables, 6 properties, 12 instance methods, 3 class methods

## Instance variables

```
Q _context;
@"BKSHIDEventKeyCommand" _keyCommand;
```

## Properties

```
@property (TQ,N,V_context) context;
@property (T@"BKSHIDEventKeyCommand",&,N,V_keyCommand) keyCommand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDAuthenticatedKeyCommandSpecification supportsSecureCoding];
+[BKSHIDAuthenticatedKeyCommandSpecification protobufSchema];
+[BKSHIDAuthenticatedKeyCommandSpecification specificationWithKeyCommand:context:];
```

## Instance methods

```
-[BKSHIDAuthenticatedKeyCommandSpecification setKeyCommand:];
-[BKSHIDAuthenticatedKeyCommandSpecification initForProtobufDecoding];
-[BKSHIDAuthenticatedKeyCommandSpecification appendDescriptionToFormatter:];
-[BKSHIDAuthenticatedKeyCommandSpecification _init];
-[BKSHIDAuthenticatedKeyCommandSpecification setContext:];
-[BKSHIDAuthenticatedKeyCommandSpecification encodeWithCoder:];
-[BKSHIDAuthenticatedKeyCommandSpecification hash];
-[BKSHIDAuthenticatedKeyCommandSpecification description];
-[BKSHIDAuthenticatedKeyCommandSpecification initWithCoder:];
-[BKSHIDAuthenticatedKeyCommandSpecification keyCommand];
-[BKSHIDAuthenticatedKeyCommandSpecification context];
-[BKSHIDAuthenticatedKeyCommandSpecification isEqual:];
```
