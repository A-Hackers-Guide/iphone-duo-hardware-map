# `_UIMainMenuStateRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuSession" _providedSession;
B _includeUncategorizedMenuState;
@"_UIMainMenuSessionIdentifier" _sessionIdentifier;
@"NSSet" _menuIdentifiers;
```

## Properties

```
@property (T@"_UIMainMenuSessionIdentifier",R,N,V_sessionIdentifier) _sessionIdentifier;
@property (T@"_UIMainMenuIdentifier",R,N) menuIdentifier;
@property (T@"NSSet",&,N,V_menuIdentifiers) menuIdentifiers;
@property (T@"_UIMainMenuSession",R,N) session;
@property (TB,N,V_includeUncategorizedMenuState) includeUncategorizedMenuState;
```

## Class methods

```
+[_UIMainMenuStateRequest supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuStateRequest encodeWithCoder:];
-[_UIMainMenuStateRequest hash];
-[_UIMainMenuStateRequest description];
-[_UIMainMenuStateRequest initWithCoder:];
-[_UIMainMenuStateRequest session];
-[_UIMainMenuStateRequest isEqual:];
-[_UIMainMenuStateRequest _sessionIdentifier];
-[_UIMainMenuStateRequest initWithMenuIdentifier:session:];
-[_UIMainMenuStateRequest menuIdentifiers];
-[_UIMainMenuStateRequest includeUncategorizedMenuState];
-[_UIMainMenuStateRequest initWithMenuIdentifiers:session:];
-[_UIMainMenuStateRequest menuIdentifier];
-[_UIMainMenuStateRequest setIncludeUncategorizedMenuState:];
-[_UIMainMenuStateRequest setMenuIdentifiers:];
```
