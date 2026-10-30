# `_UIMainMenuStateResponse`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _menuStates;
@"_UIMainMenuState" _uncategorizedMenuState;
```

## Properties

```
@property (T@"_UIMainMenuState",R,N) menuState;
@property (T@"NSDictionary",R,N,V_menuStates) menuStates;
@property (T@"_UIMainMenuState",R,N,V_uncategorizedMenuState) uncategorizedMenuState;
```

## Class methods

```
+[_UIMainMenuStateResponse supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuStateResponse encodeWithCoder:];
-[_UIMainMenuStateResponse hash];
-[_UIMainMenuStateResponse description];
-[_UIMainMenuStateResponse initWithCoder:];
-[_UIMainMenuStateResponse isEqual:];
-[_UIMainMenuStateResponse _initWithMenuStates:uncategorizedMenuState:];
-[_UIMainMenuStateResponse menuState];
-[_UIMainMenuStateResponse menuStates];
-[_UIMainMenuStateResponse uncategorizedMenuState];
```
