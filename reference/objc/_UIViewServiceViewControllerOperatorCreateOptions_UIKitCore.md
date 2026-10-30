# `_UIViewServiceViewControllerOperatorCreateOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _hostCanDynamicallySpecifySupportedInterfaceOrientations;
@"NSString" _viewControllerClassName;
@"NSUUID" _contextToken;
@"NSArray" _displayConfigurations;
@"UITraitCollection" _traitCollection;
@"BSMachPortSendRight" _hostAccessibilityServerPort;
q _availableTextServices;
q _initialInterfaceOrientation;
```

## Properties

```
@property (T@"NSString",C,N,V_viewControllerClassName) viewControllerClassName;
@property (T@"NSUUID",&,N,V_contextToken) contextToken;
@property (T@"NSArray",C,N,V_displayConfigurations) displayConfigurations;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (T@"BSMachPortSendRight",&,N,V_hostAccessibilityServerPort) hostAccessibilityServerPort;
@property (Tq,N,V_availableTextServices) availableTextServices;
@property (Tq,N,V_initialInterfaceOrientation) initialInterfaceOrientation;
@property (TB,N,V_hostCanDynamicallySpecifySupportedInterfaceOrientations) hostCanDynamicallySpecifySupportedInterfaceOrientations;
```

## Class methods

```
+[_UIViewServiceViewControllerOperatorCreateOptions supportsSecureCoding];
```

## Instance methods

```
-[_UIViewServiceViewControllerOperatorCreateOptions setTraitCollection:];
-[_UIViewServiceViewControllerOperatorCreateOptions traitCollection];
-[_UIViewServiceViewControllerOperatorCreateOptions viewControllerClassName];
-[_UIViewServiceViewControllerOperatorCreateOptions contextToken];
-[_UIViewServiceViewControllerOperatorCreateOptions encodeWithCoder:];
-[_UIViewServiceViewControllerOperatorCreateOptions initWithCoder:];
-[_UIViewServiceViewControllerOperatorCreateOptions setHostAccessibilityServerPort:];
-[_UIViewServiceViewControllerOperatorCreateOptions setInitialInterfaceOrientation:];
-[_UIViewServiceViewControllerOperatorCreateOptions availableTextServices];
-[_UIViewServiceViewControllerOperatorCreateOptions displayConfigurations];
-[_UIViewServiceViewControllerOperatorCreateOptions hostAccessibilityServerPort];
-[_UIViewServiceViewControllerOperatorCreateOptions hostCanDynamicallySpecifySupportedInterfaceOrientations];
-[_UIViewServiceViewControllerOperatorCreateOptions initialInterfaceOrientation];
-[_UIViewServiceViewControllerOperatorCreateOptions setAvailableTextServices:];
-[_UIViewServiceViewControllerOperatorCreateOptions setContextToken:];
-[_UIViewServiceViewControllerOperatorCreateOptions setDisplayConfigurations:];
-[_UIViewServiceViewControllerOperatorCreateOptions setHostCanDynamicallySpecifySupportedInterfaceOrientations:];
-[_UIViewServiceViewControllerOperatorCreateOptions setViewControllerClassName:];
```
