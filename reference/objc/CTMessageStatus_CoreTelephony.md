# `CTMessageStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 0 class methods

## Instance variables

```
I _messageId;
i _messageType;
i _result;
```

## Properties

```
@property (TI,R,V_messageId) messageId;
@property (Ti,R,V_messageType) messageType;
@property (Ti,R,V_result) result;
```

## Instance methods

```
-[CTMessageStatus messageType];
-[CTMessageStatus result];
-[CTMessageStatus messageId];
-[CTMessageStatus initWithMessageId:messageType:result:];
```
