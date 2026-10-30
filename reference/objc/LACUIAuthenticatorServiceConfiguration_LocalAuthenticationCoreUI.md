# `LACUIAuthenticatorServiceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 16 instance variables, 16 properties, 38 instance methods, 1 class methods

## Instance variables

```
B _headerHidden;
B _requiresIntent;
@"NSString" _title;
@"NSString" _bundleIdentifier;
@"NSString" _iconPath;
@"NSString" _subtitle;
@"NSString" _prompt;
@"NSString" _verifyPrompt;
@"NSString" _cancelButtonTitle;
@"NSString" _fallbackButtonTitle;
@"NSString" _passwordFieldPlaceholder;
Q _requirement;
q _passcodeLength;
Q _mode;
@"NSData" _contextData;
Q _style;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",&,N,V_iconPath) iconPath;
@property (T@"NSString",&,N,V_subtitle) subtitle;
@property (T@"NSString",&,N,V_prompt) prompt;
@property (T@"NSString",&,N,V_verifyPrompt) verifyPrompt;
@property (T@"NSString",&,N,V_cancelButtonTitle) cancelButtonTitle;
@property (T@"NSString",&,N,V_fallbackButtonTitle) fallbackButtonTitle;
@property (T@"NSString",&,N,V_passwordFieldPlaceholder) passwordFieldPlaceholder;
@property (TQ,R,N,V_requirement) requirement;
@property (Tq,N,V_passcodeLength) passcodeLength;
@property (TQ,N,V_mode) mode;
@property (T@"NSData",R,N,V_contextData) contextData;
@property (TQ,N,V_style) style;
@property (TB,N,V_headerHidden) headerHidden;
@property (TB,N,V_requiresIntent) requiresIntent;
```

## Class methods

```
+[LACUIAuthenticatorServiceConfiguration supportsSecureCoding];
```

## Instance methods

```
-[LACUIAuthenticatorServiceConfiguration prompt];
-[LACUIAuthenticatorServiceConfiguration initWithContext:];
-[LACUIAuthenticatorServiceConfiguration requirement];
-[LACUIAuthenticatorServiceConfiguration validateConfiguration];
-[LACUIAuthenticatorServiceConfiguration subtitle];
-[LACUIAuthenticatorServiceConfiguration bundleIdentifier];
-[LACUIAuthenticatorServiceConfiguration contextData];
-[LACUIAuthenticatorServiceConfiguration setSubtitle:];
-[LACUIAuthenticatorServiceConfiguration style];
-[LACUIAuthenticatorServiceConfiguration setMode:];
-[LACUIAuthenticatorServiceConfiguration setStyle:];
-[LACUIAuthenticatorServiceConfiguration title];
-[LACUIAuthenticatorServiceConfiguration iconPath];
-[LACUIAuthenticatorServiceConfiguration encodeWithCoder:];
-[LACUIAuthenticatorServiceConfiguration mode];
-[LACUIAuthenticatorServiceConfiguration setIconPath:];
-[LACUIAuthenticatorServiceConfiguration description];
-[LACUIAuthenticatorServiceConfiguration initWithCoder:];
-[LACUIAuthenticatorServiceConfiguration setTitle:];
-[LACUIAuthenticatorServiceConfiguration setBundleIdentifier:];
-[LACUIAuthenticatorServiceConfiguration isEqual:];
-[LACUIAuthenticatorServiceConfiguration setPrompt:];
-[LACUIAuthenticatorServiceConfiguration passcodeLength];
-[LACUIAuthenticatorServiceConfiguration cancelButtonTitle];
-[LACUIAuthenticatorServiceConfiguration setCancelButtonTitle:];
-[LACUIAuthenticatorServiceConfiguration fallbackButtonTitle];
-[LACUIAuthenticatorServiceConfiguration setFallbackButtonTitle:];
-[LACUIAuthenticatorServiceConfiguration setPasscodeLength:];
-[LACUIAuthenticatorServiceConfiguration initWithContext:requirement:options:];
-[LACUIAuthenticatorServiceConfiguration setVerifyPrompt:];
-[LACUIAuthenticatorServiceConfiguration verifyPrompt];
-[LACUIAuthenticatorServiceConfiguration headerHidden];
-[LACUIAuthenticatorServiceConfiguration initWithContext:requirement:];
-[LACUIAuthenticatorServiceConfiguration passwordFieldPlaceholder];
-[LACUIAuthenticatorServiceConfiguration requiresIntent];
-[LACUIAuthenticatorServiceConfiguration setHeaderHidden:];
-[LACUIAuthenticatorServiceConfiguration setPasswordFieldPlaceholder:];
-[LACUIAuthenticatorServiceConfiguration setRequiresIntent:];
```
