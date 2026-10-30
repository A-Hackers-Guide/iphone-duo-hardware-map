# `LACUIPasscodeNumberPadView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _character;
@"TPNumberPadButton" _characterView;
B _darkMode;
d _diameter;
```

## Properties

```
@property (TB,N,V_darkMode) darkMode;
@property (Td,N,V_diameter) diameter;
```

## Class methods

```
+[LACUIPasscodeNumberPadView isCharacterSupported:];
```

## Instance methods

```
-[LACUIPasscodeNumberPadView accessibilityHint];
-[LACUIPasscodeNumberPadView setDarkMode:];
-[LACUIPasscodeNumberPadView darkMode];
-[LACUIPasscodeNumberPadView _configureView];
-[LACUIPasscodeNumberPadView diameter];
-[LACUIPasscodeNumberPadView setDiameter:];
-[LACUIPasscodeNumberPadView _currentNumberPadButton];
-[LACUIPasscodeNumberPadView initWithCharacter:darkMode:diameter:];
```
