# `LACDTOEventBus`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOEventBus`
- 2 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@ observers;
dispatcher;
```

## Properties

```
@property (T@,N,R,Vobservers) observers;
```

## Instance methods

```
-[LACDTOEventBus init];
-[LACDTOEventBus observers];
-[LACDTOEventBus addEventHandler:];
-[LACDTOEventBus removeEventHandler:];
-[LACDTOEventBus dispatchEvent:sender:];
```
