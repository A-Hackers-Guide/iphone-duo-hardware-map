# `BKSHIDEventKeyCommand`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 13 properties, 27 instance methods, 9 class methods

## Instance variables

```
@"NSString" _input;
q _keyCode;
q _modifierFlags;
@"NSString" _unmodifiedInput;
@"NSString" _shiftModifiedInput;
@"NSString" _commandModifiedInput;
q _usagePage;
```

## Properties

```
@property (T@"NSString",&,N,V_unmodifiedInput) unmodifiedInput;
@property (T@"NSString",&,N,V_shiftModifiedInput) shiftModifiedInput;
@property (T@"NSString",&,N,V_commandModifiedInput) commandModifiedInput;
@property (Tq,N,V_usagePage) usagePage;
@property (TB,R) isRoutableKeyCommand;
@property (T@"NSString",R,N,V_input) input;
@property (Tq,R,N,V_keyCode) keyCode;
@property (Tq,R,N,V_modifierFlags) modifierFlags;
@property (TB,R,N) isTextualKeyCommand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventKeyCommand supportsSecureCoding];
+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:];
+[BKSHIDEventKeyCommand keyCommandForEvent:gsKeyboard:activeModifiers:];
+[BKSHIDEventKeyCommand keyCommandWithKeyCode:modifierFlags:];
+[BKSHIDEventKeyCommand _shouldMatchKeyCommandsForEvent:gsKeyboard:];
+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:];
+[BKSHIDEventKeyCommand keyCommandWithInput:modifierFlags:];
+[BKSHIDEventKeyCommand _isModifierKeyWithPage:usage:];
+[BKSHIDEventKeyCommand keyCommandForEvent:gsKeyboard:];
```

## Instance methods

```
-[BKSHIDEventKeyCommand input];
-[BKSHIDEventKeyCommand init];
-[BKSHIDEventKeyCommand modifierFlags];
-[BKSHIDEventKeyCommand isTextualKeyCommand];
-[BKSHIDEventKeyCommand setShiftModifiedInput:];
-[BKSHIDEventKeyCommand _appendKeyWithoutModifiersToDescriptionTarget:keyCodeString:];
-[BKSHIDEventKeyCommand describes:];
-[BKSHIDEventKeyCommand _sanitizedInputForDescription];
-[BKSHIDEventKeyCommand usagePage];
-[BKSHIDEventKeyCommand keyCode];
-[BKSHIDEventKeyCommand shiftModifiedInput];
-[BKSHIDEventKeyCommand encodeWithCoder:];
-[BKSHIDEventKeyCommand commandModifiedInput];
-[BKSHIDEventKeyCommand hash];
-[BKSHIDEventKeyCommand _appendPropertiesCommon:];
-[BKSHIDEventKeyCommand description];
-[BKSHIDEventKeyCommand initWithCoder:];
-[BKSHIDEventKeyCommand appendDescriptionToStream:];
-[BKSHIDEventKeyCommand isRoutableKeyCommand];
-[BKSHIDEventKeyCommand copyWithZone:];
-[BKSHIDEventKeyCommand setUnmodifiedInput:];
-[BKSHIDEventKeyCommand isModifierOnlyCommand];
-[BKSHIDEventKeyCommand isEqual:];
-[BKSHIDEventKeyCommand setCommandModifiedInput:];
-[BKSHIDEventKeyCommand _initWithInput:keyCode:modifierFlags:];
-[BKSHIDEventKeyCommand unmodifiedInput];
-[BKSHIDEventKeyCommand setUsagePage:];
```
