# `_UIMainMenuBaseMenuResponse`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenu" _menu;
@"NSString" _clientName;
@"_UIMainMenuSessionResponse" _sessionResponse;
```

## Properties

```
@property (T@"NSString",&,N,V_clientName) clientName;
@property (T@"_UIMainMenu",R,N,V_menu) menu;
@property (T@"_UIMainMenuSessionResponse",R,N,V_sessionResponse) sessionResponse;
```

## Class methods

```
+[_UIMainMenuBaseMenuResponse supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuBaseMenuResponse menu];
-[_UIMainMenuBaseMenuResponse setClientName:];
-[_UIMainMenuBaseMenuResponse encodeWithCoder:];
-[_UIMainMenuBaseMenuResponse clientName];
-[_UIMainMenuBaseMenuResponse hash];
-[_UIMainMenuBaseMenuResponse description];
-[_UIMainMenuBaseMenuResponse initWithCoder:];
-[_UIMainMenuBaseMenuResponse isEqual:];
-[_UIMainMenuBaseMenuResponse sessionResponse];
-[_UIMainMenuBaseMenuResponse _initWithMenu:clientName:sessionResponse:];
```
