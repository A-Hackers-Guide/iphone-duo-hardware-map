# `LACUIPasscodeViewState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
q _rawValue;
@"LACUIPasscodeViewStyle" _style;
@"NSString" _callerBundleIdentifier;
@"NSString" _callerIconPath;
@"NSString" _title;
@"NSString" _subtitle;
@"UIView" _accessoryView;
```

## Properties

```
@property (Tq,R,N,V_rawValue) rawValue;
@property (T@"LACUIPasscodeViewStyle",R,N,V_style) style;
@property (T@"NSString",R,N,V_callerBundleIdentifier) callerBundleIdentifier;
@property (T@"NSString",R,N,V_callerIconPath) callerIconPath;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSString",R,N,V_subtitle) subtitle;
@property (T@"UIView",R,N,V_accessoryView) accessoryView;
```

## Class methods

```
+[LACUIPasscodeViewState activeStateWithTitle:subtitle:callerBundleIdentifier:accessoryView:];
+[LACUIPasscodeViewState backOffStateWithTitle:subtitle:callerBundleIdentifier:];
```

## Instance methods

```
-[LACUIPasscodeViewState accessoryView];
-[LACUIPasscodeViewState subtitle];
-[LACUIPasscodeViewState rawValue];
-[LACUIPasscodeViewState style];
-[LACUIPasscodeViewState title];
-[LACUIPasscodeViewState isEqual:];
-[LACUIPasscodeViewState callerBundleIdentifier];
-[LACUIPasscodeViewState callerIconPath];
-[LACUIPasscodeViewState initWithRawValue:title:subtitle:callerBundleIdentifier:accessoryView:style:];
-[LACUIPasscodeViewState initWithRawValue:title:subtitle:callerBundleIdentifier:callerIconPath:accessoryView:style:];
-[LACUIPasscodeViewState withCallerIconPath:];
-[LACUIPasscodeViewState withStyle:];
```
