# `_UIHIDEventSenderDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`, `BSDescriptionStreamable`
- 2 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _eventType;
Q _senderID;
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
+[_UIHIDEventSenderDescriptor descriptorWithEvent:];
```

## Instance methods

```
-[_UIHIDEventSenderDescriptor succinctDescriptionBuilder];
-[_UIHIDEventSenderDescriptor init];
-[_UIHIDEventSenderDescriptor appendDescriptionToFormatter:];
-[_UIHIDEventSenderDescriptor descriptionWithMultilinePrefix:];
-[_UIHIDEventSenderDescriptor succinctDescription];
-[_UIHIDEventSenderDescriptor hash];
-[_UIHIDEventSenderDescriptor description];
-[_UIHIDEventSenderDescriptor copyWithZone:];
-[_UIHIDEventSenderDescriptor isEqual:];
-[_UIHIDEventSenderDescriptor descriptionBuilderWithMultilinePrefix:];
-[_UIHIDEventSenderDescriptor initWithSenderID:eventType:];
```
