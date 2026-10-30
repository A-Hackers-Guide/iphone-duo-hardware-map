# `_UIViewServiceControllerOperatorCreateResult`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _preferredStatusBarVisibility;
@"_UIHostedWindowHostingHandle" _serviceWindowHostingHandle;
@"NSArray" _supportedInterfaceOrientations;
q _preferredStatusBarStyle;
@"BSMachPortSendRight" _accessibilityServerPort;
```

## Properties

```
@property (T@"_UIHostedWindowHostingHandle",&,N,V_serviceWindowHostingHandle) serviceWindowHostingHandle;
@property (T@"NSArray",C,N,V_supportedInterfaceOrientations) supportedInterfaceOrientations;
@property (Tq,N,V_preferredStatusBarStyle) preferredStatusBarStyle;
@property (Ti,N,V_preferredStatusBarVisibility) preferredStatusBarVisibility;
@property (T@"BSMachPortSendRight",&,N,V_accessibilityServerPort) accessibilityServerPort;
```

## Class methods

```
+[_UIViewServiceControllerOperatorCreateResult supportsSecureCoding];
```

## Instance methods

```
-[_UIViewServiceControllerOperatorCreateResult supportedInterfaceOrientations];
-[_UIViewServiceControllerOperatorCreateResult setPreferredStatusBarVisibility:];
-[_UIViewServiceControllerOperatorCreateResult encodeWithCoder:];
-[_UIViewServiceControllerOperatorCreateResult initWithCoder:];
-[_UIViewServiceControllerOperatorCreateResult preferredStatusBarStyle];
-[_UIViewServiceControllerOperatorCreateResult preferredStatusBarVisibility];
-[_UIViewServiceControllerOperatorCreateResult accessibilityServerPort];
-[_UIViewServiceControllerOperatorCreateResult serviceWindowHostingHandle];
-[_UIViewServiceControllerOperatorCreateResult setAccessibilityServerPort:];
-[_UIViewServiceControllerOperatorCreateResult setPreferredStatusBarStyle:];
-[_UIViewServiceControllerOperatorCreateResult setServiceWindowHostingHandle:];
-[_UIViewServiceControllerOperatorCreateResult setSupportedInterfaceOrientations:];
```
