# `LAPSPasscode`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"LACSExtractablePassword" _extractablePassword;
@"LACPasscode" _type;
```

## Properties

```
@property (T@"LACSExtractablePassword",R,N,V_extractablePassword) extractablePassword;
@property (T@"NSData",R,N) data;
@property (T@"NSString",R,N) passcode;
@property (T@"LACPasscode",R,N,V_type) type;
```

## Class methods

```
+[LAPSPasscode emptyPasscode];
```

## Instance methods

```
-[LAPSPasscode passcode];
-[LAPSPasscode data];
-[LAPSPasscode type];
-[LAPSPasscode isEqual:];
-[LAPSPasscode initWithPasscode:];
-[LAPSPasscode initWithLocalizedPasscode:type:];
-[LAPSPasscode extractablePassword];
-[LAPSPasscode initWithPasscode:type:];
```
