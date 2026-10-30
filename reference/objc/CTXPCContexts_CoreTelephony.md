# `CTXPCContexts`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _subscriptions;
@"NSArray" _existingUserSubscriptions;
@"NSUUID" _dataPreferred;
@"NSUUID" _voicePreferred;
```

## Properties

```
@property (T@"NSArray",&,N,V_subscriptions) subscriptions;
@property (T@"NSUUID",&,N,V_dataPreferred) dataPreferred;
@property (T@"NSUUID",&,N,V_voicePreferred) voicePreferred;
@property (T@"NSArray",&,N,V_existingUserSubscriptions) existingUserSubscriptions;
```

## Class methods

```
+[CTXPCContexts supportsSecureCoding];
```

## Instance methods

```
-[CTXPCContexts subscriptions];
-[CTXPCContexts dataPreferred];
-[CTXPCContexts findForUuid:within:];
-[CTXPCContexts findForUuid:];
-[CTXPCContexts findForSlot:within:];
-[CTXPCContexts findForAccount:within:];
-[CTXPCContexts findForSlot:];
-[CTXPCContexts existingUserSubscriptions];
-[CTXPCContexts encodeWithCoder:];
-[CTXPCContexts description];
-[CTXPCContexts initWithCoder:];
-[CTXPCContexts setSubscriptions:];
-[CTXPCContexts setDataPreferred:];
-[CTXPCContexts copyWithZone:];
-[CTXPCContexts voicePreferred];
-[CTXPCContexts findForAccount:];
-[CTXPCContexts isEqual:];
-[CTXPCContexts setExistingUserSubscriptions:];
-[CTXPCContexts setVoicePreferred:];
```
